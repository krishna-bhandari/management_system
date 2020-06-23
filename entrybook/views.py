from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from .forms import Sign_up_form,update_profile
from .models import *
from django.utils import timezone
from django.db.models import F



def home(request):
	return render(request,'entrybook/index.html',{})

#display the entries
@login_required
def laptop_entry(request):
	entrybook=Laptop_entry.objects
	return render(request, 'entrybook/laptop_entrybook.html',{'entrybook':entrybook,'title':'Laptop'})
@login_required
def desktop_entry(request):
	entrybook=Desktop_entry.objects
	return render(request, 'entrybook/desktop_entrybook.html',{'entrybook':entrybook,'title':'Desktop'})
@login_required
def recovery_entry(request):
	entrybook=Recovery.objects
	return render(request, 'entrybook/recovery_entrybook.html',{'entrybook':entrybook,'title':'Recovery'})

	#input entry
@login_required
def input_desktop_entry(request):
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
		if request.POST['entry_number'] and request.POST['customer_name'] and request.POST['address'] and request.POST['contact'] and request.POST['device_detail']:
			desktop=Desktop_entry()
			desktop.entry_number=request.POST['entry_number']
			desktop.device_detail=request.POST['device_detail']
			desktop.device_name=request.POST['device_name']
			desktop.customer_name=request.POST['customer_name']
			desktop.problem==request.POST['problem']
			# desktop.solution=request.POST['category']
			# desktop.status=request.POST['status']
			# desktop.remarks=request.POST['remarks']
			desktop.contact=request.POST['contact']
			desktop.address=request.POST['address']
			desktop.entry_date=timezone.datetime.now().strftime('%Y-%m-%d')
			desktop.save()
			return redirect('home')				
		else:
			messages.success(request, 'invalid data entry')

			return render(request, 'entrybook/desktop_entryform.html',{'title':'Desktop Entry','new':new_entry_number,'dates':date_only})
	else:	
		return render(request, 'entrybook/desktop_entryform.html',{'title':'Desktop Entry','new':new_entry_number,'dates':date_only})
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
			laptop.problem==request.POST['problem']
			# laptop.solution=request.POST['category']
			# desktop.status=request.POST['status']
			# desktop.remarks=request.POST['remarks']
			laptop.contact=request.POST['contact']
			laptop.address=request.POST['address']
			laptop.entry_date=timezone.datetime.now().strftime('%Y-%m-%d')
			laptop.save()
			return redirect('home')
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
			recovery.problem==request.POST['problem']
			# recovery.solution=request.POST['category']
			# desktop.status=request.POST['status']
			# desktop.remarks=request.POST['remarks']
			recovery.contact=request.POST['contact']
			recovery.address=request.POST['address']
			recovery.entry_date=timezone.datetime.now().strftime('%Y-%m-%d')
			recovery.save()
			return redirect('home')
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
