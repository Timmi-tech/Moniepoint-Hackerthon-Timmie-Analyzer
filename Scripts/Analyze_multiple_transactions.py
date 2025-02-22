import os

# Root folder containing the data for multiple transactions 
root_folder = r"C:\Users\user\Desktop\MoniePoint Hackerthon\Data"

# Dictionary to store analytics
sales_volume_per_day = {}
sales_value_per_day = {}
product_sales = {}
staff_sales_per_month = {}
hourly_sales_volume = {}

# Created a Function to process each transaction file
def processing_transaction_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")  # Split line by comma
            if len(parts) != 4:
                print(f"Skipping malformed line: {line}")
                continue

            # Extract transaction details
            sales_staff_id = parts[0]
            transaction_time = parts[1]
            product_list = parts[2].strip("[]")  # Remove brackets
            sale_amount = float(parts[3])

            # Extract date, month, and hour
            date_part, time_part = transaction_time.split("T")
            hour_part = time_part[:2]  # Get the hour
            year, month, day = date_part.split("-")

            # Update sales volume and value per day
            sales_volume_per_day[date_part] = sales_volume_per_day.get(date_part, 0) + 1
            sales_value_per_day[date_part] = sales_value_per_day.get(date_part, 0) + sale_amount

            # Update most sold product by volume
            for product in product_list.split("|"):  # Split products by '|'
                if ":" not in product:
                    print(f"Skipping malformed product: {product}")
                    continue
                product_id, quantity = product.split(":")
                quantity = int(quantity)
                product_sales[product_id] = product_sales.get(product_id, 0) + quantity

            # Update highest sales staff per month
            month_key = f"{year}-{month}"
            if month_key not in staff_sales_per_month:
                staff_sales_per_month[month_key] = {}
            staff_sales_per_month[month_key][sales_staff_id] = (
                staff_sales_per_month[month_key].get(sales_staff_id, 0) + sale_amount
            )

            # Update highest hour of the day by transaction volume
            hourly_sales_volume[hour_part] = hourly_sales_volume.get(hour_part, 0) + 1

# Process all transaction files in folders
for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)
    if os.path.isdir(folder_path):  # Ensure it's a folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".txt"):  # Process only text files
                file_path = os.path.join(folder_path, file_name)
                print(f"Processing file: {file_path}")
                processing_transaction_file(file_path)

# Find required analytics

# 1. Highest sales volume in a day
highest_sales_volume_day = max(sales_volume_per_day, key=sales_volume_per_day.get)
print(f"Highest sales volume in a day: {highest_sales_volume_day} with {sales_volume_per_day[highest_sales_volume_day]} transactions")

# 2. Highest sales value in a day
highest_sales_value_day = max(sales_value_per_day, key=sales_value_per_day.get)
print(f"Highest sales value in a day: {highest_sales_value_day} with ${sales_value_per_day[highest_sales_value_day]:.2f}")

# 3. Most sold product ID by volume
most_sold_product = max(product_sales, key=product_sales.get)
print(f"Most sold product ID: {most_sold_product} with {product_sales[most_sold_product]} units sold")

# 4. Highest sales staff ID for each month
for month, staff_data in staff_sales_per_month.items():
    top_staff = max(staff_data, key=staff_data.get)
    print(f"Top sales staff for {month}: Staff ID {top_staff} with sales of ${staff_data[top_staff]:.2f}")

# 5. Highest hour of the day by average transaction volume
busiest_hour = max(hourly_sales_volume, key=hourly_sales_volume.get)
print(f"Busiest hour of the day: {busiest_hour}:00 with {hourly_sales_volume[busiest_hour]} transactions")

output_file = "sales_report.txt"

with open(output_file, "w", encoding="utf-8") as file:
    file.write(f"🔹 **Sales Report** 🔹\n\n")

    file.write(f"📌 Highest Sales Volume in a Day: {highest_sales_volume_day} ({sales_volume_per_day[highest_sales_volume_day]} transactions)\n")
    file.write(f"📌 Highest Sales Value in a Day: {highest_sales_value_day} (${sales_value_per_day[highest_sales_value_day]:.2f})\n")
    file.write(f"📌 Most Sold Product ID: {most_sold_product} ({product_sales[most_sold_product]} units sold)\n\n")

    file.write("📊 **Top Sales Staff for Each Month:**\n")
    for month, staff_data in staff_sales_per_month.items():
        top_staff = max(staff_data, key=staff_data.get)
        file.write(f"   - {month}: Staff ID {top_staff} (${staff_data[top_staff]:.2f})\n")

    file.write(f"\n⏳ **Busiest Hour of the Day:** {busiest_hour}:00 ({hourly_sales_volume[busiest_hour]} transactions)\n")

print(f"✅ Results saved to {output_file}")


