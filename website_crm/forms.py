from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

# Sign Up Form model

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email address...'}))
    first_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name...'}))
    last_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name...'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User name...'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


# Add Record here...

class AddRecord(forms.ModelForm):
    first_name = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name...'}))
    last_name = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name...'}))
    email = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email...'}))
    phone = forms.CharField(required=True,max_length=25,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone...'}))
    address = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address...'}))
    city = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City...'}))
    state = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'State...'}))
    zip_code = forms.CharField(required=True,max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zip Code...'}))

    class Meta:
        model = Record
        exclude = ('user',)