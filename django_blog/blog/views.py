
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})



@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email')
        user.save()
    return render(request, 'blog/profile.html', {'user': request.user})

# Create your views here.
