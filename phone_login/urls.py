from django.conf.urls import url

from .views import GenerateOTP, ValidateOTP,CreateOTP

urlpatterns = [
    url(r'^generate/$', GenerateOTP.as_view(), name="generate"),
    url(r'^validate/$', ValidateOTP.as_view(), name="validate"),
    url(r'^create/$', CreateOTP.as_view(), name="create"),
]
