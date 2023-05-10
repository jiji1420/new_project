from django.urls import path, include
from .views import ProductView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductView)


urlpatterns =[
    path('', include(router.urls)),
]