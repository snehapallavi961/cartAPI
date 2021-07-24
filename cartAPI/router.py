from shoppingAPI.viewsets import shoppingcartViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('shopping',shoppingcartViewset)

# localhost:p/api/shopping/5
# GET, POST, PUT, DELETE
# list , retrive