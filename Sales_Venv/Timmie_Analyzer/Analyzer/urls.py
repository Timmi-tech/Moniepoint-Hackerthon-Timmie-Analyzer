from django.urls import path
from . import views


urlpatterns = [
    path('sales', views.upload_file_view, name='upload_file_view'),
]