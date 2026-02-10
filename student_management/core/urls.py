from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "core"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Login page
    path('login/', LoginView.as_view(
        template_name='core/login.html',
        redirect_authenticated_user=True
    ), name='login'),

    # Logout page (POST)
    path('logout/', LogoutView.as_view(next_page='core:login'), name='logout'),
]
