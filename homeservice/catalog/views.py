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
    """View function of login page for customers."""

    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'client_login.html', context=context)

def workerLogin(request):
    """View function of login page for workers."""

    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'worker_login.html', context=context)

def expertsList(request):
    """View function of list view of service experts"""

    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'experts_list.html', context=context)

def expertsDetail(request):
    """View function for detail view of service experts"""

    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'experts_detail.html', context=context)