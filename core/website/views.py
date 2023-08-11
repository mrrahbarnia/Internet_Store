from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm, NewsletterForm


# Create your views here.

def index_view(request):
    return render(request, "website/index.html")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message submitted,thank you.")
            return render(request, 'website/contact.html',{"form":form})
        messages.error(request, "Your message didn't submit.")
    form = ContactForm()
    return render(request, "website/contact.html", {"form":form})

def about_view(request):
    return render(request, "website/about.html")


def newsletter_view(request):
    next = request.POST.get('next', '/')
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            # next = request.POST.get('next', '/')
            messages.success(request, "Your information was sent,thank you.")
            return HttpResponseRedirect(next,{"form":form})
        messages.error(request, "Your information wasn't sent.")
    form = NewsletterForm()
    return HttpResponseRedirect(next,{"form":form})
