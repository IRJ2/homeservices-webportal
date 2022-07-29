from django.http import  HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from catalog.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    """View function for home page of site."""

    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def clientLogin(request):
    """View function of login page for customers."""
    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['password']
        
        check_client = Customer.objects.filter(c_uid  = email, c_password = password1).count()

        if check_client == 1:
            request.session['client'] = email
            return redirect('home_client')

        else:
            return HttpResponse('<h3>Please enter valid Username or Password.</h3>')
    else:
        return render(request, 'client_login.html')

    context = {

    }

    # Render the HTML template client_login.html with the data in the context variable
    return render(request, 'client_login.html', context=context)

def clientSignup(request):
    """View function of signup page for customers."""
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['re-password']


        if password1==password2 :
            client = Customer.objects.create(c_fname = name,
                                            c_uid = email,
                                            c_password = password1)
            client.save()
            return redirect('client_login')
        else:
            return redirect('client_signup')
    context = {

    }

    # Render the HTML template client_signup.html with the data in the context variable
    return render(request, 'client_signup.html', context=context)

def clientProfile(request):
    """View function of signup page for customers."""

    context = {

    }

    # Render the HTML template client_profile.html with the data in the context variable
    return render(request, 'client_profile.html', context=context)

def expertProfile(request):
    """View function of expert's profile page for experts."""

    context = {

    }

    # Render the HTML template expert_profile.html with the data in the context variable
    return render(request, 'expert_profile.html', context=context)

def expertDisplayProfile(request):
    """View function of expert's profile page for experts."""

    context = {

    }

    # Render the HTML template expert_Display_profile.html with the data in the context variable
    return render(request, 'expert_display_profile.html', context=context)

def expertLogin(request):
    """View function of login page for experts."""
    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['password']
        
        check_expert = Worker.objects.filter(W_email  = email, W_password = password1).count()

        if check_expert == 1:
            request.session['expert'] = email
            return redirect('home_expert')
        else:
            return HttpResponse('<h3>Please enter valid Username or Password.</h3>')
    
    else:
        return render(request, 'expert_login.html')
    context = {

    }

    # Render the HTML template worker_login.html with the data in the context variable
    return render(request, 'expert_login.html', context=context)

def expertSignup(request):
    """View function for signup page of service experts"""
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['re-password']
        companyname = request.POST['companyname']
        categories = request.POST['categories']
        rate = request.POST['rate']
        motto = request.POST['motto']
        desc = request.POST['desc']
        phone = request.POST['phone']

        if password1==password2 :
            expert = Worker.objects.create(W_fname = name,
                                            W_email = email,
                                            W_password = password1,
                                            W_company = companyname,
                                            W_company_motto = motto,
                                            W_desc = desc,
                                            W_category = categories,
                                            w_phno = phone,
                                            Rate_P_Hour = rate)
            expert.save()
            return redirect('expert_login')
        else:
            return redirect('expert_signup')


    context = {

    }

    # Render the HTML template expert_signup.html with the data in the context variable
    return render(request, 'expert_signup.html', context=context)

def expertsList(request):
    """View function of list view of service experts"""

    context = {

    }

    # Render the HTML template experts_list.html with the data in the context variable
    return render(request, 'experts_list.html', context=context)

def expertsDetail(request):
    """View function for detail view of service experts"""

    context = {

    }

    # Render the HTML template experts_detail.html with the data in the context variable
    return render(request, 'experts_detail.html', context=context)

def homeClient(request):
    """View function for detail view of service experts"""

    context = {

    }

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'client_home.html', context=context)

def homeExpert(request):
    """View function for detail view of service experts"""

    context = {

    }

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'expert_home.html', context=context)