from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import logout_require
# Create your views here.


@logout_require
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created. You are ready to login')
            return redirect('login')
        else:
            return render(request, 'users/register.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        context = {
            'u_form': u_form,
        }
        return render(request, 'users/profile.html', context)
