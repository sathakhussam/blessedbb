from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.Mylogin, name='login'),
    path('register/', views.register, name='register'),
    path('admin/', views.Customadmin, name='admin'),
    path('eachform/<int:form_id>', views.eachform, name='eachform'),
]