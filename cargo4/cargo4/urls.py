"""
URL configuration for cargo4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
 
from cargo4app.views import *
from home.views import *



urlpatterns = [

   
    # Users
    path('adminlogin/',login_view),
    path('custregister/',register_view),
    path('custlogin/',cust_login),
    path('empregister/',emp_register),
    path('emplogin/',emp_login),

    path('dsbrd/',dsbrd),
   
   
    

    # HOME URL
    path('about/',about),
    path('company/',company),
    path('contact/',contact),
    path('',index),
    path('service/',service),
    path('shop/',shop),
    path('dashboard/',dashboard),
    path('emdashboard/',emdashboard),
    
    # customer
    path('book/',booking_view),
    path('success/',success),
    path('invoice/<int:booking_id>/',generate_invoice),
    path('inquiry/', inquiry_view),
    path('feedback/', feedback_view),
     
    
    #1 ADMIN URL 
    path('adminlist/', admin_list),  # List of admins
    path('createadmin/', admin_create),  # Create new admin
    path('updateadmin/<int:pk>/', admin_update),  # Update admin
    path('deleteadmin/<int:pk>/', admin_delete),  # Delete admin
    
   
    # 4 CUSTOMER URL
    path('customerlist/',customer_list),
    path('createcustomer/',customer_create),
    path('updatecustomer/<int:id>/',customer_update),
    path('deletecustomer/<int:id>/',customer_delete),
    
    #2 CARGO URL
    path('cargolist/',cargo_list),
    path('cargocreate/',cargo_create),
    path('cargoupdate/<int:pk>/',cargo_update),
    path('cargodelete/<int:pk>/',cargo_delete),
    
    
    #5 DELIVERY URL
    path('deliverylist/',delivery_list),
    path('deletedelivery/<int:id>/', delivery_delete ),
    path('updatedelivery/<int:id>/',delivery_update),
    path('createdelivery/',delivery_create),
    
    #6 DESIGNATION URL
    path('designationlist/',designation_list),
    path('designationcreate/',designation_create),
    path('designationupdate/<int:id>/',designation_update),
    path('designationdelete/<int:id>/',designation_delete),
    
    #7 EMPLOYEE URL
    path('employeelist/',employee_list),
    path('createemployee/',employee_create),
    path('updateemployee/<int:id>/',employee_update),
    path('deleteemployee/<int:id>/',employee_delete),
    
    #8 FEEDBACK URL
    path('feedbacklist/',feedback_list),
    path('feedbackcreate/',feedback_create),
    path('feedbackupdate/<int:id>/',feedback_update),
    path('feedbackdelete/<int:id>/',feedback_delete),
    
    #9 INVENTORY URL
    path('inventorylist/',inventory_list),
    path('inventorycreate/',inventory_create),
    path('inventoryupdate/<int:id>/',inventory_update),
    path('inventorydelete/<int:id>/',inventory_delete),
    
    # 11 MATERIAL URL
    path('materiallist/',materials_list),
    path('materialcreate/',material_create),
    path('materialupdate/<int:id>/',material_update),
    path('materialdelete/<int:id>/',material_delete),
    # 15 PRODUCT URL
    path('productlist/',product_list),
    path('productcreate/',product_create),
    path('productupdate/<int:id>/',product_update),
    path('productdelete/<int:id>/',product_delete),
    
    # 16 SERVICE URL
    path('servicelist/',service_list),
    path('servicecreate/',service_create),
    path('serviceupdate/<int:id>/',service_update),
    path('servicedelete/<int:id>/',service_delete),
    
    # 17 SUPPLIER URL
    path('supplierlist/',supplier_list),
    path('suppliercreate/',supplier_create),
    path('supplierupdate/<int:id>/',supplier_update),
    path('supplierdelete/<int:id>/',supplier_delete),
    
    # 18 WAREHOUSE URL
    path('warehouselist/',warehouse_list),
    path('warehousecreate/',warehouse_create),
    path('warehouseupdate/<int:id>/',warehouse_update),
    path('warehousedelete/<int:id>/',warehouse_delete),
    #3 CARGO_WEIGHT URL
    path('cargoweightlist/',cargo_weight_list),
    path('cargoweightcreate/',cargo_weight_create),
    path('cargoweightupdate/<int:id>/',cargo_weight_update),
    path('cargoweightdelete/<int:id>/',cargo_weight_delete),
    
    #10 INVOICE URL
    path('invoicelist/',invoice_list),
    path('invoicecreate/',invoice_create),
    path('invoiceupdate/<int:id>/',invoice_update),
    path('invoicedelete/<int:id>/',invoice_delete),
        
    # 12 ORDER_DETAIL URL
    path('orderlist/',order_list),
    path('ordercreate/',order_create),
    path('orderupdate/<int:id>/',order_update),
    path('orderdelete/<int:id>/',order_delete),

 # 13 PAYMENT URL 
    path('paymentlist/',payment_list),
    path('paymentcreate/',payment_create),
    path('paymentupdate/<int:id>/',payment_update),
    path('paymentdelete/<int:id>/',payment_delete),  

 # 14 PRICE URL
    path('pricelist/',price_list),
    path('pricecreate/',price_create),
    path('priceupdate/<int:id>/',price_update),
    path('pricedelete/<int:id>/',price_delete),
    
    # 19 TRUCK URL
    path('trucklist/',truck_list), 
    path('truckcreate/',create_truck),
    path('truckupdate/<int:id>/',update_truck),
    path('truckdelete/<int:id>/',delete_truck),
    
    # 20 INQUIRY URL
    path('inquirylist/',inquiry_list),
    path('inquirycreate/',create_inquiry),
    path('inquiryupdate/<int:id>/',update_inquiry),
    path('inquirydelete/<int:id>/',delete_inquiry),
    
    # 21 BOOKING URL
    path('bookinglist/',booking_list),
    path('bookingcreate/',create_booking),
    path('bookingupdate/<int:id>/',update_booking),
    path('bookingdelete/<int:id>/',delete_booking),
    
    # 22 NEW FEEDBACK URL
    path('fblist/',cust_fb_list),
    path('fbcreate/',newfb_create),
    path('newfbdelete/<int:id>/',newfb_delete),
    path('newfbupdate/<int:id>/',newfb_update)

]