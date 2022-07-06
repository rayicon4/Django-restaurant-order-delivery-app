from django import forms
import calculation
from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import customerinfomodel, morningmenu, afternoonmenu, eveningmenu, orderinfo


from django.forms import PasswordInput

##STUDY HOW TO BUILD CUSTOM FORMS AND DJANGO FORMS TO USE FOR PROJECT
# class myuserform(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(myuserform, self).__init__(*args, *kwargs)
#         self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
#         self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Confirm Password','class': 'form-control'})

#         class Meta:
#             model = User



# class customerpassword(forms.ModelForm):
#         password = forms.CharField(widget=forms.PasswordInput(attrs ={'class':'form-control','type':'password','placeholder':'Password'}), label='')



class customerinfoform(UserCreationForm):
    class Meta:
        model = customerinfomodel
        fields = ['username','firstname', 'lastname', 'email', 'phonenumber', 'location', 'password1', 'password2']


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class dashboardform(forms.ModelForm): ##morning
    class Meta:
        model = morningmenu
        fields = ['food_type', 'price', 'description']


class foodformat(forms.ModelForm): #afternoon
    class Meta:
        model = afternoonmenu
        fields = ['food_typea', 'pricea', 'descriptiona']


class dashboardformat(forms.ModelForm): ##evening
    class Meta:
        model = eveningmenu
        fields = ['food_types', 'prices', 'descriptions']




class TestForm(forms.Form):
    quantity = forms.DecimalField()
    price = forms.DecimalField()
    total = forms.DecimalField(
        widget=calculation.FormulaInput('quantity*price') # <- using single math expression
    )



class orderinfoform(forms.ModelForm):
    class Meta:
        model = orderinfo
        fields = ['order', 'created']

    # apply_taxes = forms.BooleanField(initial=True)
    # tax = forms.DecimalField(
    #     # using math expression and javascript functions.
    #     widget=calculation.FormulaInput('apply_taxes ? parseFloat(amount/11).toFixed(2) : 0.0') 
    # )

        