from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('change_password/', views.PasswordChange.as_view(), name="change_password"),
    path('change_password_done/', views.PasswordChangeDone.as_view(), name="change_password_done"),

    path('profile/<slug:username>/', views.profile, name="profile"),

]