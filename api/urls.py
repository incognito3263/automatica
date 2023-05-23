from rest_framework import routers
from api.views import MainViewset


router = routers.SimpleRouter()
router.register(r'main', MainViewset)
urlpatterns = router.urls