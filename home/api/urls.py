from django.urls import path
from .views import *

urlpatterns = [
    path('list/',BlogListAPIView.as_view(),name="api-list"),
    path('update/<pk>',BlogUpdateAPIView.as_view(),name='update'),
    path('create/',BlogCreateAPIView.as_view(),name='create'),
    path('destroy/<pk>',BlogDestroyAPIView.as_view(),name='destroy'),
    path('retrieve/<pk>',BlogRetrieveAPIView.as_view(),name='retrieve'),
]
