from django.urls import path
from App import views

urlpatterns = [
    path("", views.ContactView.as_view(), name="Login"),
    path('#ContactMe/', views.ContactView.as_view(), name='contact'),  # Updated URL pattern
]
