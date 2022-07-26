from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Employee, Fav, ReqEmployee
from .serializers import EmployeesSerializer, FavSerializer, ReqEmployeeSerializer
from user.models import Profile


# Add New Employee 
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_emp(request: Request, profile_id):

    ''' 
        This function is to add a new employee.
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    profile = Profile.objects.get(id=profile_id)
    request.data.update(user=request.user.id, profile=profile.id)
    new_employee = EmployeesSerializer(data=request.data)
    if new_employee.is_valid():
        new_employee.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "employee" : new_employee.data
        }
        return Response(dataResponse)
    else:
        print(new_employee.errors)
        dataResponse = {"msg" : "couldn't create an employee!"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

# Get All Employees
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_emp(request : Request):
    ''' 
        This function is to view all employees.
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    emps = Employee.objects.all()
    dataResponse = {
        "msg" : "List of all employees",
        "employees" : EmployeesSerializer(instance=emps, many=True).data
        }
    return Response(dataResponse)

# Get Company ID Employees
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_comp_emp(request : Request):
    '''list the company's employees'''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    emps = Employee.objects.filter(user=user.id)
    dataResponse = {
        "msg" : "List of All company employees",
        "employees" : EmployeesSerializer(instance=emps, many=True).data
        }
    return Response(dataResponse)

# Update ID Employee
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def edit_emp(request : Request, emp_id):
    '''
        Update Employee info
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    emp = Employee.objects.get(id=emp_id)
    request.data.update(user=request.user.id)
    updated_emp = EmployeesSerializer(instance=emp, data=request.data)
    if updated_emp.is_valid():
        updated_emp.save()
        responseData = {
            "msg" : "updated successefully"
        }
        return Response(responseData)
    else:
        print(updated_emp.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

# Delete ID Employee
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_emp(request: Request, emp_id):
    '''
        delete an employee
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    emp = Employee.objects.get(id=emp_id) 
    emp.delete()
    return Response({"msg" : "Deleted Successfully"})

# Add New Request 
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_req(request:Request, emp_id):
    ''' 
        this function adds a new request 
    '''
    user:User = request.user
    emp = Employee.objects.get(id=emp_id)
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    if ReqEmployee.objects.filter(user=request.user.id , employee=emp).exists():
        return Response({"msg" : "You have already created a request !"}, status=status.HTTP_400_BAD_REQUEST)
    request.data.update(user=request.user.id, employee=emp.id)

    req = ReqEmployeeSerializer(data=request.data)
    if req.is_valid():
        req.save()
        dataResponse = {
        "msg" : "Created Successfully",
        "req" : req.data
        }
        return Response(dataResponse)
    else:
        print(req.errors)
        dataResponse = {"msg" : "couldn't add a request"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

# Get Company ID Request - Received  request (for the company the employee belongs to)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_req(request: Request):
    ''' 
    This function is to list all of the requests
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    req = ReqEmployee.objects.filter(user=user.id)
    dataResponse = {
        "msg" : "List of employees requests",
        "req" : ReqEmployeeSerializer(instance=req, many=True).data
    }

    return Response(dataResponse)

# Delete ID Request
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_req(request: Request, req_id):
    
    '''
        Delete a request
    '''
    user:User = request.user
    req = ReqEmployee.objects.get(id=req_id) 
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    if ReqEmployee.objects.filter(user=request.user.id).exists() :
        req.delete()

    return Response({"msg" : "Deleted Successfully"})

# Get Company ID Request - Sent
# Get ID Request 

# Add Fav 
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_fav(request:Request, emp_id):
    ''' 
        this function adds an employee to the fav
    '''
    user:User = request.user
    emp = Employee.objects.get(id=emp_id)
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    if Fav.objects.filter(user=request.user.id , employee=emp).exists():
        return Response({"msg" : "You have already added this employee to your faivorate!"}, status=status.HTTP_400_BAD_REQUEST)
    request.data.update(user=request.user.id, employee=emp.id)

    fav = FavSerializer(data=request.data)
    if fav.is_valid():
        fav.save()
        dataResponse = {
        "msg" : "Created Successfully",
        "fav" : fav.data
        }
        return Response(dataResponse)
    else:
        dataResponse = {"msg" : "couldn't add a request"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

# Get Fav
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_fav(request: Request):
    ''' 
    This function is to list all of the fav employees
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    fav = ReqEmployee.objects.filter(user=user.id)
    dataResponse = {
        "msg" : "List of your fav employees",
        "fev" : ReqEmployeeSerializer(instance=fav, many=True).data
    }

    return Response(dataResponse)

# Delete fav
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_fav(request: Request, emp_id):
    '''
        Delete an emp from fav
    '''
    user:User = request.user
    emp = Fav.objects.get(id=emp_id) 
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    if Fav.objects.filter(user=request.user.id).exists() :
        emp.delete()

    return Response({"msg" : "Deleted Successfully"})