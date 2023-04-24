from django.urls import path

from . import views

app_name = 'beverage'

urlpatterns = [
    path('new/', views.create_homebrew, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]
