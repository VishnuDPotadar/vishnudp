from django.urls import path,include


urlpatterns = [
    path('hospital/',include('doctorapp.urls')),
]