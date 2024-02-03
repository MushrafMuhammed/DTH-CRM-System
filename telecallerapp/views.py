from django.http import JsonResponse
from django.shortcuts import redirect, render
from adminapp.models import Lead, Status, Telecaller


# Create your views here.
def loginfun(request):
    # if request.user.is_authenticated:
    #     return redirect('telecallerapp:dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = authenticate(username=username, password=password)
        try :
            telecaller = Telecaller.objects.get(
                 email = username,
                 phone = password
            )
            request.session["telecaller_sessionID"] = telecaller.id
            return redirect('telecallerapp:dashboard')
        except :
            print('invalid username or password !')

        # if user is not None:
        #     login(request, user)
        #     return redirect('telecallerapp:dashboard')
        # else:
        #     print('Invalid credentials') 
    return render(request, 'telecallerapp/pages-login.html')

def registerfun(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        country = request.POST.get('country')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        print(name,country,email,phone)
        
        try:
            Telecaller.objects.create(
                name = name,
                country = country,
                email = email,
                phone = phone
            )
            return redirect('login')
        except Exception as e:
            return render(request, 'telecallerapp/pages-register.html',{'message': f'Error: {e}'})
    return render(request, 'telecallerapp/pages-register.html')

def dashboardfun(request):
    telecaller = request.session["telecaller_sessionID"]
    profile = Telecaller.objects.get(id = telecaller)
    return render(request, 'telecallerapp/pages-dashboard.html', {'profile' : profile.name})

def customerfun(request):
    return render(request, 'telecallerapp/pages-customer.html')

def leadfun(request):
    telecaller = request.session["telecaller_sessionID"]
    profile = Telecaller.objects.get(id = telecaller)
    leads = Lead.objects.filter(
        telecaller = telecaller
    )
    status = Status.objects.all()
    return render(request, 'telecallerapp/pages-lead.html', {'leads' : leads, 'status' : status, 'profile' : profile.name})

def update_leadfun(request):
    try:
        if request.method == 'POST':
            # print('update checked')
            lead_id = request.POST.get('id')
            lead_status = request.POST.get('lead_status')
            print(lead_id,lead_status)
            editLeed  = Lead.objects.get(
                id=lead_id
            )
            editLeed.lead_status = lead_status

            editLeed.save()
            return JsonResponse({'message': 'Lead Status Updated successfully'})
            
    except Exception as e:
        return JsonResponse({'message': f'Error: {str(e)}'})

def logoutfun(request):
    if 'admin_sessionID' in request.session:
        request.session.flush()
    return redirect('telecallerapp:login')