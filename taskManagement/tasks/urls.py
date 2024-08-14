from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, AreaViewSet


router= DefaultRouter()

router.register(r'areas', AreaViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns= router.urls

