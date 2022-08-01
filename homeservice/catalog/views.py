from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from catalog.models import *
from django.contrib import messages
from django.http import Http404

# Create your views here.
def index(request):
    """View function for home page of site."""

    context = {

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def clientLogin(request):
    """View function of login page for customers."""
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password']

        client = Customer.objects.filter(c_uid = email, c_password = password1).count()

        if client == 1:
            request.session['email'] = email
            request.session['usr_type']="user"
            return redirect('home_client')
        else:
            return HttpResponse("Invalid Credentials")

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
            if Customer.objects.filter(c_uid = email).count()<1:
                client = Customer.objects.create(c_fname = name,
                                                c_uid = email,
                                                c_password = password1)
                client.save()
            else:
                return HttpResponse("Email already exists.")
            return redirect('client_login')
        else:
            return redirect('client_signup')
    context = {

    }

    # Render the HTML template client_signup.html with the data in the context variable
    return render(request, 'client_signup.html', context=context)

def clientProfile(request):
    """View function of signup page for customers."""

    if 'email' in request.session:
        current_client = request.session['email']
        client = Customer.objects.get(c_uid = current_client)
        context = {'client' : client}
        # Render the HTML template client_profile.html with the data in the context variable
        return render(request, 'client_profile.html',context=context)
    else:
        return redirect('index')


def expertProfile(request):
    """View function of expert's profile page for experts."""
    if 'email' in request.session:
        current_expert = request.session['email']
        expert = Worker.objects.get(W_email = current_expert)
        context = {'expert' : expert}
        # Render the HTML template expert_profile.html with the data in the context variable
        return render(request, 'expert_profile.html',context=context)
    else:
        return redirect('index')
    
def expertDisplayProfile(request):
    """View function of expert's profile page for experts."""
    if 'email' in request.session:
        current_expert = request.session['email']
        expert = Worker.objects.get(W_email = current_expert)
        context = {'expert' : expert}
        # Render the HTML template expert_Display_profile.html with the data in the context variable
        return render(request, 'expert_display_profile.html', context=context)
    else:
        return redirect('index')

def expertLogin(request):
    """View function of login page for experts."""
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password']

        expert = Worker.objects.filter(W_email = email, W_password = password1).count()

        if expert == 1:
            request.session['email'] = email
            request.session['usr_type']="worker"
            return redirect('home_expert')
        else:
            return HttpResponse("Invalid Credentials")
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
            if Worker.objects.filter(W_email = email).count()<1:
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
            else:
                return HttpResponse("Email already exists.")
            return redirect('expert_login')
        else:
            return redirect('expert_signup')

    context = {

    }

    # Render the HTML template expert_signup.html with the data in the context variable
    return render(request, 'expert_signup.html', context=context)

def getTemplateList(request):
    """Function to get the base generic template with respect to the type of user"""
    context = {}
    if request.session['usr_type'] == "user":
        context['parent_template'] = 'base_generic.html'
    else:
        context['parent_template'] = 'base_expert.html'
    return render(request, 'catalog/experts_list.html', context=context)

def getTemplateDetail(request):
    """Function to get the base generic template with respect to the type of user"""
    context = {}
    if request.session['usr_type'] == "user":
        context['parent_template'] = 'base_generic.html'
    else:
        context['parent_template'] = 'base_expert.html'
    return render(request, 'catalog/worker_detail.html', context=context)
    
class PlumbingListView(generic.ListView):
    """Class for the list view of experts in Plumbing Service"""
    model = Worker
    context_object_name = 'worker_list'   # worker_list is a list of template variable
    queryset = Worker.objects.filter(W_category__icontains='Plumbing Service')[0:] # Get all experts containing in Plumbing Service category
    template_name = 'catalog/experts_list.html'  # Specify template location

class ACServicingListView(generic.ListView):
    model = Worker
    context_object_name = 'worker_list'   # worker_list is a list of template variable
    queryset = Worker.objects.filter(W_category__icontains='AC Servicing')[0:] # Get all experts containing in Plumbing Service category
    template_name = 'catalog/experts_list.html'  # Specify template location

class CarpentryListView(generic.ListView):
    model = Worker
    context_object_name = 'worker_list'   # worker_list is a list of template variable
    queryset = Worker.objects.filter(W_category__icontains='Carpentry')[0:] # Get all experts containing in Plumbing Service category
    template_name = 'catalog/experts_list.html'  # Specify template location

class ElectricWorksListView(generic.ListView):
    model = Worker
    context_object_name = 'worker_list'   # worker_list is a list of template variable
    queryset = Worker.objects.filter(W_category__icontains='Electric Works')[0:] # Get all experts containing in Plumbing Service category
    template_name = 'catalog/experts_list.html'  # Specify template location

class HomeCleaningListView(generic.ListView):
    model = Worker
    context_object_name = 'worker_list'   # worker_list is a list of template variable
    queryset = Worker.objects.filter(W_category__icontains='Home Cleaning')[0:] # Get all experts containing in Plumbing Service category
    template_name = 'catalog/experts_list.html'  # Specify template location

class LaptopRepairListView(generic.ListView):
    model = Worker
    context_object_name = 'worker_list'   # worker_list is a list of template variable
    queryset = Worker.objects.filter(W_category__icontains='Laptop Repair')[0:] # Get all experts containing in Plumbing Service category
    template_name = 'catalog/experts_list.html'  # Specify template location

class ExpertDetailView(generic.DetailView):
    """Class for the detail view of experts"""
    model = Worker
    def expert_detail_view(request, primary_key):
        try:
            # expert = Worker.objects.get(pk=primary_key)
            expert = Worker.objects.filter(W_email__icontains=primary_key)[:1]
        except Worker.DoesNotExist:
            raise Http404('Expert does not exist')
        return render(request, 'catalog/worker_detail.html', context={'expert': expert})

def homeClient(request):
    """View function for detail view of service experts"""
    if 'email' in request.session:
        
        context = {

        }

            # Render the HTML template home.html with the data in the context variable
        return render(request, 'client_home.html', context=context)
    return redirect('index')

def homeExpert(request):
    """View function for detail view of service experts"""
    if 'email' in request.session:
        context = {

        }

        # Render the HTML template home.html with the data in the context variable
        return render(request, 'expert_home.html', context=context)
    return redirect('index')

def logout(request):
    if 'email' in request.session:
        request.session.flush()
    return redirect('index')
