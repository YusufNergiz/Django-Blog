from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Importing the Register view from the Users App inorder to directly use it in here
from users import views as user_view
# user_view is now gets the path to the views.py file of users App.

# Importing the built in Django Login and Logout Pages
from django.contrib.auth import views as auth_views
# auth_views now gives access to the built in Django classes of LoginView and LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name="password-reset"),
    path('register', user_view.register, name='register-page'),
    path('profile/', user_view.profile, name='profile'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)