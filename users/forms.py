from django import forms
from django.contrib.auth.forms import UserCreationForm , PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import  Permission, Group
from users.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

 

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class AssignRoleForm(forms.Form):
    role = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Select a Role"
    )


class CreateGroupForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Assign Permission'
    )

    class Meta:
        model = Group
        fields = ['name', 'permissions'] 




class CustomPasswordResetForm(PasswordResetForm):
    pass

class CustomPasswordResetConfirmForm(SetPasswordForm):
    pass

   
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "profile_image", "phone"]





