from django.urls import path
from . import views

urlpatterns = [
    path('', views.platform_view, name='platform_view'),  # Главная страница
    path('games/', views.games_view, name='games_view'),  # Список игр
    path('cart/', views.cart_view, name='cart_view'),     # Корзина
    path('register/', views.sign_up_by_html, name='sign_up_by_html'),  # Регистрация
]
