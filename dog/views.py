from registration.backends.simple.views import RegistrationView
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from dog.models import Region
from dog.models import Cottage
from dog.forms import RegionForm
from dog.forms import CottageForm
from dog.forms import UserForm
from dog.forms import UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.template import RequestContext

def index(request):

   request.session.set_test_cookie()
   region_list = Region.objects.order_by('-likes')[:5]
   cottage_list = Cottage.objects.order_by('-views')[:5]
   context_dict = {'cottages':cottage_list, 'regions':region_list}

   visitor_cookie_handler(request)
   context_dict['visits'] = request.session['visits']

   print(request.session['visits'])
   
   response = render(request, 'dog/index.html', context=context_dict)
   return response

def about(request):
   context_dict = {}
   visitor_cookie_handler(request) 
   context_dict['visits'] = request.session['visits']
   return render(request, 'dog/about.html', context=context_dict)

def show_region(request, region_name_slug):
   context_dict = {}
   try:
      region = Region.objects.get(slug=region_name_slug)
      cottages = Cottage.objects.filter(region=region)
      context_dict['cottages'] = cottages
      context_dict['region'] = region
   except Region.DoesNotExist:
      context_dict['cottages'] = None
      context_dict['region'] = None
      
   return render(request, 'dog/region.html', context_dict)

def add_region(request):
   form = RegionForm()

   if request.method =='POST':
      form = RegionForm(request.POST)

      if form.is_valid():
         reg = form.save(commit=True)
         print(reg, reg.slug)
         
         return index(request)
   
      else: print(form.errors)
   return render(request, 'dog/add_region.html', {'form':form})


def add_cottage(request, region_name_slug):
   try:
      region = Region.objects.get(slug=region_name_slug)
   except Region.DoesNotExist:
      region = None
   
   form = CottageForm()
   if request.method == 'POST':
      form = CottageForm(request.POST)
      if form.is_valid():
         if region:
            cottage = form.save(commit=False)
            cottage.region = region
            cottage.views = 0
            cottage.save()
            return show_region(request, region_name_slug)
      else:
         print(form.errors)
         
   context_dict = {'form':form, 'region':region}      
   return render(request, 'dog/add_cottage.html', context_dict)


@login_required
def restricted(request):
   return render(request, 'dog/restricted.html', {})


#@login_required
#def user_logout(request):
#   logout(request)
#   return HttpResponseRedirect(reverse('index'))

def get_server_side_cookie(request, cookie, default_val=None):
      val = request.session.get(cookie)
      if not val:
         val = default_val
      return val

class MyRegistrationView(RegistrationView):
   def get_success_url(self, user):
      return '/dog/'


def visitor_cookie_handler(request):
      visits = int(request.COOKIES.get('visits', '1'))
      last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
      last_visit_time = datetime.strptime(last_visit_cookie[:-7],
      '%Y-%m-%d %H:%M:%S')

      if (datetime.now() - last_visit_time).days > 0:
         visits = visits + 1
         request.session['last_visit'] = str(datetime.now())
      else:
         
         request.session['last_visit'] = last_visit_cookie

      request.session ['visits'] = visits

      
      
