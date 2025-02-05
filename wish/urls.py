from django.urls import path
from django.conf import settings
from .views import *

app_name = 'wish'

urlpatterns=[
  path('items/<int:item_id>/', WishItemView.as_view()),
  path('items/<int:user_id>/<int:item_id>/gifts/', SendView.as_view()),
  path('<int:user_id>/', WishView.as_view()),
  path('tomywish/<int:item_id>/', ToMyWishView.as_view()),
  
]           