from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import EventDetailView,CircularDetailView,ClubDetailView

urlpatterns = [
      path('',views.signup, name="signup"),        
      path('accounts/', include('django.contrib.auth.urls')), 
      path('login/',views.CustomLoginView.as_view(), name='login',kwargs={'redirect_authenticated_user': True}),  
      path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name="logout"),
      path('editprofile/',views.editprofile, name="editprofile"),
      path('event/',views.event, name="event"),
      path('club/',views.club, name="club"),
      path('circular/',views.circular, name="circular"),
      path('home',views.home, name="home"),
      path('event_detail/<pk>/', EventDetailView.as_view(),name="event_detail"),
      path('circular_detail/<pk>/',CircularDetailView.as_view(),name="circular_detail"),
      path('club_detail/<pk>/',ClubDetailView.as_view(),name="club_detail"),
     
]