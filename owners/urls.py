from django.urls import path
from owners.views import OwnersView,DogsView

from django.urls.conf import include

urlpatterns = [
    path('/owners', OwnersView.as_view()),
    path('/dogs', DogsView.as_view())
]