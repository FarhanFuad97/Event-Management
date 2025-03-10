from django.urls import path
from users.views import signup_view, login_view,activate_user, logout_view, admin_dashboard, assign_role,create_group, group_list, no_permission, ProfileView,  CustomPasswordResetView, CustomPasswordRestConfirmView, EditProfileView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('activate/<int:user_id>/<str:token>/', activate_user),
    path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('admin/<int:user_id>/assign-role/', assign_role, name='assign-role'),
    path('admin/create-group/', create_group, name='create-group'),
    path('admin/group-list/', group_list, name='group-list'),
    path('no-permission/', no_permission, name='no-permission'),
    path('my_profile/', ProfileView.as_view(), name = 'profile'),
    path('password-change/', PasswordChangeView.as_view(template_name='user/password_change.html'), name='password-change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'), name='password_change_done'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/confirm/<uidb64>/<token>/',CustomPasswordRestConfirmView.as_view(), name='password_reset_confirm' ),
    path("edit_profile/", EditProfileView.as_view(), name = "edit_profile"),
    
    
    
    
]