from django.urls import path, include
from django.urls.conf import include

urlpatterns = [
    path('curd2', include('owners.urls'))
]