from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from ..models import User_extInfo
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        # fields = '__all__'
#
class UserextForm(forms.ModelForm):
    class Meta:
        model = User_extInfo
        fields = ['emp_contact','emp_job_title','emp_no_of_employees','emp_interest','emp_free_text','emp_country']
