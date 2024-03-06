from django.urls import path
from telecallerapp import views
 
app_name = 'telecallerapp' 

urlpatterns = [
   path('login/',  views.loginfun, name='login'),
   path('register/',  views.registerfun, name='register'),
   path('', views.dashboardfun, name='dashboard'),
   path('dashboard/', views.dashboardfun, name='dashboard'),
   path('customer/', views.customerfun, name='customers'),
   path('lead/', views.leadfun, name='leads'),
   path('update_lead/', views.update_leadfun, name='update_leadfun'),
   path('logout/', views.logoutfun, name='logout'),
]
