from rest_framework import routers 
from .api import UserViewSet

router = routers.DefaultRouter()
router.register('api/user', UserViewSet , 'users')

urlpatterns = router.urls