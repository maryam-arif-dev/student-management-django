from django.urls import path
from . import views

app_name = 'enrollments'

urlpatterns = [
    path('', views.enrollment_list, name='list'),
    path('add/', views.add_enrollment, name='add'),
    path('edit/<int:id>/', views.edit_enrollment, name='edit'),
    path('delete/<int:id>/', views.delete_enrollment, name='delete'),
]
