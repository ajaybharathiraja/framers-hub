from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.user_login, name='home'),
    path('register/farmer/', views.register_farmer, name='register_farmer'),
    path('register/customer/', views.register_customer, name='register_customer'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('farmer/dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('customer/dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('farmer/products/', views.farmer_products, name='farmer_products'),
    path('farmer/products/add/', views.farmer_add_product, name='farmer_add_product'),
    path('farmer/products/<int:listing_id>/pricing/', views.farmer_set_pricing, name='farmer_set_pricing'),
    path('farmer/crop-recommendation/', views.crop_recommendation_view, name='crop_recommendation_view'),
    path('farmer/dynamic-pricing/', views.dynamic_pricing_view, name='dynamic_pricing_view'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('marketplace/product/<int:pk>/', views.product_details, name='product_details'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:listing_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='order_history'),
    path('orders/update/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('survey/', views.tam_survey_view, name='tam_survey_view'),
    
    # API endpoints
    path('api/market-intelligence/', api.market_intelligence_api, name='api_market_intelligence'),
    path('api/crop-recommendation/', api.crop_recommendation_api, name='api_crop_recommendation'),
]
