from django.conf.urls import url
from profile import views

urlpatterns = [
    url(r"^$", views.home, name="home"),
]