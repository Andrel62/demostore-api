from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import ProductList, CartItemViews

schema_view = get_schema_view(
   openapi.Info(
      title="Store API docs",
      default_version='v1',
      description="display products from store perform CRUD on cart",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="andreldaga61@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns=[
    path('products/', ProductList.as_view(), name="product_list"),
    path('cart-items/', CartItemViews.as_view()),
    path('cart-items/<int:id>', CartItemViews.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
