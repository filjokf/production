
from django.urls import path,include
from django.conf.urls import url
from webapp import views
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()

router.register(r'production',productionViewSet)

urlpatterns = [
    path('', views.importexl,name='importexl'),
    path('', include(router.urls)),
    path('webapp-auth/', include('rest_framework.urls'))
    
]