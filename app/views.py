from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.views.generic import View
from django.http import HttpResponse
from .forms import UserForm
from app.convertor import convertfun
from django.views.decorators.csrf import csrf_exempt

def home(request):
    
    return render(request, 'app/index.html')

def register(request):
   # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['re_enter_password']
            if password == password2:
                user.set_password(password)
                user.save()
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return render(request, 'app/index.html')
            else:
                HttpResponse('Password must match')
                return render(request, 'app/register.html', {'form': form})

    else:
        form = UserForm()
    return render(request, 'app/register.html', {'form': form})
@csrf_exempt
def conversion(request):
    amount=request.POST.get('amount')
    try:
        amount=float(amount)
    except:
        HttpResponse('Invalid')
    convert_from=request.POST.get('convert')
    convert_to=request.POST.get('to')
    if (convert_from == convert_to):
       converted_amount=amount
    else :
        params={'base':convert_from,'symbols':convert_to}
        converted_amount=convertfun(amount,params)
    return HttpResponse(converted_amount)
