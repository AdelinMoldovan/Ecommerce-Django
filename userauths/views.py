from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from userauths import models as userauths_models
from userauths import forms as userauths_forms
from vendor import models as vendor_models


def register_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Deja sunteți autentificat")
        return redirect('/')   

    form = userauths_forms.UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()

        full_name = form.cleaned_data.get('full_name')
        email = form.cleaned_data.get('email')
        mobile = form.cleaned_data.get('mobile')
        password = form.cleaned_data.get('password1')
        user_type = form.cleaned_data.get("user_type")

        user = authenticate(email=email, password=password)
        login(request, user)

        messages.success(request, f"Contul a fost creat cu success")
        profile = userauths_models.Profile.objects.create(full_name = full_name, mobile = mobile, user=user)
        if user_type == "Vendor":
            vendor_models.Vendor.objects.create(user=user, store_name=full_name)
            profile.user_type = "Vendor"
        else:
            profile.user_type = "Customer"
        
        profile.save()

        next_url = request.GET.get("next", 'store:index')
        return redirect(next_url)
    
    context = {
        'form':form
    }
    return render(request, 'userauths/sign-up.html', context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "Deja sunteți autentificat")
        return redirect('store:index')
    
    if request.method == 'POST':
        form = userauths_forms.LoginForm(request.POST)  
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            captcha_verified = form.cleaned_data.get('captcha', False)  

            if captcha_verified:
                try:
                    user_instance = userauths_models.User.objects.get(email=email, is_active=True)
                    user_authenticate = authenticate(request, email=email, password=password)

                    if user_instance is not None:
                        login(request, user_authenticate)
                        messages.success(request, "Sunteți autentificat")
                        next_url = request.GET.get("next", 'store:index')

                        print("next_url ========", next_url)
                        if next_url == '/undefined/':
                            return redirect('store:index')
                        
                        if next_url == 'undefined':
                            return redirect('store:index')

                        if next_url is None or not next_url.startswith('/'):
                            return redirect('store:index')

                        return redirect(next_url)

                    else:
                        messages.error(request, 'Numele de utilziator sau parola nu există')
                except userauths_models.User.DoesNotExist:
                    messages.error(request, 'User does not exist')
            else:
                messages.error(request, 'Verificarea Captcha a eșuat. Vă rugăm să încercați din nou.')

    else:
        form = userauths_forms.LoginForm()  

    return render(request, "userauths/sign-in.html", {'form': form})

def logout_view(request):
    if "cart_id" in request.session:
        cart_id = request.session['cart_id']
    else:
        cart_id = None
    logout(request)
    request.session['cart_id'] = cart_id
    messages.success(request, 'Ați fost deconectat')
    return redirect("userauths:sign-in")

def handler404(request, exception, *args, **kwargs):
    context = {}
    response = render(request, 'userauths/404.html', context)
    response.status_code = 404
    return response

def handler500(request, *args, **kwargs):
    context = {}
    response = render(request, 'userauths/500.html', context)
    response.status_code = 500
    return response

