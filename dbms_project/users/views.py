from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterFormStudent, UserRegisterFormStartup, CustomerForm, UserUpdateForm
from main.decorators import unauthenticated_user, allowed_users

@unauthenticated_user
def register_student(request):
    if request.method == 'POST':
        form = UserRegisterFormStudent(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            messages.success(request, f'Your account has been created! You can now login!')
            return redirect('login')
    else:
        form = UserRegisterFormStudent()

    return render(request, 'users/register.html', {'form': form})

@login_required
def customer(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = CustomerForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            if request.user.profile.get_validity():
                messages.success(request, f'Your profile information has been fully updated! You can start booking now!')

            return redirect('customer')

    else:
        if not request.user.profile.get_validity():
            messages.error(request, f'You need to fully update your profile information before you start booking!')
        u_form = UserUpdateForm(instance=request.user)
        p_form = CustomerForm(instance=request.user.profile) 

    context = {
        'u_form':  u_form,
        'p_form': p_form
    }
    return render(request, 'users/customer.html', context)

