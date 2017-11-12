from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from .forms import DateInput, TimeInput

# Create your views here.

# BEGIN_OF_CODE_GENERATION

# END_OF_CODE_GENERATION


@login_required()
def home_page(request):
    template_name = 'app/home_page.html'
    return render(request, template_name, {'user': request.user})


@login_required()
def user_profile(request):
    template_name = 'app/user_profile.html'
    return render(request, template_name, {'user': request.user})


@login_required
def user_update(request):
    template_name = 'app/user_profile_update.html'
    user = get_object_or_404(User, pk=request.user.id)
    form = UserChangeForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user-profile')
    return render(request, template_name, {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user-profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'app/change_password.html', {'form': form})
