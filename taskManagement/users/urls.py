from rest_framework.routers import DefaultRouter
from .views import UserModelView, AuthenticateView
from django.urls import path

router= DefaultRouter()
router.register(r'users', UserModelView)

urlpatterns= [
#custom_login es el nombre asignado a la url
    path(r'login', AuthenticateView.as_view(), name='custom_login'),
    *router.urls
]