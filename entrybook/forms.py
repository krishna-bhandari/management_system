from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import *
class update_profile(UserChangeForm):
	password = forms.CharField( widget=forms.TextInput(attrs={'type':'hidden'}))


	class Meta:
		model=User
		fields=('username','first_name','last_name','email','password',)




class Sign_up_form(UserCreationForm):
	email = forms.EmailField(label='Email address',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model=User
		fields=('username','first_name','last_name','email','password1','password2',)



	def __init__(self, *args, **kwargs):
		super(Sign_up_form,self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class']='form-control'
		self.fields['username'].widget.attrs['placeholder']='Enter UserName'
		self.fields['username'].help_text =''

		# self.fields['username'].label=''

		self.fields['password1'].widget.attrs['class']='form-control'
		self.fields['password2'].widget.attrs['class']='form-control'


class Order_form(ModelForm):
	class Meta:
		model= Orders
		fields='__all__'

	def __init__(self, *args, **kwargs):
		super(Order_form,self).__init__(*args, **kwargs)

		self.fields['order_detail'].widget.attrs['class']='form-control'
		self.fields['order_number'].widget.attrs['class']='form-control'
		self.fields['order_by'].widget.attrs['class']='form-control'
		self.fields['status'].widget.attrs['class']='form-control'
		self.fields['quantity'].widget.attrs['class']='form-control'
		self.fields['photo'].widget.attrs['class']='form-control'

class Update_order_form(ModelForm):
	class Meta:
		model= Orders
		fields='__all__'

	def __init__(self, *args, **kwargs):
		super(Update_order_form,self).__init__(*args, **kwargs)

		self.fields['order_detail'].widget.attrs['class']='form-control'
		self.fields['order_number'].widget.attrs['class']='form-control'
		self.fields['order_by'].widget.attrs['class']='form-control'
		self.fields['status'].widget.attrs['class']='form-control'
		self.fields['quantity'].widget.attrs['class']='form-control'
		self.fields['photo'].widget.attrs['class']='form-control'