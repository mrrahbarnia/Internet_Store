from django.shortcuts import render
from .forms import LoginForm, SignupForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout ,decorators
from django.contrib import messages

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Logged in as {request.user.username}')
                    if 'next' in request.POST:
                        return HttpResponseRedirect(request.POST.get('next'),{"form":form})
                    else:
                        return HttpResponseRedirect('/' , {"form":form})
        context = {"form":LoginForm()} 
        return render(request, "accounts/login.html", context)
    else:
        messages.info(request, f"You have already loged in before as {request.user.username}.")
        return HttpResponseRedirect('/',{"form":LoginForm()})
    
@decorators.login_required()
def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out')
    if 'next' in request.GET:
        return HttpResponseRedirect(request.GET.get('next'))
    else:
        return HttpResponseRedirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                context = {"form":form}
                messages.success(request, "Signed up.")
                if "next" in request.POST:
                    return HttpResponseRedirect(request.POST.get('next'), context)
                else:
                    return HttpResponseRedirect('/', context)
            messages.error(request, "You didn't register successfully.")
            if "next" in request.POST:
                return HttpResponseRedirect(request.POST.get('next'), {"form":SignupForm()})
            else:
                return HttpResponseRedirect('/', {"form":SignupForm()})
        return render(request, 'accounts/signup.html', {"form":SignupForm()})
    else:
        messages.info(request, "You have already signed up before.")
        return HttpResponseRedirect('/')