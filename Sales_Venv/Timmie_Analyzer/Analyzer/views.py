from django.shortcuts import render
from django.core.files.storage import default_storage
import os
import zipfile
import shutil

def handle_uploaded_file(file):
    # Save uploaded ZIP file
    zip_path = default_storage.save(f"uploads/{file.name}", file)
    extract_path = f"uploads/extracted/{os.path.splitext(file.name)[0]}"
    os.makedirs(extract_path, exist_ok=True)
    
    # Extract ZIP file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    
    # Process extracted files
    analytics = process_transaction_files(extract_path)
    
    # Clean up extracted files after processing
    shutil.rmtree(extract_path)
    
    return analytics, file.name  # Return analytics and file name

def process_transaction_files(folder_path):
    sales_volume_per_day = {}
    sales_value_per_day = {}
    product_sales = {}
    staff_sales_per_month = {}
    hourly_sales_volume = {}

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith(".txt"):
            with open(file_path, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) != 4:
                        continue

                    sales_staff_id, transaction_time, product_list, sale_amount = parts
                    sale_amount = float(sale_amount)
                    date_part, time_part = transaction_time.split("T")
                    hour_part = time_part[:2]
                    year, month, day = date_part.split("-")

                    # Update daily sales volume and value
                    sales_volume_per_day[date_part] = sales_volume_per_day.get(date_part, 0) + 1
                    sales_value_per_day[date_part] = sales_value_per_day.get(date_part, 0) + sale_amount

                    # Update product sales count
                    for product in product_list.strip("[]").split("|"):
                        if ":" in product:
                            product_id, quantity = product.split(":")
                            product_sales[product_id] = product_sales.get(product_id, 0) + int(quantity)

                    # Update staff sales per month
                    month_key = f"{year}-{month}"
                    if month_key not in staff_sales_per_month:
                        staff_sales_per_month[month_key] = {}
                    staff_sales_per_month[month_key][sales_staff_id] = (
                        staff_sales_per_month[month_key].get(sales_staff_id, 0) + sale_amount
                    )

                    # Update hourly sales volume
                    hourly_sales_volume[hour_part] = hourly_sales_volume.get(hour_part, 0) + 1

    # Find max values
    highest_sales_day = max(sales_volume_per_day, key=sales_volume_per_day.get, default="N/A")
    highest_sales_value_day = max(sales_value_per_day, key=sales_value_per_day.get, default="N/A")
    most_sold_product = max(product_sales, key=product_sales.get, default="N/A")
    busiest_hour = max(hourly_sales_volume, key=hourly_sales_volume.get, default="N/A")

    # Add missing values
    highest_sales_volume = sales_volume_per_day.get(highest_sales_day, 0)
    highest_sales_value = sales_value_per_day.get(highest_sales_value_day, 0)
    most_sold_quantity = product_sales.get(most_sold_product, 0)
    busiest_hour_transactions = hourly_sales_volume.get(busiest_hour, 0)

    analytics = {
        "highest_sales_day": highest_sales_day,
        "highest_sales_volume": highest_sales_volume,
        "highest_sales_value_day": highest_sales_value_day,
        "highest_sales_value": highest_sales_value,
        "most_sold_product": most_sold_product,
        "most_sold_quantity": most_sold_quantity,
        "busiest_hour": busiest_hour,
        "busiest_hour_transactions": busiest_hour_transactions,
        "top_staff_per_month": {
            month: max(staff.items(), key=lambda x: x[1], default=("N/A", 0))
            for month, staff in staff_sales_per_month.items()
        }
    }

    return analytics

def upload_file_view(request):
    analytics = None
    file_name = None
    if request.method == "POST" and request.FILES.get("zip_file"):
        file = request.FILES["zip_file"]
        analytics, file_name = handle_uploaded_file(file)
    
    return render(request, "upload.html", {"analytics": analytics, "uploaded_file_name": file_name})
