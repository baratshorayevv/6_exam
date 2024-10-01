from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('detail/<int:_id>/', views.detail_page, name='detail'),
    path('products/', views.all_products, name='all_products'),
    path('popular/', views.popular_items, name='popular_items'),
    path('new-arrivals/', views.new_arrivals, name='new_arrivals'),
    path('register/', views.register, name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('products/search/', views.product_search, name='product_search'),
]
