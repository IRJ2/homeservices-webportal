from django.shortcuts import render
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site."""

    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def clientLogin(request):
    """View function for home page of site."""

    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'client_login.html', context=context)

def workerLogin(request):
    """View function for home page of site."""

    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'worker_login.html', context=context)

def expertsList(request):
    """View function for home page of site."""

    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'experts_list.html', context=context)