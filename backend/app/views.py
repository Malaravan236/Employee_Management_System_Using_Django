from django.shortcuts import render,redirect,get_object_or_404

from .models import Employee
from .forms import Employee_form

# Create
def add_Employee(request):
    if request.method=="POST":
        form=Employee_form(request.POST)
        if(form.is_valid()):
            form.save()
            return render(request,"success.html")
    else:
        form=Employee_form()
    return render(request,"index.html",{'form':form})

# Read
def view_Employee(request):
    emp=Employee.objects.all()
    return render(request,"list.html",{'emp':emp})


# Update
def update_Employee(request,id):
    emp_1=Employee.objects.get(id=id)
    if(request.method=='POST'):
        emp_1.Employee_id=request.POST['Employee_id']
        emp_1.Name=request.POST['Name']
        emp_1.Department=request.POST['Department']
        emp_1.Salary=request.POST['Salary']
        emp_1.Phone=request.POST['Phone']
        emp_1.Email=request.POST['Email']
        emp_1.Address=request.POST['Address']
        emp_1.Joining_date=request.POST['Joining_date']
        emp_1.Status=request.POST['Status']
        emp_1.save()
        return redirect("list")
    return render(request,"Update.html",{"emp_1":emp_1})

# delete
def delete_Employee(request,id):
    emp=get_object_or_404(Employee,id=id)
    emp.delete()
    return redirect('list')

