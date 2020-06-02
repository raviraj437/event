from django.urls import path, include
from app import views
from .views import getPhoneNumberRegistered

urlpatterns =[
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    # path('restricted/', views.restricted),
    path("<phone>/", getPhoneNumberRegistered.as_view(), name="OTP Gen"),
]