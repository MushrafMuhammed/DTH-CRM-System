from django.urls import path
from adminapp import views
import adminapp

app_name = 'adminapp'

urlpatterns = [
   path('login/',  views.loginfun, name='login'),
   path('register/',  views.registerfun, name='register'),
   path('',  views.dashboardfun, name='dashboard'),
   path('dashboard/', views.dashboardfun, name='dashboard'),
   path('customer/', views.customerfun, name='customers'),
   path('people/', views.peoplefun, name='people'),
   path('company/', views.companyfun, name='companies'),
   path('lead/', views.leadfun, name='leads'),
   path('offer/', views.offerfun, name='offers'),
   path('invoice/', views.invoicefun, name='invoice'),
   path('quote/', views.quotefun, name='quote'),
   path('payment/', views.paymentfun, name='payment'),
   path('expenses/', views.expensesfun, name='expense'),
   path('product/', views.productfun, name='product'),
   path('product_category/', views.category_productfun, name='category_product'),
   # path('layout/', views.layoutfun, name='layout'),
   # path('test/', views.testfun, name='test'),



]
