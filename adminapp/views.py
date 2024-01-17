from django.shortcuts import render

# Create your views here.

def loginfun(request):
    return render(request, 'adminapp/pages-login.html')

def registerfun(request):
    return render(request, 'adminapp/pages-register.html')

def dashboardfun(request):
    return render(request, 'adminapp/pages-dashboard.html')

def customerfun(request):
    return render(request, 'adminapp/pages-customer.html')

def peoplefun(request):
    return render(request, 'adminapp/pages-people.html')

def companyfun(request):
    return render(request, 'adminapp/pages-company.html')

def leadfun(request):
    return render(request, 'adminapp/pages-lead.html')

def offerfun(request):
    return render(request, 'adminapp/pages-offer.html')


def invoicefun(request):
    return render(request, 'adminapp/pages-invoice.html')

def quotefun(request):
    return render(request, 'adminapp/pages-quote.html')

def paymentfun(request):
    return render(request, 'adminapp/pages-payment.html')

def expensesfun(request):
    return render(request, 'adminapp/pages-expense.html')

def productfun(request):
    return render(request, 'adminapp/pages-product.html')

def category_productfun(request):
    return render(request, 'adminapp/pages-product_category.html')


def layoutfun(request):
    return render(request, 'adminapp/components-layout.html')


def testfun(request):
    return render(request, 'adminapp/check-layout.html')


