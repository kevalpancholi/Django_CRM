from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

# Setting up a sign up form class to inherit from UserCreationForm class; extending its functionality and customising it
class SignUpForm(UserCreationForm):
    # attrs = {'class':'form-control'} adds bootstrap styling for form controls
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))

    # Meta class is an inner class that provides metadata about the model or form class it belongs to.
    # Meta class is used to configure various behaviours or options without adding additional methods or fields to the class.
    # Primarily used in models, forms, and admin configurations
    # In this case, the meta class is used to specify which model the form is based on, which fields to include/exclude
    # and how form widgets should behave
    class Meta:
        # User model is a built-in model in django that stores essential information about each user
        # such as username, password, email etc.
        model = User
        # Two passwords for typing and re-typing a password when signing up to prevent typos
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        # Constructor which is automatically called when an object is created; allows class to initialise the attributes of the object or perform setups
        # Init method used to customise the form fields when the form is instantiated
        # *args = lets you pass as many arguments as you want, and they will be captured as a tuple
        # **kwargs = lets you pass as many key word arguments to a function, and they will be captured as a dictionary
    def __init__(self, *args, **kwargs):
        # Super() method calls the parent class' (UserCreationForm's) __init__() method
        # Then adds custom behaviour, such as setting HTML attributes - basically extending its functionality
        # Super() can be used to call any method or property that exists in the parent class
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

# class AddRecordForm(forms.ModelForm):
#     earning_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"placeholder":"YYYY-MM-DD", "class":"form-control", "type":"date"}), label='')
#     cash_sale = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Cash Sale", "class":"form-control"}), label='', decimal_places=2)
#     NMS_num = forms.IntegerField(required=True, widget =forms.widgets.NumberInput(attrs={"placeholder":"No. of NMS", "class":"form-control"}), label='', min_value=0)
#     NMS_earning = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"NMS Earning", "class":"form-control"}), label='', decimal_places=2)
#     flu_vacc_num = forms.IntegerField(required=True, widget =forms.widgets.NumberInput(attrs={"placeholder":"No. of Flu Vaccinations", "class":"form-control"}), label='', min_value=0)
#     flu_earning = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Flu Earning", "class":"form-control"}), label='', decimal_places=2)
#     covid_vacc_num = forms.IntegerField(required=True, widget =forms.widgets.NumberInput(attrs={"placeholder":"No. of Covid Vaccinations", "class":"form-control"}), label='', min_value=0)
#     covid_earning = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Covid Earning", "class":"form-control"}), label='', decimal_places=2)

#     class Meta:
#         model = Record
#         # Exclude created_at field from the record model as input date will automatically be recorded
#         exclude = ("created_at",)

class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        # Exclude created_at field from the record model as input date will automatically be recorded
        exclude = ("created_at",)
        widgets = {
            'earning_date': forms.DateInput(attrs={"placeholder": "YYYY-MM-DD", "class": "form-control", "type": "date"}),
            'cash_sale': forms.NumberInput(attrs={"placeholder": "Cash Sale", "class": "form-control"}),
            'NMS_num': forms.NumberInput(attrs={"placeholder": "No. of NMS", "class": "form-control"}),
            'NMS_earning': forms.NumberInput(attrs={"placeholder": "NMS Earning", "class": "form-control"}),
            'flu_vacc_num': forms.NumberInput(attrs={"placeholder": "No. of Flu Vaccinations", "class": "form-control"}),
            'flu_earning': forms.NumberInput(attrs={"placeholder": "Flu Earning", "class": "form-control"}),
            'covid_vacc_num': forms.NumberInput(attrs={"placeholder": "No. of Covid Vaccinations", "class": "form-control"}),
            'covid_earning': forms.NumberInput(attrs={"placeholder": "Covid Earning", "class": "form-control"}),
        }

    # Dynamically make all fields required
    def __init__(self, *args, **kwargs):
        super(AddRecordForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True  # Ensure all fields are required
            field.label = ""  # Remove any default field labels
