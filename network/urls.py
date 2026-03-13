from rest_framework.routers import DefaultRouter
from network.views import ElectroRetailNetworkViewSet


router = DefaultRouter()
router.register(r'network', ElectroRetailNetworkViewSet, basename='network')

urlpatterns = router.urls
