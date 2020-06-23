from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Inquery
from django.utils import timezone
from django.db.models import F

def show_inquery(request):
	inqueries=Inquery.objects
	return render(request, 'inquery/show_inquery.html',{'entrybook':inqueries,'title':'Old Inqueries'})

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
			return redirect('home')				
		else:
			messages.success(request, 'invalid data entry')

			return render(request, 'inquery/inquery_form.html',{'title':'New inquery','new':new_entry_number,'dates':date_only})
	else:	
		return render(request, 'inquery/inquery_form.html',{'title':'New inquery','new':new_entry_number,'dates':date_only})

