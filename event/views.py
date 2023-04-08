from .models import Circular, Club, Department, Student,Event
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm,CustomAuthForm,EditProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.generic.detail import DetailView

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():        
            user=form.save(commit=False)     
            user.save()     
            Student.objects.create(user=user)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)            
            login(request, user)
            return redirect('/login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = CustomAuthForm

def home(request):
    now = datetime.now()
    circular=Circular.objects.filter(department__name=request.user.student.department).order_by('-id')[:3]
    dataset=Event.objects.filter(end_date__gte=now).order_by('-id')[:3] 
    club=Club.objects.order_by('-id')[:3]
    return render(request, 'index.html',{'dataset':dataset,'circular':circular,'club':club})


def event(request):
    now = datetime.now()
    dataset=Event.objects.filter(end_date__gte=now)
    return render(request, 'event.html',{'dataset':dataset})


  
class EventDetailView(DetailView):    
    model = Event

class CircularDetailView(DetailView):    
    model = Circular

class ClubDetailView(DetailView):    
    model = Club   

def circular(request):    
    circular=Circular.objects.filter(department__name=request.user.student.department)
    return render(request, 'circulars.html',{'circular':circular})

def club(request):
    club=Club.objects.all()    
    return render(request, 'club.html',{'club':club})

@login_required(login_url='/login/')
def editprofile(request):
    if request.method == "POST": 
        user = request.user
        student = user.student     
        form = EditProfileForm(request.POST,instance=student)       
        if form.is_valid():    
            student.save()            
            print(form)
            return redirect('home')
        else:
            return render(request,'editprofile.html', {'form': form})
    else:
        user = request.user
        student = user.student 
        form = EditProfileForm(instance=student)         
    return render(request,'editprofile.html', {'form': form})