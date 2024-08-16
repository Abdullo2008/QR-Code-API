from django.urls import path
from .views import *


urlpatterns = [
    path('', create_qr),

    # path('qr', my_view)
]
