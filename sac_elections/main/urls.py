from django.urls import path, include

from . import views

urlpatterns = [
  # /
  path('', views.home, name='home'),
  # TEMPORARY
  path('signin', views.sign_in, name='signin'),
  path('signout', views.sign_out, name='signout'),
  path('callback', views.callback, name='callback'),
  path('vote', include([
  		path('/', views.vote, name='vote'),
  		path('/<category>', views.poll, name='poll'),
  	])),
  path('dashboard', views.dashboard, name='dashboard'),
]