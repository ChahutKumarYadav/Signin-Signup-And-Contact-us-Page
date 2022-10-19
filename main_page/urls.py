from .views import SignUpFormView,Login,home,Contact
from django.urls import path
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('register/', SignUpFormView.as_view(), name='register'),
    path('', Login, name='login'),
    path('home/', home, name='home'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('contact/',Contact, name='contact'),
]
