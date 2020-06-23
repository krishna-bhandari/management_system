from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

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
