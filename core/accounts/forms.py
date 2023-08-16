from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(AuthenticationForm):
    """
    This class defines fields of login form
    """
    username = forms.CharField(label="Email address", min_length=7, max_length=20,
                            validators=[RegexValidator(r'^[A-Za-z0-9+_.-]+@(.+)$',
                            message="The email format is not correct.")], widget=forms.TextInput(
                            attrs={'placeholder':"Enter your email address"}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder":"Enter your password","autocomplete": "current-password"}),
    )



class SignupForm(UserCreationForm):
    """
    This class defines fields of signup form
    """
    email = forms.CharField(label="Email address", min_length=8, max_length=20, 
                        validators=[RegexValidator(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',message="Your email format is not correct.")],
                        widget=forms.TextInput(attrs={"placeholder":"Example: admin@admin.com"}))
    
    username = forms.CharField(label="Username", min_length=8, max_length=20,
                        validators=[RegexValidator(r"^(?=[a-zA-Z0-9._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$",
                        message="The username is 8-20 characters long and must include numbers and chars.")],
                        required=False,
                        widget=forms.TextInput(attrs={"placeholder":"Enter your username"})
                        )

    password1 = forms.CharField(label=("Password"),strip=False, min_length=5, max_length=50,
                widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                "placeholder":"Password must be a bit complex"}),)
    
    password2 = forms.CharField(label="Password Confirmation", strip=False, 
                widget= forms.PasswordInput(attrs={"autocomplete": "new-password","placeholder":"Enter the same password as before"}))
    

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]