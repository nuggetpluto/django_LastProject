from django.shortcuts import render, redirect
from .models import Buyer, Game
from .forms import UserRegisterForm
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)


# Главная страница
def platform_view(request):
    logging.info('Главная страница загружается')
    return render(request, 'fourth_task/platform.html')


# Список игр с использованием QuerySet
def games_view(request):
    logging.info('Загружается список игр')
    games = Game.objects.all()  # Получаем все игры из базы данных
    return render(request, 'fourth_task/games.html', {'games': games})


# Корзина
def cart_view(request):
    logging.info('Загружается корзина')
    return render(request, 'fourth_task/cart.html')


# Регистрация с использованием QuerySet
def sign_up_by_html(request):
    logging.info('Загружается страница регистрации')
    info = {}
    if request.method == "POST":
        logging.info('Обрабатывается POST запрос')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        # Проверки
        if password != repeat_password:
            logging.info('Пароли не совпадают')
            info['error'] = 'Пароли не совпадают.'
        elif Buyer.objects.filter(name=username).exists():
            logging.info('Пользователь уже существует')
            info['error'] = 'Пользователь уже существует.'
        else:
            logging.info('Создание нового пользователя')
            Buyer.objects.create(name=username, age=age, balance=0.0)
            return redirect('platform_view')

    form = UserRegisterForm()
    return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info})
