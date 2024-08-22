import datetime
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render ,redirect ,get_object_or_404 
from cargo4app.models import *
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def dashboard(request):
    return render(request,"admin/dashboard.html",)                                                                                                                                                                                                                                                                           

def emdashboard(request):    
    return render(request,"admin/emdashboard.html")

# 1 ADMIN CRUD
# Create Admin

def admin_create(request):
    if request.method == 'POST':
        admin_id = request.POST.get('admin_id')
        admin_name = request.POST.get('admin_name')
        admin_pass = request.POST.get('admin_pass')
        if admin_id and admin_name and admin_pass:
            Admin.objects.create(
                admin_id=admin_id, 
                admin_name=admin_name, 
                admin_pass=admin_pass)
            return redirect("/adminlist/")
    return render(request, 'admin/admin_create.html')

# Read Admin
def admin_list(request):
    admins = Admin.objects.all()
    if request.method=="GET":
        ad = request.GET.get('searchinput')
        if ad!= None:
            admins = Admin.objects.filter(admin_name__icontains = ad)
        
        
    return render(request, 'admin/admin_list.html', {'admins': admins})

# Update Admin
def admin_update(request, pk):
    admin = get_object_or_404(Admin, admin_id=pk)
    if request.method == 'POST':
        admin_name = request.POST.get('admin_name', admin.admin_name)
        admin_pass = request.POST.get('admin_pass', admin.admin_pass)
        if admin_name and admin_pass:
            admin.admin_name = admin_name
            admin.admin_pass = admin_pass
            admin.save()
            return redirect('/adminlist/')
    return render(request, 'admin/admin_update.html', {'admin': admin})

# Delete Admin
def admin_delete(request, pk):
    admin = get_object_or_404(Admin, admin_id=pk)
    if request.method == 'POST':
        admin.delete()
        return redirect('/adminlist/')
    return render(request, 'admin/admin_delete.html', {'admin': admin})

# 2 CARGO CRUD 
#Read Cargo
def cargo_list(request):
    cargo = Cargo.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            cargo = Cargo.objects.filter(cargo_id__icontains = cr)
        
    return render(request, 'admin/cargo_list.html', {'cargos': cargo})

#Create Cargo
def cargo_create(request):
    if request.method == 'POST':
        cargo_id = request.POST.get('cargo_id')
        cust_id = request.POST.get('cust_id')
        product_id = request.POST.get('product_id')
        emp_id = request.POST.get('emp_id')
        weight = request.POST.get('weight')
        bill_no = request.POST.get('bill_no')
        Cargo.objects.create(
            cargo_id=cargo_id,
            cust_id=cust_id,
            product_id=product_id,
            emp_id=emp_id,
            weight=weight,
            bill_no=bill_no
        )
        return redirect('/cargolist/')
    return render(request, 'admin/cargo_create.html')

#Update Cargo
def cargo_update(request, pk):
    cargo = get_object_or_404(Cargo, cargo_id=pk)
    if request.method == 'POST':
        cargo.cust_id = request.POST.get('cust_id')
        cargo.product_id = request.POST.get('product_id')
        cargo.emp_id = request.POST.get('emp_id')
        cargo.weight = request.POST.get('weight')
        cargo.bill_no = request.POST.get('bill_no')
        cargo.save()
        return redirect('/cargolist/')
    return render(request, 'admin/cargo_update.html', {'cargos': cargo})

#Delete Cargo
def cargo_delete(request, pk):
    cargo = get_object_or_404(Cargo, cargo_id=pk)
    if request.method == 'POST':
        cargo.delete()
        return redirect('/cargolist/')
    return render(request, 'admin/cargo_delete.html', {'cargos': cargo})

# 4 CUSTOMER CRUD
# Read Customer
def customer_list(request):
    customer = Customer.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            customer = Customer.objects.filter(cust_firstname__icontains = cr )
        
    return render(request, 'admin/customer_list.html', {'customers': customer})

# Create Customer
def customer_create(request):
    if request.method == 'POST':
        cust_id = request.POST.get('cust_id')
        cust_firstname = request.POST.get('cust_firstname')
        customer_lastname = request.POST.get('customer_lastname')
        cust_password = request.POST.get('cust_password')
        cust_gender = request.POST.get('cust_gender')
        cust_contact_no_field = request.POST.get('cust_contact_no_field')
        cust_email = request.POST.get('cust_email')
        cust_address = request.POST.get('cust_address')
        Customer.objects.create(
            cust_id=cust_id,
            cust_firstname=cust_firstname,
            customer_lastname=customer_lastname,
            cust_password=cust_password,
            cust_gender=cust_gender,
            cust_contact_no_field=cust_contact_no_field,
            cust_email=cust_email,
            cust_address=cust_address
        )
        return redirect('/customerlist/')
    return render(request, 'admin/customer_create.html')

# Update Customer 
def customer_update(request, id):
    customer = get_object_or_404(Customer, cust_id=id)
    if request.method == 'POST':
        customer.cust_firstname = request.POST.get('cust_firstname')
        customer.customer_lastname = request.POST.get('customer_lastname')
        customer.cust_password = request.POST.get('cust_password')
        customer.cust_gender = request.POST.get('cust_gender')
        customer.cust_contact_no_field = request.POST.get('cust_contact_no_field')
        customer.cust_email = request.POST.get('cust_email')
        customer.cust_address = request.POST.get('cust_address')
        customer.save()
        return redirect('/customerlist/')
    return render(request, 'admin/customer_update.html', {'customer': customer})

# Delete Customer
def customer_delete(request,id):
    customer = get_object_or_404(Customer, cust_id=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('/customerlist/')
    return render(request, 'admin/customer_delete.html', {'customer': customer})

# 5 DELIVERY CRUD
# Read Delivery
def delivery_list(request):
    delivery = Delivery.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            delivery = Delivery.objects.filter(delivery_id__icontains = cr )
        
    return render(request, 'admin/delivery_list.html', {'deliveries': delivery})

# Create Delivery 
def delivery_create(request):
    if request.method == 'POST':
        delivery_id = request.POST.get('delivery_id')
        cargo_id = request.POST.get('cargo_id')
        pickup_date = request.POST.get('pickup_date')
        delivery_date = request.POST.get('delivery_date')
        pickup_address = request.POST.get('pickup_address')
        destination_address = request.POST.get('destination_address')
        Delivery.objects.create(
            delivery_id=delivery_id,
            cargo_id=cargo_id,
            pickup_date=pickup_date,
            delivery_date=delivery_date,
            pickup_address=pickup_address,
            destination_address=destination_address
        )
        return redirect('/deliverylist/')
    return render(request, 'admin/delivery_create.html')

# Update Delivery 
def delivery_update(request, id):
    delivery = get_object_or_404(Delivery, delivery_id=id)
    if request.method == 'POST':
        delivery.cargo_id = request.POST.get('cargo_id')
        delivery.pickup_date = request.POST.get('pickup_date')
        delivery.delivery_date = request.POST.get('delivery_date')
        delivery.pickup_address = request.POST.get('pickup_address')
        delivery.destination_address = request.POST.get('destination_address')
        delivery.save()
        return redirect('/deliverylist/')
    return render(request, 'admin/delivery_update.html', { 'delivery': delivery})

# Delete Delivery 
def delivery_delete(request, id):
    delivery = get_object_or_404(Delivery, delivery_id=id)
    if request.method == 'POST':
        delivery.delete()
        return redirect('/deliverylist/')
    return render(request, 'admin/delivery_delete.html', {'delivery': delivery})

# 5 DESIGNATION CRUD
# Read Designation
def designation_list(request):
    designation = Designation.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            designation = Designation.objects.filter(designation__icontains = cr )
        
    return render(request, 'admin/designation_list.html', {'designations': designation})

# Create Designation
def designation_create(request):
    if request.method == 'POST':
        designation_id = int(request.POST.get('designation_id'))
        designation = request.POST.get('designation')
        qualification = request.POST.get('qualification')

        Designation.objects.create(
            designation_id=designation_id, 
            designation=designation, 
            qualification=qualification
        )
        return redirect('/designationlist/')

    return render(request, 'admin/designation_create.html')

# Update Designation
def designation_update(request, id):
    designation = get_object_or_404(Designation, designation_id = id)

    if request.method == 'POST':
        designation.designation = request.POST.get('designation')
        designation.qualification = request.POST.get('qualification')
        designation.save()
        return redirect('/designationlist/')

    return render(request, 'admin/designation_update.html', {'designation': designation })

# Delete Designation
def designation_delete(request, id):
    designation = get_object_or_404(Designation, designation_id = id)

    if request.method == 'POST':
        designation.delete()
        return redirect('/designationlist/')

    return render(request, 'admin/designation_delete.html', {'designation': designation})

# 7 EMPLOYEE CRUD
# Read employees
def employee_list(request):
    employee = Employee.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            employee = Employee.objects.filter(emp_firstname__icontains = cr )
        
    return render(request, 'admin/employee_list.html', {'employees': employee})

# Create Employee
def employee_create(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        emp_firstname = request.POST.get('emp_firstname')
        emp_lastname = request.POST.get('emp_lastname')
        emp_password = request.POST.get('emp_password')
        designation_id = int(request.POST.get('designation_id'))
        experience = request.POST.get('experience')
        emp_salary = int(request.POST.get('emp_salary'))
        gender = request.POST.get('gender')
        emp_dob = request.POST.get('emp_dob')
        emp_doj = request.POST.get('emp_doj')
        emp_contact_no = int(request.POST.get('emp_contact_no'))
        emp_email = request.POST.get('emp_email')
        emp_address = request.POST.get('emp_address')
        working_days = request.POST.get('working_days')
        leave_days = request.POST.get('leave_days')

        Employee.objects.create(
            emp_id=emp_id, 
            emp_firstname=emp_firstname, 
            emp_lastname=emp_lastname, 
            emp_password=emp_password,
            designation_id=designation_id, 
            experience=experience, 
            emp_salary=emp_salary, 
            gender=gender,
            emp_dob=emp_dob, 
            emp_doj=emp_doj, 
            emp_contact_no=emp_contact_no, 
            emp_email=emp_email,
            emp_address=emp_address, 
            working_days=working_days, 
            leave_days=leave_days
        )
        return redirect('/employeelist/')

    return render(request, 'admin/employee_create.html')

# Update Eemployee
def employee_update(request, id):
    employee = get_object_or_404(Employee, emp_id=id)

    if request.method == 'POST':
        employee.emp_id = request.POST.get('emp_id')
        employee.emp_firstname = request.POST.get('emp_firstname')
        employee.emp_lastname = request.POST.get('emp_lastname')
        employee.emp_password = request.POST.get('emp_password')
        employee.designation_id = int(request.POST.get('designation_id'))
        employee.experience = request.POST.get('experience')
        employee.emp_salary = int(request.POST.get('emp_salary'))
        employee.gender = request.POST.get('gender')
        employee.emp_dob = request.POST.get('emp_dob')
        employee.emp_doj = request.POST.get('emp_doj')
        employee.emp_contact_no = int(request.POST.get('emp_contact_no'))
        employee.emp_email = request.POST.get('emp_email')
        employee.emp_address = request.POST.get('emp_address')
        employee.working_days = request.POST.get('working_days')
        employee.leave_days = request.POST.get('leave_days')
        employee.save()
        return redirect('/employeelist/')

    return render(request, 'admin/employee_update.html', {'employee': employee })

# Delete Employee
def employee_delete(request, id):
    employee = get_object_or_404(Employee, emp_id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('/employeelist/')

    return render(request, 'admin/employee_delete.html', {'employee': employee})

# 8 FEEDBACK CRUD
# Read Feedback
def feedback_list(request):
    feedback = Feedback.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            feedback = Feedback.objects.filter(f_id__icontains = cr )
        
    return render(request, 'admin/feedback_list.html', {'feedbacks': feedback})

# Create Feedback 
def feedback_create(request):
    if request.method == 'POST':
        f_id = int(request.POST.get('f_id'))
        feedback = request.POST.get('feedback')
        f_date = request.POST.get('f_date')
        cust_id = int(request.POST.get('cust_id'))

        Feedback.objects.create(
            f_id=f_id, 
            feedback=feedback, 
            f_date=f_date, 
            cust_id=cust_id
        )
        return redirect('/feedbacklist/')

    return render(request, 'admin/feedback_create.html')

# Update Feedback
def feedback_update(request, id):
    feedback = get_object_or_404(Feedback, f_id = id)

    if request.method == 'POST':
        feedback.feedback = request.POST.get('feedback')
        feedback.f_date = request.POST.get('f_date')
        feedback.cust_id = int(request.POST.get('cust_id'))
        feedback.save()
        return redirect('/feedbacklist/')

    return render(request, 'admin/feedback_update.html', {'feedback': feedback })

# Delete Feedback 
def feedback_delete(request, id):
    feedback = get_object_or_404(Feedback, f_id = id)

    if request.method == 'POST':
        feedback.delete()
        return redirect('/feedbacklist/')

    return render(request, 'admin/feedback_delete.html', {'feedback': feedback})

# 9 INVENTORY CRUD
# Read Inventory
def inventory_list(request):
    inventory = Inventory.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            inventory = Inventory.objects.filter(inventory_id__icontains = cr )
        
    return render(request, 'admin/inventory_list.html', {'inventories': inventory})

# Create Inventory 
def inventory_create(request):
    if request.method == 'POST':
        inventory_id = int(request.POST.get('inventory_id'))
        product_id = int(request.POST.get('product_id'))
        arrival_date = request.POST.get('arrival_date')
        departure_date = request.POST.get('departure_date')

        Inventory.objects.create(
            inventory_id=inventory_id, 
            product_id=product_id, 
            arrival_date=arrival_date, 
            departure_date=departure_date
        )
        return redirect('/inventorylist/')

    return render(request, 'admin/inventory_create.html')

# Update Inventory
def inventory_update(request, id):
    inventory = get_object_or_404(Inventory, inventory_id= id)

    if request.method == 'POST':
        inventory.product_id = int(request.POST.get('product_id'))
        inventory.arrival_date = request.POST.get('arrival_date')
        inventory.departure_date = request.POST.get('departure_date')
        inventory.save()
        return redirect('/inventorylist/')

    return render(request, 'admin/inventory_update.html', {'inventory': inventory })

# Delete Inventory
def inventory_delete(request, id):
    inventory = get_object_or_404(Inventory, inventory_id = id)

    if request.method == 'POST':
        inventory.delete()
        return redirect('/inventorylist/')

    return render(request, 'admin/inventory_delete.html', {'inventory': inventory})
 
# 11 Material CRUD
# Read Material 
def materials_list(request):
    material = Materials.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            material = Materials.objects.filter(material_name__icontains = cr )
        
    return render(request, 'admin/materials_list.html', {'materials': material})

# Create Material
def material_create(request):
    if request.method == 'POST':
        material_id = request.POST.get('material_id')
        material_name = request.POST.get('material_name')
        material_type = request.POST.get('material_type')
        quantity = request.POST.get('quantity')
        sup_id = request.POST.get('sup_id')
        materialprice = request.POST.get('materialprice')
        
        material = Materials(
            material_id=material_id, 
            material_name=material_name,
            material_type=material_type, 
            quantity=quantity,
            sup_id=sup_id, 
            materialprice=materialprice)
        material.save()
        return redirect('/materialslist/')
    else:
        return render(request, 'admin/material_create.html')
    
# Update Material
def material_update(request, id):
    material = get_object_or_404(Materials,  material_id = id)
    
    if request.method == 'POST':
        material.material_name = request.POST.get('material_name')
        material.material_type = request.POST.get('material_type')
        material.quantity = request.POST.get('quantity')
        material.sup_id = request.POST.get('sup_id')
        material.materialprice = request.POST.get('materialprice')
        
        material.save()
        return redirect('/materialslist/')
    else:
        return render(request, 'admin/material_update.html', {'material': material})

# Material Delete
def material_delete(request, id):
    material = get_object_or_404(Materials, material_id= id)
    
    if request.method == 'POST':
        material.delete()
        return redirect('/materiallist/')  # Redirect to material list page after deletion
    
    return render(request, 'admin/material_delete.html', {'material': material})

#  12 Order_Detail CRUD
# Read Order
def order_list(request):
    order = OrderDetail.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            order = OrderDetail.objects.filter(order_id__icontains = cr )
        
    return render(request, 'admin/order_list.html', {'orders': order})

# Create Order 
def order_create(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order_date = request.POST.get('order_date') #date()
        pay_method = request.POST.get('pay_method')
        cust_id = request.POST.get('cust_id')
        product_id = request.POST.get('product_id')
        service_id = request.POST.get('service_id')
        
        order_detail = OrderDetail(
            order_id = order_id,
            order_date=order_date, 
            pay_method=pay_method,
            cust_id=cust_id, 
            product_id=product_id, 
            service_id=service_id)
        order_detail.save()
        return redirect('/orderlist/')
    else:
        return render(request, 'admin/order_create.html')

# Update Order
def order_update(request, id):
    order = OrderDetail.objects.get(order_id= id)
    
    if request.method == 'POST':
        order.order_date = request.POST.get('order_date')#.date()
        order.pay_method = request.POST.get('pay_method')
        order.cust = request.POST.get('cust_id')
        order.product = request.POST.get('product_id')
        order.service = request.POST.get('service_id')
        order.save()
        return redirect('/orderlist/')
    else:
        return render(request, 'admin/order_update.html', {'order': order})

# Delete Order
def order_delete(request, id):
    order = OrderDetail.objects.get(order_id= id)
    if request.method == 'POST':
        order.delete()
        return redirect('/orderlist/')
    else:
        return render(request, 'admin/order_delete.html', {'order': order})

# 15 Product CRUD
# Read Product
def product_list(request):
    product = Product.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            product = Product.objects.filter(product_name__icontains = cr )
    return render(request, 'admin/product_list.html', { 'products': product })

# Create Product
def product_create(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        weight = request.POST.get('weight')
        productprice = request.POST.get('productprice')
        
        Product.objects.create(
            product_id=product_id, 
            product_name=product_name,
            weight=weight, 
            productprice=productprice)
        return redirect('/productlist/')
    return render(request, 'admin/product_create.html')

# Update Product
def product_update(request, id):
    product = get_object_or_404(Product, product_id= id)
    if request.method == 'POST':
        product.product_name = request.POST.get('product_name')
        product.weight = request.POST.get('weight')
        product.productprice = request.POST.get('productprice')
        product.save()
        return redirect('/productlist/')
    return render(request, 'admin/product_update.html', {'product': product})

# Delete Product
def product_delete(request, id):
    product = get_object_or_404(Product, product_id= id)
    if request.method == 'POST':
        product.delete()
        return redirect('/productlist/')
    return render(request, 'admin/product_delete.html', {'product': product})

# 16 Service CRUD
# Read Service
def service_list(request):
    service = Service.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            service = Service.objects.filter(service_name__icontains = cr )
        
    return render(request, 'admin/service_list.html', {'services': service})

# Create Service
def service_create(request):
    if request.method == 'POST':
        service_id = request.POST.get('service_id')
        service_name = request.POST.get('service_name')
        service_desc = request.POST.get('service_desc')
        
        Service.objects.create(
            service_id=service_id, 
            service_name=service_name,
            service_desc=service_desc)
        return redirect('/servicelist/')
    return render(request, 'admin/service_create.html')

# Read Service
def service_update(request, id):
    service = get_object_or_404(Service, service_id = id)
    if request.method == 'POST':
        service.service_name = request.POST.get('service_name')
        service.service_desc = request.POST.get('service_desc')
        service.save()
        return redirect('/servicelist/')
    return render(request, 'admin/service_update.html', {'service': service})

# Read Service
def service_delete(request, id):
    service = get_object_or_404(Service, service_id = id)
    if request.method == 'POST':
        service.delete()
        return redirect('/servicelist/')
    return render(request, 'admin/service_delete.html', {'service': service})

# 17 Supplier CRUD
# Read Supplier
def supplier_list(request):
    supplier = Supplier.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            supplier = Supplier.objects.filter(sup_name__icontains = cr )
    return render(request, 'admin/supplier_list.html', {'suppliers': supplier})

# Create Supplier
def supplier_create(request):
    if request.method == 'POST':
        sup_id = request.POST.get('sup_id')
        sup_name = request.POST.get('sup_name')
        contact_no = request.POST.get('contact_no')
        sup_email = request.POST.get('sup_email')
        sup_address = request.POST.get('sup_address')
        Supplier.objects.create(
            sup_id=sup_id,
            sup_name=sup_name, 
            contact_no=contact_no, 
            sup_email=sup_email, 
            sup_address=sup_address)
        return redirect('/supplierlist/')
    return render(request, 'admin/supplier_create.html')

# Update Supplier
def supplier_update(request, id):
    supplier = get_object_or_404(Supplier, sup_id= id)
    if request.method == 'POST':
        supplier.sup_name = request.POST.get('sup_name')
        supplier.contact_no = request.POST.get('contact_no')
        supplier.sup_email = request.POST.get('sup_email')
        supplier.sup_address = request.POST.get('sup_address')
        supplier.save()
        return redirect('/supplierlist/')
    return render(request, 'admin/supplier_update.html', {'supplier': supplier})

# Delete Supplier
def supplier_delete(request, id):
    supplier = get_object_or_404(Supplier, sup_id= id)
    if request.method == 'POST':
        supplier.delete()
        return redirect('/supplierlist/')
    return render(request, 'admin/supplier_delete.html', {'supplier': supplier})

# 18 Warehouse CRUD
# Read Warehouse
def warehouse_list(request):
    warehouse = Warehouse.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            warehouse = Warehouse.objects.filter(warehouse_id__icontains = cr )
    return render(request, 'admin/warehouse_list.html', {'warehouses': warehouse})

# Create Warehouse
def warehouse_create(request):
    if request.method == 'POST':
        warehouse_id = request.POST.get('warehouse_id')
        warehouse_address = request.POST.get('warehouse_address')
        capacity = request.POST.get('capacity')
        emp_id = request.POST.get('emp_id') 

        warehouse = Warehouse(
            warehouse_id=warehouse_id,
            warehouse_address=warehouse_address,
            capacity=capacity,
            emp_id=emp_id
        )
        warehouse.save()
        return redirect('/warehouselist/')  # Redirect to the list view after creating

    return render(request, 'admin/warehouse_create.html')

# Update Warehouse
def warehouse_update(request, id):
    warehouse = get_object_or_404(Warehouse, warehouse_id = id)

    if request.method == 'POST':
        warehouse.warehouse_address = request.POST.get('warehouse_address')
        warehouse.capacity = request.POST.get('capacity')
        warehouse.emp_id = request.POST.get('emp_id')
        warehouse.save()
        return redirect('/warehouselist/')  # Redirect to the list view after updating

    return render(request, 'admin/warehouse_update.html', {'warehouse': warehouse})

# Delete Warehouse
def warehouse_delete(request, id ):
    warehouse = get_object_or_404(Warehouse, warehouse_id= id )
    if request.method == 'POST':
        warehouse.delete()
        return redirect('/warehouselist/')
    return render(request, 'admin/warehouse_delete.html', {'warehouse': warehouse})

# 3 CARGO_WEIGHT CRUD
# Read Cargo_weight
def cargo_weight_list(request):
    cargo_weight = CargoWeight.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            cargo_weight = CargoWeight.objects.filter(weight__icontains = cr )
    return render(request, 'admin/cargo_weight_list.html', {'cargo_weights': cargo_weight})

# Create Cargo_weight ( not working )
def cargo_weight_create(request):
    if request.method == 'POST':
        weight_id = request.POST.get('weight_id')
        weight = request.POST.get('weight')
        measurement_unit = request.POST.get('measurement_unit')
        cargo_id = request.POST.get('cargo_id')  # assuming cargo_id is provided in the form
        product_id = request.POST.get('product_id')  # assuming product_id is provided in the form
        cargo_weight = CargoWeight(
            weight_id=weight_id, 
            weight=weight, 
            measurement_unit=measurement_unit,                           
            cargo_id=cargo_id, 
            product_id=product_id)
        cargo_weight.save()
        return redirect('/cargoweightlist/')
    else:
        return render(request, 'admin/cargo_weight_create.html')

# Update Cargo_weight
def cargo_weight_update(request, id):
    cargo_weight = CargoWeight.objects.get(weight_id= id)
    if request.method == 'POST':
        cargo_weight.weight = request.POST.get('weight')
        cargo_weight.measurement_unit = request.POST.get('measurement_unit')
        cargo_weight.cargo_id = request.POST.get('cargo_id')  # assuming cargo_id is provided in the form
        cargo_weight.product_id = request.POST.get('product_id')  # assuming product_id is provided in the form
        cargo_weight.save()
        return redirect('/cargoweightlist/')
    else:
        return render(request, 'admin/cargo_weight_update.html', {'cargo_weight': cargo_weight})

# Delete Cargo_weight
def cargo_weight_delete(request, id):
    cargo_weight = get_object_or_404(CargoWeight, weight_id = id)
    if request.method == 'POST':
        cargo_weight.delete()
        return redirect('/cargoweightlist/')
    
    return render(request, 'admin/cargo_weight_delete.html', {'cargo_weight': cargo_weight})
        
# 10 INVOICE CRUD
# Read Invoices 
def invoice_list(request):
    invoice = Invoice.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            invoice = Invoice.objects.filter(invoice_id__icontains = cr )
    return render(request, 'admin/invoice_list.html', {'invoices': invoice})

def invoice_create(request):
    if request.method == 'POST':
        invoice_id = request.POST.get('invoice_id')
        order_id = request.POST.get('order_id')
        due_date = request.POST.get('due_date')
        price_id = request.POST.get('price_id')

        # Ensure all fields are provided
        if not invoice_id or not order_id or not due_date or not price_id:
            return HttpResponse("All fields are required", status=400)

        try:
            # Parse the due date
            due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
        except ValueError:
            return HttpResponse("Invalid date format", status=400)

        # Fetch the related OrderDetail and Price objects
        try:
            order = OrderDetail.objects.get(pk=order_id)
            price = Price.objects.get(pk=price_id)
        except (OrderDetail.DoesNotExist, Price.DoesNotExist):
            return HttpResponse("Invalid order or price ID", status=400)

        # Create the Invoice object
        try:
            invoice = Invoice.objects.create(
                invoice_id=invoice_id,
                order=order,
                due_date=due_date,
                price=price
            )
            return redirect('/invoicelist/')
        except IntegrityError as e:
            return render(request, 'admin/invoice_create.html', {
                'error': f'Failed to create invoice: {e}',
                'invoice_id': invoice_id,
                'order_id': order_id,
                'due_date': due_date,
                'price_id': price_id,
            })

    return render(request, 'admin/invoice_create.html')

# Update Invoice
def invoice_update(request, id):
    invoice = get_object_or_404(Invoice, invoice_id = id )
    if request.method == 'POST':
        invoice.invoice_id = request.POST.get('invoice_id')
        invoice.order = request.POST.get('order_id')
        invoice.due_date = request.POST.get('due_date')
        invoice.price = request.POST.get('price_id')
        invoice.save()
        return redirect('/invoicelist/')
    else:
        return render(request, 'admin/invoice_update.html', {'invoice': invoice})

# Delete Invoice
def invoice_delete(request, id):
    invoice = get_object_or_404(Invoice, invoice_id = id)
    if request.method == 'POST':
        invoice.delete()
        return redirect('/invoicelist/')
    else:
        return render(request, 'admin/invoice_delete.html', {'invoice': invoice})
  
# 13 Payment CRUD
# Read Payment
def payment_list(request):
    payment = Payment.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            payment = Payment.objects.filter(pay_amount__icontains = cr )
    return render(request, 'admin/payment_list.html', {'payments': payment})

# Create Payment
def payment_create(request):
    if request.method == 'POST':
        pay_id = request.POST.get('pay_id')
        pay_date = request.POST.get('pay_date')#.date()
        price_id = request.POST.get('price_id')
        order_id = request.POST.get('order_id')
        cust_id = request.POST.get('cust_id')
        pay_method = request.POST.get('pay_method')
        pay_amount = request.POST.get('pay_amount')
        pay_status = request.POST.get('pay_status')
        payment = Payment.objects.create(
            pay_id = pay_id,
            pay_date=pay_date, 
            price_id=price_id, 
            order_id=order_id,
            cust_id=cust_id, 
            pay_method=pay_method,          
            pay_amount=pay_amount, 
            pay_status=pay_status)
        payment.save()
        return redirect('/paymentlist/')
    else:
        return render(request, 'admin/payment_create.html')

# Update Payment
def payment_update(request, id):
    payment = Payment.objects.get(pay_id= id)
    if request.method == 'POST':
        payment.pay_date = request.POST.get('pay_date')#.date()
        payment.price_id = request.POST.get('price_id')
        payment.order_id = request.POST.get('order_id')
        payment.cust_id = request.POST.get('cust_id')
        payment.pay_method = request.POST.get('pay_method')
        payment.pay_amount = request.POST.get('pay_amount')
        payment.pay_status = request.POST.get('pay_status')
        payment.save()
        return redirect('/paymentlist/')
    else:
        return render(request, 'admin/payment_update.html', {'payment': payment})

# Delete Payment
def payment_delete(request, id):
    payment = Payment.objects.get(pay_id= id)
    if request.method == 'POST':
        payment.delete()
        return redirect('/paymentlist/')
    else:
        return render(request, 'admin/payment_delete.html', {'payment': payment})

# 14 Price CRUD
# Read Price
def price_list(request):
    price = Price.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            price = Price.objects.filter(price_id__icontains = cr )
    return render(request, 'admin/price_list.html', {'prices': price})

# Create Price
def price_create(request):
    if request.method == 'POST':
        
        price_id = request.POST.get('price_id')
        order_id = request.POST.get('order_id')
        price_weight = request.POST.get('price_weight')
        price_distance = request.POST.get('price_distance')
        total_price = request.POST.get('total_price')
        
         # Ensure all fields are provided
        if not price_id or not order_id or not price_weight or not price_distance or not total_price:
            return HttpResponse("All fields are required", status=400)
        
        # Ensure the OrderDetail exists
        try:
            order = OrderDetail.objects.get(pk=order_id)
        
        except OrderDetail.DoesNotExist:
            return HttpResponse("Invalid order ID", status=400)

        try:
            price = Price.objects.create(
                price_id=price_id,
                order = order, 
                price_weight=price_weight, 
                price_distance=price_distance, 
                total_price=total_price)
            price.save()
            return redirect('/pricelist/')
    
    
    
        except IntegrityError as e:
            return render(request, 'admin/price_form.html', {
                'error': f'Failed to create price: {e}',
                'price_id': price_id,
                'order_id': order_id,
                'price_weight': price_weight,
                'price_distance': price_distance,
                'total_price': total_price,
            })
    else:
        return render(request, 'admin/price_create.html')

# Update Price
def price_update(request, id):
    # order = OrderDetail.objects.all()
    price = Price.objects.get(price_id = id)
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        price_weight = request.POST.get('price_weight')
        price_distance = request.POST.get('price_distance')
        total_price = request.POST.get('total_price')
       
        # Ensure all fields are provided
        if not order_id or not price_weight or not price_distance or not total_price:
            return HttpResponse("All fields are required", status=400)

        # Ensure the OrderDetail exists
        try:
            order = OrderDetail.objects.get(pk=order_id)
        except OrderDetail.DoesNotExist:
            return HttpResponse("Invalid order ID", status=400)
       
         # Update the Price object
        try:
            price.order = order
            price.price_weight = price_weight
            price.price_distance = price_distance
            price.total_price = total_price
            price.save()
            return redirect('/pricelist/')
        except IntegrityError as e:
            return render(request, 'admin/price_update.html', {'error': f'Failed to update price: {e}','price': price})
        
    else:
        return render(request, 'admin/price_update.html', {'price': price})

# Read Price
def price_delete(request, id):
    price = Price.objects.get(price_id = id)
    if request.method == 'POST':
        price.delete()
        return redirect('/pricelist/')
    return render(request, 'admin/price_delete.html', {'price': price})
 
# 19 TRUCK CRUD
# Read Truck
def truck_list(request):
    truck = Trucks.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            truck = Trucks.objects.filter(trucktype__icontains = cr )
    return render(request, 'admin/truck_list.html', {'trucks': truck})

# Create Truck
def create_truck(request):
    if request.method == 'POST':
        truckid = request.POST.get('truckid')
        trucktype = request.POST.get('trucktype')
        lengthft = request.POST.get('lengthft')
        widthft = request.POST.get('widthft')
        heightft = request.POST.get('heightft')
        maxloadtons = request.POST.get('maxloadtons')
        
        Trucks.objects.create(
            truckid=truckid,
            trucktype=trucktype,
            lengthft=lengthft,
            widthft=widthft,
            heightft=heightft,
            maxloadtons=maxloadtons,
 
        )
        return redirect('/trucklist/')  

    return render(request, 'admin/truck_create.html')

# Update Truck
def update_truck(request, id):
    truck = get_object_or_404(Trucks, truckid=id)
    
    if request.method == 'POST':
        truck.trucktype = request.POST.get('trucktype')
        truck.lengthft = request.POST.get('lengthft')
        truck.widthft = request.POST.get('widthft')
        truck.heightft = request.POST.get('heightft')
        truck.maxloadtons = request.POST.get('maxloadtons')
        truck.image = request.POST.get('image')
        truck.save()
        return redirect('/trucklist/')

    return render(request, 'admin/truck_update.html', {'truck': truck})

# Delete Truck
def delete_truck(request, id):
    truck = get_object_or_404(Trucks, truckid = id)
    if request.method == 'POST':
        truck.delete()
        return redirect('/trucklist/')

    return render(request, 'admin/truck_delete.html', {'truck': truck})

# 20 INQUIRY CRUD
# Read Inquiry
def inquiry_list(request):
    inquiry = Inquiries.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            inquiry = Inquiries.objects.filter(inq_id__icontains = cr )
    return render(request, 'admin/inquiry_list.html', {'inquiries': inquiry})

# Create Inquiry
def create_inquiry(request):
    if request.method == 'POST':
       
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        Inquiries.objects.create(
            
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        return redirect('/inquirylist/')

    return render(request, 'admin/inquiry_create.html')

# Update Inquiry
def update_inquiry(request, id):
    inquiry = get_object_or_404(Inquiries, inq_id=id)
    
    if request.method == 'POST':
        inquiry.name = request.POST.get('name')
        inquiry.email = request.POST.get('email')
        inquiry.phone = request.POST.get('phone')
        inquiry.message = request.POST.get('message')
        inquiry.save()
        return redirect('/inquirylist/')

    return render(request, 'admin/inquiry_update.html', {'inquiry': inquiry})

# Delete Inquiry
def delete_inquiry(request, id):
    inquiry = get_object_or_404(Inquiries, inq_id=id)
    if request.method == 'POST':
        inquiry.delete()
        return redirect('/inquirylist/')

    return render(request, 'admin/inquiry_delete.html', {'inquiry': inquiry})

# 21 BOOKING CRUD
# Read Booking
def booking_list(request):
    bookings = Booking.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            bookings = Booking.objects.filter(book_id__icontains = cr )
    return render(request, 'admin/booking_list.html', {'bookings': bookings})

# Create Booking
def create_booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        pick_address = request.POST.get('pick_address')
        deliver_address = request.POST.get('deliver_address')
        product_detail = request.POST.get('product_detail')
        pay_type = request.POST.get('pay_type')
        
        Booking.objects.create(
            name=name,
            lname=lname,
            mobile=mobile,
            email=email,
            pick_address=pick_address,
            deliver_address=deliver_address,
            product_detail=product_detail,
            pay_type=pay_type
        )
        return redirect('/bookinglist/')  # Redirect to a list view after creation

    return render(request, 'admin/booking_create.html')

# Update Booking
def update_booking(request, id):
    booking = get_object_or_404(Booking, book_id=id)
    
    if request.method == 'POST':
        booking.name = request.POST.get('name')
        booking.lname = request.POST.get('lname')
        booking.mobile = request.POST.get('mobile')
        booking.email = request.POST.get('email')
        booking.pick_address = request.POST.get('pick_address')
        booking.deliver_address = request.POST.get('deliver_address')
        booking.product_detail = request.POST.get('product_detail')
        booking.pay_type = request.POST.get('pay_type')
        booking.save()
        return redirect('booking_detail', book_id=booking.book_id)

    return render(request, 'admin/booking_update.html', {'booking': booking})

# Delete Booking
def delete_booking(request, id):
    booking = get_object_or_404(Booking, book_id= id)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')

    return render(request, 'admin/booking_delete.html', {'booking': booking})

# 22 CUSTFEEDBACK CRUD 
# Read Feedback
def cust_fb_list(request):
    feedback = Custfeedback.objects.all()
    if request.method=="GET":
        cr = request.GET.get('searchinput')
        if cr!= None:
            feedback = Custfeedback.objects.filter(fb_id__icontains = cr )
    return render(request, 'admin/newfeedback_list.html', {'feedbacks': feedback} )

# create Feedback
def newfb_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        custfeedback = request.POST.get('custfeedback')

        Custfeedback.objects.create(
            name=name,
            email=email,
            custfeedback=custfeedback
        )
        return redirect('/fblist/') 

    return render(request, 'admin/newfb_create.html')

# Update Feedback

def newfb_update(request, id):
    feedback = get_object_or_404(Custfeedback, fb_id=id)

    if request.method == 'POST':
        feedback.name = request.POST.get('name')
        feedback.email = request.POST.get('email')
        feedback.custfeedback = request.POST.get('custfeedback')
        feedback.save()
        return redirect('/fblist/')

    return render(request, 'admin/newfb_update.html', {'feedback': feedback})

# Delete Feedback
def newfb_delete(request, id):
    feedback = get_object_or_404(Custfeedback, fb_id=id)
    if request.method == 'POST':
        feedback.delete()
        return redirect('/fblist/')

    return render(request, 'admin/newfb_delete.html', {'feedback': feedback})

#USERs 
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Validate input
        if not username and not password:
            messages.error(request, 'Both fields are required.')
        elif not username:
            messages.error(request,'Username is required,')
        elif not password:
            messages.error(request,'Password is required,')
        else:
            try:
                admin = Admin.objects.get(admin_name=username, admin_pass=password)
                request.session['admin_id'] = admin.admin_id
                return redirect('../dashboard/')
            except Admin.DoesNotExist:
                messages.error(request, 'Invalid username or password.')
                
    return render(request, 'user/adminlogin.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        address = request.POST.get('address')

        # Basic validation
        if not all([first_name, last_name, password, gender, contact_no, email, address]):
            messages.error(request, 'All fields are required.')
        else:
            if Customer.objects.filter(cust_email=email).exists():
                messages.error(request, 'Email is already registered.')
            else:
                hashed_password = make_password(password)
                Customer.objects.create(
                    cust_firstname=first_name,
                    customer_lastname=last_name,
                    cust_password=hashed_password,
                    cust_gender=gender,
                    cust_contact_no_field=contact_no,
                    cust_email=email,
                    cust_address=address
                )
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('cust_login')
    return render(request, 'user/custregister.html')

def cust_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email and not password:
            messages.error(request, 'Both fields are required.')
        elif not email:
            messages.error(request,'email is required,')
        elif not password:
            messages.error(request,'Password is required,')
        else:
            try:
                customer = Customer.objects.get(cust_email=email)
                request.session['cust_email'] = customer.cust_email
                return redirect('../')
            except Customer.DoesNotExist:
                messages.error(request, 'Email not registered.')
                
    return render(request, 'user/custlogin.html')

def emp_register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        designation_id = request.POST.get('designation_id')
        gender = request.POST.get('gender')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        
        # Basic validation
        if not all([first_name, last_name, password,  designation_id, gender,  contact_no, email, ]):
            messages.error(request, 'All fields are required.')
        else:
            if Employee.objects.filter(emp_email=email).exists():
                messages.error(request, 'Email is already registered.')
            else:
                hashed_password = make_password(password)
                Employee.objects.create(
                    emp_firstname=first_name,
                    emp_lastname=last_name,
                    emp_password=hashed_password,
                     designation_id=designation_id,
                    gender=gender,
                    emp_contact_no=contact_no,
                    emp_email=email,
                )
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('emp_login')
    return render(request, 'user/empregister.html')

def emp_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email and not password:
            messages.error(request, 'Both fields are required.')
        elif not email:
            messages.error(request,'email is required,')
        elif not password:
            messages.error(request,'Password is required,')
        else:
            try:
                employee = Employee.objects.get(emp_email=email)
                request.session['employee_email'] = employee.emp_email
                return redirect('/emdashboard/')
            except Employee.DoesNotExist:
                messages.error(request, 'Email not registered.')
                
    return render(request, 'user/emplogin.html')

# customer side
def booking_view(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email', '')
        pick_address = request.POST.get('pick_address')
        deliver_address = request.POST.get('deliver_address')
        product_detail = request.POST.get('product_detail')
        pay_type = request.POST.get('pay_type')
        
        # Create and save a new Booking instance
        booking = Booking(
            name=name,
            lname=lname,
            mobile=mobile,
            email=email,
            pick_address=pick_address,
            deliver_address=deliver_address,
            product_detail=product_detail,
            pay_type=pay_type
        )
        booking.save()
        
        # # Redirect to a success page or another page
        # return HttpResponse("Booking submitted successfully!")
    
    return render(request, 'customer/booking.html')

def success(request):
    return render(request,'customer/success.html')

def generate_invoice(request, booking_id):
    booking = get_object_or_404(Booking, book_id=booking_id)
    
    order = OrderDetail.objects.filter(order_id=booking_id).first()
    price = Price.objects.filter(order=order).first()
    payment = Payment.objects.filter(order=order)
    
    context = {
        'booking': booking,
        'order': order,
        'price': price,
        'payment': payment,
    }
    
    # Render the invoice template
    return render(request, 'customer/invoice.html', context)

def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        custfeedback = request.POST.get('custfeedback')
        
        Custfeedback.objects.create(
            name=name, 
            email=email, 
            custfeedback=custfeedback)
    return render(request, 'customer/feedback.html')

def inquiry_view(request):
    if request.method == 'POST':
        # Retrieve data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Create and save a new Inquiry instance
        inquiry = Inquiries(name=name, email=email, phone=phone, message=message)
        inquiry.save()

    
    return render(request, 'customer/inquiry_form.html')

def dsbrd(request):
    return render(request, 'admin/dsbrd.html')




