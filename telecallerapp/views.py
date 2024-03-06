from django.http import JsonResponse
from django.shortcuts import redirect, render
from adminapp.models import Lead, Status, Telecaller

# Create your views here.
def registerfun(request):
    if request.method == 'POST':
        print('reg-tested')
        name = request.POST.get('name')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(name,country,email,phone,password)
        
        try:
            print('tested')

            Telecaller.objects.create(
                name = name,
                country = country,
                phone = phone,
                email = email,
                password = password,
            )
            return redirect('telecaller:login')
        except Exception as e:
            return render(request, 'telecallerapp/pages-register.html',{'message': f'Error: {e}'})
    return render(request, 'telecallerapp/pages-register.html')

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
                 password = password
            )
            request.session['telecaller_sessionID'] = telecaller.id
            print(request.session['telecaller_sessionID'])
            return redirect('telecallerapp:dashboard')
        except :
            print('invalid username or password !')

        # if user is not None:
        #     login(request, user)
        #     return redirect('telecallerapp:dashboard')
        # else:
        #     print('Invalid credentials') 
    return render(request, 'telecallerapp/pages-login.html')

def dashboardfun(request):
    if 'telecaller_sessionID' in request.session:
        telecaller = request.session['telecaller_sessionID']
        profile = Telecaller.objects.get(id = telecaller)
    else:
        return redirect('telecallerapp:login')
    return render(request, 'telecallerapp/pages-dashboard.html', {'profile' : profile.name})

def customerfun(request):
    return render(request, 'telecallerapp/pages-customer.html')

def leadfun(request):
    telecaller = request.session['telecaller_sessionID']
    profile = Telecaller.objects.get(id = telecaller)
    leads = Lead.objects.filter(
        telecaller = telecaller
    )
    return render(request, 'telecallerapp/pages-lead.html', {'leads' : leads, 'profile' : profile.name})

def update_leadfun(request):
    try:
        if request.method == 'POST':
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
    if 'telecaller_sessionID' in request.session:
        request.session.flush()
    return redirect('telecallerapp:login')