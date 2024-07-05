from django.urls import path

from .views import Register



# register endpoint = api/users/register/
urlpatterns = [
    path('register/', Register.as_view()),
]