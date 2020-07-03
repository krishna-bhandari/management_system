from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.utils import timezone
from django.db.models import F
from django.http import JsonResponse

from django.views.generic import ListView,View


def home(request):
	return render(request,'entrybook/index.html',{'greet':'WELCOME TO A-CET COMPUTERS'})

def home1(request):
	messages.success(request, 'This feature is under construction.')
	return render(request,'entrybook/index.html',{'greet':'THANKS FOR VISITING HERE'})
#display the entries
@login_required
def laptop_entry(request):
	entrybook=Laptop_entry.objects
	if entrybook is None:

		messages.success(request, 'No Entries. Click New Entry to add new entry.')

		return render(request, 'entrybook/laptop_entrybook.html',{'entrybook':entrybook,'title':'Laptop'})
	else:
		return render(request, 'entrybook/laptop_entrybook.html',{'entrybook':entrybook,'title':'Laptop'})
@login_required
def desktop_entry(request):
	entrybook=Desktop_entry.objects
	if entrybook is None:

		messages.success(request, 'No Entries. Click New Entry to add new entry.')

		return render(request, 'entrybook/desktop_entrybook.html',{'title':'Desktop'})
	else:
		return render(request, 'entrybook/desktop_entrybook.html',{'entrybook':entrybook,'title':'Desktop'})
@login_required
def recovery_entry(request):
	entrybook=Recovery.objects
	return render(request, 'entrybook/recovery_entrybook.html',{'entrybook':entrybook,'title':'Recovery'})

	#input entry
@login_required
def input_desktop_entry(request):
	user=User.objects
	last_entry=Desktop_entry.objects.last()
	if last_entry is not None:
		late=str(last_entry.entry_number)
		a=late.split('-')
		b=int(a[1])+1
		new_entry_number=a[0]+'-'+str(b)
	else:
		new_entry_number='D-1001'
	time=timezone.datetime.now()
	date_only=time.strftime('%Y-%m-%d')
	if request.method=='POST':
		if request.POST['entry_number'] and request.POST['problem'] and request.POST['customer_name'] and request.POST['address'] and request.POST['contact'] and request.POST['device_detail']:
			desktop=Desktop_entry()
			desktop.entry_number=request.POST['entry_number']
			desktop.device_detail=request.POST['device_detail']
			desktop.device_name=request.POST['device_name']
			desktop.customer_name=request.POST['customer_name']
			desktop.problem=request.POST['problem']
			desktop.contact=request.POST['contact']
			desktop.address=request.POST['address']
			desktop.technician=request.POST['technician']
			desktop.entry_date=timezone.datetime.now().strftime('%Y-%m-%d')
			desktop.save()
			messages.success(request, 'Entry added successfully')
			return redirect('desktop_entry')				
		else:
			messages.success(request, 'invalid data entry')

			return render(request, 'entrybook/desktop_entryform.html',{'staff':user,'title':'Desktop Entry','new':new_entry_number,'dates':date_only})
	else:	
		return render(request, 'entrybook/desktop_entryform.html',{'staff':user,'title':'Desktop Entry','new':new_entry_number,'dates':date_only})
@login_required
def input_laptop_entry(request):
	last_entry=Laptop_entry.objects.last()
	if last_entry is not None:
		late=str(last_entry.entry_number)
		a=late.split('-')
		b=int(a[1])+1
		new_entry_number=a[0]+'-'+str(b)
	else:
		new_entry_number='L-1001'	
	time=timezone.datetime.now()
	date_only=time.strftime('%Y-%m-%d')
	if request.method=='POST':
		if request.POST['entry_number'] and request.POST['customer_name'] and request.POST['address'] and request.POST['contact'] and request.POST['device_detail']:
			laptop=Laptop_entry()
			laptop.entry_number=request.POST['entry_number']
			laptop.device_detail=request.POST['device_detail']
			laptop.device_name=request.POST['device_name']
			laptop.customer_name=request.POST['customer_name']
			laptop.problem=request.POST['problem']
			laptop.contact=request.POST['contact']
			laptop.address=request.POST['address']
			laptop.technician=request.POST['technician']

			laptop.entry_date=timezone.datetime.now().strftime('%Y-%m-%d')
			laptop.save()
			messages.success(request, 'Entry added successfully')

			return redirect('laptop_entry')
		else:
			messages.success(request, 'invalid data entry')
			return render(request, 'entrybook/laptop_entryform.html',{'title':'Laptop Entry','new':new_entry_number,'dates':date_only})
	else:	
		return render(request, 'entrybook/laptop_entryform.html',{'title':'Laptop Entry','new':new_entry_number,'dates':date_only})
@login_required
def input_recovery_entry(request):
	last_entry=Recovery.objects.last()
	if last_entry is not None:

		late=str(last_entry.entry_number)
		a=late.split('-')
		b=int(a[1])+1
		new_entry_number=a[0]+'-'+str(b)
	else:
		new_entry_number='R-1001'	

	time=timezone.datetime.now()
	date_only=time.strftime('%Y-%m-%d')
	if request.method=='POST':
		if request.POST['entry_number'] and request.POST['customer_name'] and request.POST['address'] and request.POST['contact'] and request.POST['device_detail']:
			recovery=Recovery()
			recovery.entry_number=request.POST['entry_number']
			recovery.device_detail=request.POST['device_detail']
			recovery.device_name=request.POST['device_name']
			recovery.customer_name=request.POST['customer_name']
			recovery.problem=request.POST['problem']
			recovery.contact=request.POST['contact']
			recovery.technician=request.POST['technician']
			recovery.address=request.POST['address']
			recovery.entry_date=timezone.datetime.now().strftime('%Y-%m-%d')
			recovery.save()
			messages.success(request, 'Entry added successfully')

			return redirect('recovery_entry')
		else:
			messages.success(request, 'invalid data entry')

			return render(request, 'entrybook/recovery_entryform.html',{'title':'Recovery Entry','new':new_entry_number,'dates':date_only})
	else:	
		return render(request, 'entrybook/recovery_entryform.html',{'title':'Recovery Entry','new':new_entry_number,'dates':date_only})

def inqueries(request):
	pass

#user profile
def login_user(request):
	if request.method=='POST':
		username=request.POST['user_name']
		password=request.POST['password']
		user=authenticate(request,username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, 'successfully logged In')
			return redirect('home')
		else:
			messages.success(request, 'Login not successfull- Please try again..')
			return redirect('login')

	else:
		return render(request,'entrybook/login.html')

def logout_user(request):
	logout(request)
	messages.success(request, 'you have been logout')
	return redirect('home')

def register_user(request):
	if request.method=='POST':
		form=Sign_up_form(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data['username']
			password=form.cleaned_data['password1']
			user=authenticate(request,username=username, password=password)
			login(request, user)
			messages.success(request, 'Registeration successfull')
			return redirect('home')
	else:
		form=Sign_up_form()

	context ={'form':form}
	return render(request,'entrybook/register.html',context)


def update_user(request):
	if request.method=='POST':
		form=update_profile(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
		
			messages.success(request, 'Update successfull')
			return redirect('home')
	else:
		form=update_profile(instance=request.user)

	context ={'form':form}
	return render(request,'entrybook/update_profile.html',context)

def change_password(request):
	if request.method=='POST':
		form=PasswordChangeForm(data=request.POST,user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)	#used to keep user login after password change
			messages.success(request, 'Password successfully changed')
			return redirect('home')
	else:
		form=PasswordChangeForm(user=request.user)

	context ={'form':form}
	return render(request,'entrybook/change_password.html',context)


def show_users(request):

	user=User.objects
	context={'staff':user}
	return render(request,'entrybook/staff.html',context)


def delete_desktop_entry(request,entry_id):
	Desktop_entry.objects.get(id=entry_id).delete()
	messages.success(request, 'entry deleted successfully')
	return redirect('desktop_entry')
def delete_laptop_entry(request,entry_id):
	Laptop_entry.objects.get(id=entry_id).delete()
	messages.success(request, 'entry deleted successfully')
	return redirect('laptop_entry')
def delete_recovery_entry(request,entry_id):
	Recovery.objects.get(id=entry_id).delete()
	messages.success(request, 'entry deleted successfully')
	return redirect('recovery_entry')
    


def update_desktop_entrybook(request,entry_id):
	user=User.objects
	desktop=Desktop_entry.objects.get(id=entry_id)
	if request.method=='POST':
		if request.POST['status'] and request.POST['solution']and request.POST['remarks']and request.POST['entry_number']:
			desktop=Desktop_entry.objects.get(id=entry_id)
			desktop.entry_number=request.POST['entry_number']
			desktop.solution=request.POST['solution']
			desktop.status=request.POST['status']
			desktop.remarks=request.POST['remarks']
			desktop.technician=request.POST['technician']
			desktop.save()
			messages.success(request, 'entry updated successfully')
			return redirect('desktop_entry')				
		else:
			messages.success(request, 'invalid data entry')

			return render(request, 'entrybook/desktop_entrybook_update.html',{'staff':user,'title':'Update Entry','entry':desktop})
	else:	
		return render(request, 'entrybook/desktop_entrybook_update.html',{'staff':user,'title':'Update Entry','entry':desktop})
def update_laptop_entrybook(request,entry_id):
	user=User.objects
	desktop=Laptop_entry.objects.get(id=entry_id)
	if request.method=='POST':
		if request.POST['status'] and request.POST['solution']and request.POST['remarks']and request.POST['entry_number']:
			desktop=Laptop_entry.objects.get(id=entry_id)
			desktop.entry_number=request.POST['entry_number']
			desktop.solution=request.POST['solution']
			desktop.status=request.POST['status']
			desktop.remarks=request.POST['remarks']
			desktop.technician=request.POST['technician']
			desktop.save()
			messages.success(request, 'entry updated successfully')
			
			return redirect('laptop_entry')				
		else:
			messages.success(request, 'invalid data entry')

			return render(request, 'entrybook/laptop_entrybook_update.html',{'staff':user,'title':'Update Entry','entry':desktop})
	else:	
		return render(request, 'entrybook/laptop_entrybook_update.html',{'staff':user,'title':'Update Entry','entry':desktop})


def update_recovery_entrybook(request,entry_id):
	user=User.objects
	desktop=Recovery.objects.get(id=entry_id)
	if request.method=='POST':
		if request.POST['status'] and request.POST['solution']and request.POST['remarks']and request.POST['entry_number']:
			desktop=Recovery.objects.get(id=entry_id)
			desktop.entry_number=request.POST['entry_number']
			desktop.solution=request.POST['solution']
			desktop.status=request.POST['status']
			desktop.remarks=request.POST['remarks']
			desktop.technician=request.POST['technician']
			desktop.save()
			messages.success(request, 'entry updated successfully')
			
			return redirect('recovery_entry')				
		else:
			messages.success(request, 'invalid data entry')

			return render(request, 'entrybook/recovery_entrybook_update.html',{'staff':user,'title':'Update Entry','entry':desktop})
	else:	
		return render(request, 'entrybook/recovery_entrybook_update.html',{'staff':user,'title':'Update Entry','entry':desktop})

def show_inquery(request):
	inqueries=Inquery.objects
	return render(request, 'entrybook/show_inquery.html',{'entrybook':inqueries,'title':'Old Inqueries'})

@login_required
def submit_inquery(request):
	last_entry=Inquery.objects.last()
	if last_entry is not None:
		late=str(last_entry.entry_number)
		a=late.split('-')
		b=int(a[1])+1
		new_entry_number=a[0]+'-'+str(b)
	else:
		new_entry_number='I-1001'
	time=timezone.datetime.now()
	date_only=time.strftime('%Y-%m-%d')
	if request.method=='POST':
		if request.POST['customer_name'] and request.POST['address'] and request.POST['contact'] and request.POST['inquery_detail']:
			desktop=Inquery()
			desktop.entry_number=request.POST['entry_number']
			desktop.inquery_detail=request.POST['inquery_detail']
			desktop.customer_name=request.POST['customer_name']
			desktop.remarks=request.POST['remarks']
			
			desktop.contact=request.POST['contact']
			desktop.address=request.POST['address']
			desktop.entry_date=timezone.datetime.now().strftime('%Y-%m-%d')
			desktop.save()
			return redirect('inquery')				
		else:
			messages.success(request, 'invalid data entry')

			return render(request, 'entrybook/inquery_form.html',{'title':'New inquery','new':new_entry_number,'dates':date_only})
	else:	
		return render(request, 'entrybook/inquery_form.html',{'title':'New inquery','new':new_entry_number,'dates':date_only})

def show_order(request):
	order=Orders.objects
	return render(request, 'entrybook/show_order.html',{'order':order})

def create_order(request):
	form=Order_form()
	if request.method=='POST':
		form=Order_form(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'order in progress')
			return redirect('show_order')
		else:
			messages.success(request, 'invalid entry')
			return redirect('/')
	context={'form':form,'title':'New Order'}
	# messages.success(request, message)
	return render(request, 'entrybook/create_order.html',context )

def update_order(request,order_id):
	order=Orders.objects.get(id=order_id)
	form=Order_form(instance=order)
	if request.method=='POST':
		order=Orders.objects.get(id=order_id)
		form=Order_form(request.POST,instance=order)
		if form.is_valid():
			form.save()
			messages.success(request, 'order updated')
			return redirect('show_order')
		else:
			messages.success(request, 'invalid entry')
			return render(request, 'entrybook/update_order.html',context)
			
	else:
		context={'form':form,'title':'Update Order'}
		return render(request, 'entrybook/update_order.html',context)




# def delete_order(request,order_id):
# 	order_del=Orders.objects.get(id=order_id).delete()
# 	messages.success(request, 'order deleted')
# 	return redirect('show_order')
