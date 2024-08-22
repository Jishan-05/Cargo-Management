# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from cargo4app.models import *

class Admin(models.Model):
    admin_id = models.AutoField(db_column='Admin_id', primary_key=True)  # Field name made lowercase.
    admin_name = models.CharField(db_column='Admin_name', max_length=45)  # Field name made lowercase.
    admin_pass = models.CharField(db_column='Admin_pass', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cargo(models.Model):
    cargo_id = models.IntegerField(primary_key=True)
    cust_id = models.IntegerField()
    product_id = models.IntegerField(db_column='Product_id')  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='Emp_id')  # Field name made lowercase.
    weight = models.CharField(max_length=10)
    bill_no = models.IntegerField(db_column='Bill_no')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cargo'


class CargoWeight(models.Model):
    weight_id = models.IntegerField(primary_key=True)
    weight = models.CharField(max_length=30)
    measurement_unit = models.CharField(max_length=30)
    cargo = models.ForeignKey(Cargo, models.CASCADE)
    product = models.ForeignKey(Cargo, models.CASCADE, related_name='cargoweight_product_set')

    class Meta:
        managed = False
        db_table = 'cargo_weight'


class Customer(models.Model):
    # cust_id = models.IntegerField(primary_key=True)
    cust_id = models.AutoField(primary_key=True)
    cust_firstname = models.CharField(max_length=10)
    customer_lastname = models.CharField(max_length=10)
    cust_password = models.CharField(db_column='Cust_password', max_length=255)  # Field name made lowercase.
    cust_gender = models.CharField(db_column='Cust_gender', max_length=10)  # Field name made lowercase.
    cust_contact_no_field = models.IntegerField(db_column='Cust_contact_no_field' )  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cust_email = models.CharField(db_column='Cust_email', max_length=30)  # Field name made lowercase.
    cust_address = models.CharField(db_column='Cust_address', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Delivery(models.Model):
    delivery_id = models.IntegerField(db_column='Delivery_id', primary_key=True)  # Field name made lowercase.
    cargo_id = models.IntegerField(db_column='Cargo_id')  # Field name made lowercase.
    pickup_date = models.DateField(db_column='Pickup_date')  # Field name made lowercase.
    delivery_date = models.DateField(db_column='Delivery_date')  # Field name made lowercase.
    pickup_address = models.CharField(db_column='Pickup_address', max_length=100)  # Field name made lowercase.
    destination_address = models.CharField(db_column='Destination_address', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'delivery'


class Designation(models.Model):
    designation_id = models.IntegerField(db_column='Designation_id', primary_key=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=20)  # Field name made lowercase.
    qualification = models.CharField(db_column='Qualification', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'designation'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Employee(models.Model):
    emp_id = models.AutoField(db_column='Emp_id', primary_key=True)  # Field name made lowercase.
    emp_firstname = models.CharField(db_column='Emp_Firstname', max_length=10)  # Field name made lowercase.
    emp_lastname = models.CharField(db_column='Emp_Lastname', max_length=10)  # Field name made lowercase.
    emp_password = models.CharField(db_column='Emp_password', max_length=10)  # Field name made lowercase.
    designation_id = models.IntegerField(db_column='Designation_id')  # Field name made lowercase.
    experience = models.CharField(db_column='Experience', max_length=30)  # Field name made lowercase.
    emp_salary = models.IntegerField(db_column='Emp_salary', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=5)  # Field name made lowercase.
    emp_dob = models.DateField(db_column='Emp_DOB', blank=True, null=True)  # Field name made lowercase.
    emp_doj = models.DateField(db_column='Emp_DOJ', blank=True, null=True)  # Field name made lowercase.
    emp_contact_no = models.BigIntegerField(db_column='Emp_contact_no', blank=True, null=True)  # Field name made lowercase.
    emp_email = models.CharField(db_column='Emp_email', max_length=30)  # Field name made lowercase.
    emp_address = models.CharField(db_column='Emp_address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    working_days = models.CharField(db_column='Working_days', max_length=60, blank=True, null=True)  # Field name made lowercase.
    leave_days = models.CharField(db_column='Leave_days', max_length=60,blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'



class Feedback(models.Model):
    f_id = models.IntegerField(db_column='F_id', primary_key=True)  # Field name made lowercase.
    feedback = models.CharField(db_column='Feedback', max_length=50)  # Field name made lowercase.
    f_date = models.DateField(db_column='F_date')  # Field name made lowercase.
    cust_id = models.IntegerField(db_column='Cust_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feedback'


class Inventory(models.Model):
    inventory_id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    arrival_date = models.DateField(db_column='Arrival_date')  # Field name made lowercase.
    departure_date = models.DateField(db_column='Departure_date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory'


class Invoice(models.Model):
    invoice_id = models.IntegerField(db_column='Invoice_id', primary_key=True)  # Field name made lowercase.
    order = models.ForeignKey('OrderDetail', models.CASCADE)
    due_date = models.DateField(db_column='Due_Date')  # Field name made lowercase.
    price = models.ForeignKey('Price', models.CASCADE)

    class Meta:
        managed = False
        db_table = 'invoice'


class Materials(models.Model):
    material_id = models.IntegerField(db_column='Material_id', primary_key=True)  # Field name made lowercase.
    material_name = models.CharField(db_column='Material_name', max_length=20)  # Field name made lowercase.
    material_type = models.CharField(max_length=60)
    quantity = models.CharField(db_column='Quantity', max_length=20)  # Field name made lowercase.
    sup = models.ForeignKey('Supplier', models.CASCADE, db_column='Sup_id')  # Field name made lowercase.
    materialprice = models.IntegerField(db_column='Materialprice')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'materials'


class OrderDetail(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_date = models.DateField()
    pay_method = models.CharField(max_length=30)
    cust = models.ForeignKey(Customer, models.CASCADE)
    product = models.ForeignKey('Product', models.CASCADE)
    service = models.ForeignKey('Service', models.CASCADE)

    class Meta:
        managed = False
        db_table = 'order_detail'


class Payment(models.Model):
    pay_id = models.IntegerField(primary_key=True)
    pay_date = models.DateField(db_column='Pay_date')  # Field name made lowercase.
    price_id = models.IntegerField()
    order = models.ForeignKey(OrderDetail, models.CASCADE)
    cust = models.ForeignKey(Customer, models.CASCADE)
    pay_method = models.CharField(db_column='Pay_method', max_length=30)  # Field name made lowercase.
    pay_amount = models.IntegerField()
    pay_status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'payment'


class Price(models.Model):
    price_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(OrderDetail, models.CASCADE)
    price_weight = models.IntegerField(db_column='Price/weight')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    price_distance = models.IntegerField(db_column='Price/distance')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_price = models.IntegerField(db_column='Total_price')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'price'


class Product(models.Model):
    product_id = models.IntegerField(db_column='Product_id', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(max_length=30)
    weight = models.CharField(max_length=50)
    productprice = models.IntegerField(db_column='ProductPrice')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class Service(models.Model):
    service_id = models.IntegerField(db_column='Service_id', primary_key=True)  # Field name made lowercase.
    service_name = models.CharField(db_column='Service_name', max_length=20)  # Field name made lowercase.
    service_desc = models.CharField(db_column='Service_desc', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service'


class Supplier(models.Model):
    sup_id = models.IntegerField(db_column='Sup_id', primary_key=True)  # Field name made lowercase.
    sup_name = models.CharField(db_column='Sup_name', max_length=20)  # Field name made lowercase.
    contact_no = models.BigIntegerField(db_column='Contact_no')  # Field name made lowercase.
    sup_email = models.CharField(db_column='Sup_email', max_length=30)  # Field name made lowercase.
    sup_address = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'supplier'


class Warehouse(models.Model):
    warehouse_id = models.IntegerField(db_column='Warehouse_id', primary_key=True)  # Field name made lowercase.
    warehouse_address = models.CharField(db_column='Warehouse_address', max_length=100)  # Field name made lowercase.
    capacity = models.CharField(db_column='Capacity', max_length=100)  # Field name made lowercase.
    emp = models.ForeignKey(Employee, models.CASCADE, db_column='Emp_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'warehouse'
  


class Trucks(models.Model):
    truckid = models.AutoField(db_column='TruckID', primary_key=True)  # Field name made lowercase.
    trucktype = models.CharField(db_column='TruckType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lengthft = models.IntegerField(db_column='LengthFT', blank=True, null=True)  # Field name made lowercase.        
    widthft = models.DecimalField(db_column='WidthFT', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    heightft = models.DecimalField(db_column='HeightFT', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    maxloadtons = models.DecimalField(db_column='MaxLoadTons', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trucks'


class Booking(models.Model):
    book_id = models.BigAutoField(db_column='Book_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=254, blank=True, null=True)
    pick_address = models.CharField(max_length=100)
    deliver_address = models.CharField(max_length=100)
    product_detail = models.TextField()
    pay_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'booking'


class Inquiries(models.Model):
    inq_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'inquiries'


class Custfeedback(models.Model):
    fb_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    custfeedback = models.TextField()

    class Meta:
        managed = False
        db_table = 'custfeedback'