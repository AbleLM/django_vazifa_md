from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.contact_form, name="contact_form"),
    path("xabarlar", views.message_list, name="message_list"),
    path("xabarlar/", views.message_list),
]
