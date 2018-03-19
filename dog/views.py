from registration.backends.simple.views import RegistrationView
from django.shortcuts import render_to_response,  get_object_or_404, render, redirect
from django.http import HttpResponse
from dog.models import Region, Comment, Cottage
from dog.forms import RegionForm, CottageForm, CommentForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.template import RequestContext
from django.views.generic import RedirectView
from django.db.models import Count

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

def searchresults(request):

   request.session.set_test_cookie()
   region_list = Region.objects.order_by('-likes')[:5]
   cottage_list = Cottage.objects.order_by('-views')[:5]
   context_dict = {'cottages':cottage_list, 'regions':region_list}

   visitor_cookie_handler(request)
   context_dict['visits'] = request.session['visits']

   print(request.session['visits'])

   response = render(request, 'dog/searchresults.html', context=context_dict)
   return response

def regions(request):
   context_dict = {}
   visitor_cookie_handler(request)
   context_dict['visits'] = request.session['visits']
   return render(request, 'dog/regions.html', context=context_dict)

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

def show_cottage(request, cottage_name_slug):
   context_dict = {}
   try:
      cottage = Cottage.objects.get(slug=cottage_name_slug)
      comments = Comment.objects.filter(cottage=cottage)
      context_dict['comments'] = comments
      context_dict['cottage'] = cottage
   except Cottage.DoesNotExist:
      context_dict['comments'] = None
      context_dict['cottage'] = None

   return render(request, 'dog/cottage.html', context_dict)

class CottageLikeToggle(RedirectView):
    def get_redirect_url(self, cottage_name_slug):
        print(self)
        slug = cottage_name_slug
        print(slug)
        obj = get_object_or_404(Cottage, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_


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

def browse_cottages(request):
      context_dict = {}
      try:
            cottages = Cottage.objects.all()
            context_dict['cottages'] = cottages
      except Cottage.DoesNotExist:
            context_dict['cottages'] = None
      
      
      return render(request, 'dog/browse_cottages.html', context_dict)



def mostliked(request, ):
      context_dict = {}
      try:
            mlcottages = Cottage.objects.all()
            mlcottages = Cottage.objects.annotate(like_count=Count('likes')).order_by('-like_count')
            context_dict['cottages'] = mlcottages
      except Cottage.DoesNotExist:
            context_dict['cottages'] = None
      print(mlcottages)
      
      return render(request, 'dog/browse_cottages.html', context_dict)
      

def mostviewed(request):
      context_dict = {}
      try:
            mvcottages = Cottage.objects.all()
            mvcottages = Cottage.objects.annotate(view_count=Count('views')).order_by('-view_count')
            context_dict['cottages'] = mvcottages
      except Cottage.DoesNotExist:
            context_dict['cottages'] = None
            
      return render(request, 'dog/browse_cottages.html', context_dict)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions

# class CottageLikeAPIToggle(APIView):
#     authentication_classes = (authentication.SessionAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)

#     def get(self, request, slug=None, format=None):
#         # slug = self.kwargs.get("slug")
#         obj = get_object_or_404(Post, slug=slug)
#         url_ = obj.get_absolute_url()
#         user = self.request.user
#         updated = False
#         liked = False
#         if user.is_authenticated():
#             if user in obj.likes.all():
#                 liked = False
#                 obj.likes.remove(user)
#             else:
#                 liked = True
#                 obj.likes.add(user)
#             updated = True
#         data = {
#             "updated": updated,
#             "liked": liked
#         }
#         return Response(data)

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
                        cottage.region = Region.objects.get(slug=region_name_slug)
                        cottage.views = 0
                        if 'image' in request.FILES:
                              cottage.image = request.FILES['image']
                              cottage.save()
                              return show_region(request, region_name_slug)
                  else:
                        print(form.errors)

      context_dict = {'form':form, 'region':region}
      return render(request, 'dog/add_cottage.html', context_dict)



def review(request, cottage_name_slug):
      context_dict = {}
      try:
            cottage = Cottage.objects.get(slug=cottage_name_slug)
      except CottageDoesNotExist:
            cottage = None

      comments = Comment.objects.order_by('-date_added')
      context = {'comments' : comments, 'cottage':cottage}
      return render (request, 'dog/review.html', context)


def sign(request, cottage_name_slug):
      try:
            cottage = Cottage.objects.get(slug=cottage_name_slug)
      except Cottage.DoesNotExist:
            cottage = None

      form = CommentForm()
      if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                  if cottage:
                     new_comment = Comment(name=request.POST['name'],comment=request.POST['comment'])
                     new_comment.cottage = cottage
                     new_comment.save()
                     return show_cottage(request, cottage_name_slug)
                  else:
                     print(form.errors)
      else:
            form = CommentForm()

      context_dict = {'form' : form, 'cottage': cottage}
      return render (request, 'dog/sign.html', context_dict)


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
