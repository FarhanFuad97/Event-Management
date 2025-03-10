
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import  Group
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm,AssignRoleForm, CreateGroupForm, CustomPasswordResetForm, CustomPasswordResetConfirmForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

from django.views.generic import TemplateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model


User = get_user_model()




def is_admin(user):
    return user.groups.filter(name='Admin').exists()
def is_organizer(user):
    return user.groups.filter(name='Organizer').exists()


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active = False
            user.save()
            messages.success(request, 'A Confirmation mail sent. Please check your email')
            login(request, user)  
            return redirect('login')  
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})




@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



def activate_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if user.is_active:
            return HttpResponse("Your account is already activated.")
        
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save() 
            return redirect('login')  
        else:
            return HttpResponse("Invalid or expired activation link.")
    except User.DoesNotExist:
        return HttpResponse("User not found.")
    
@user_passes_test(is_admin, login_url='no-permission')
def admin_dashboard(request):
    users = User.objects.all()
    return render(request, 'admin/dashboard.html', {"users": users})

@user_passes_test(is_admin, login_url='no-permission')
def assign_role(request, user_id):
    user = User.objects.get(id=user_id)
    form = AssignRoleForm()
    if request.method == 'POST':
        form = AssignRoleForm(request.POST)
        if form.is_valid():  
            role = form.cleaned_data.get('role')
            user.groups.clear()  
            user.groups.add(role)
            messages.success(request, f"User {user.username} has been assigned to the {role.name} role")
            return redirect('admin-dashboard')
    return render(request, 'admin/assign_role.html', {"form": form})
@user_passes_test(is_admin, login_url='no-permission')
def create_group(request):
    form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)

        if form.is_valid():  
            group = form.save()
            messages.success(request, f"Group {group.name} has been created successfully")
            return redirect('create-group')
    
    return render(request, 'admin/create_group.html', {'form': form})

@user_passes_test(is_admin, login_url='no-permission')
def group_list(request):
    groups = Group.objects.all()
    return render(request, 'admin/group_list.html', {'groups': groups})



def no_permission(request):
    return render(request, 'no_permission.html')


@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    template_name = "user/my_profile.html"

    def get_context_data(self, **kwargs):
        user = self.request.user 
        context = super().get_context_data(**kwargs)
        context["user"] = user
        context["is_admin"] = is_admin(self.request.user)
        context["is_organizer"] = is_organizer(self.request.user)
        return context 
    

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'auth/reset_password.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['protocol'] = 'https'if  self.request.is_secure() else 'http'
        context['domain'] = self.request.get_host()
        return context

    def form_valid(self, form):
        messages.success(self.request, 'A Reset email sent. Please Check your email')
        
        return super().form_valid(form)
    
class CustomPasswordRestConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm
    template_name = 'auth/reset_password.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Password reset successfully')
        
        return super().form_valid(form)
    

class EditProfileView(UpdateView):
    model = User
    template_name = "user/edit_profile.html"
    form_class = EditProfileForm
    success_url = reverse_lazy("edit_profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_admin"] = is_admin(self.request.user)
        context["is_organizer"] = is_organizer(self.request.user)
        return context 
    
    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return redirect("edit_profile")
        
        
    










