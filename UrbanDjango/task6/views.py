from django.shortcuts import render
from .models import Buyer, Game
from .forms import UserRegisterForm


def home_view(request):
    return render(request, 'task6/home.html')


def shop_view(request):
    games = Game.objects.all()
    return render(request, 'task6/shop.html', {'games': games})


def cart_view(request):
    return render(request, 'task6/cart.html')


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, balance=0.00, age=age)
                return render(request, 'task6/registration_page.html', {'success': f'Приветствуем, {username}!'})
        else:
            info['error'] = 'Форма не валидна'
    else:
        form = UserRegisterForm()

    info['form'] = form
    return render(request, 'task6/registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif Buyer.objects.filter(name=username).exists():
            info['error'] = 'Пользователь уже существует'
        else:
            Buyer.objects.create(name=username, balance=0.00, age=age)
            return render(request, 'task6/registration_page.html', {'success': f'Приветствуем, {username}!'})

    return render(request, 'task6/registration_page.html', info)


def create_records(request):
    # Создаем покупателей
    buyer1 = Buyer.objects.create(name="John Doe", balance=100.00, age=25)
    buyer2 = Buyer.objects.create(name="Jane Smith", balance=200.00, age=30)
    buyer3 = Buyer.objects.create(name="Alice Johnson", balance=150.00, age=17)

    # Проверка создания покупателей
    print(f"Buyer 1: {buyer1}")
    print(f"Buyer 2: {buyer2}")
    print(f"Buyer 3: {buyer3}")

    # Создаем игры
    game1 = Game.objects.create(
        title="Game 1", cost=50.00, size=5.0, description="Description 1", age_limited=True)
    game2 = Game.objects.create(
        title="Game 2", cost=30.00, size=3.0, description="Description 2", age_limited=False)
    game3 = Game.objects.create(
        title="Game 3", cost=40.00, size=4.0, description="Description 3", age_limited=True)

    # Связываем покупателей с играми
    game1.buyer.set([buyer1, buyer2])
    game2.buyer.set([buyer1, buyer2, buyer3])
    game3.buyer.set([buyer1, buyer2])

    # Изменение элемента в базе данных
    game1.title = 'New Title for Game 1'
    game1.save()

    # Получение всех объектов и удаление одного из них
    all_buyers = Buyer.objects.all()
    all_games = Game.objects.all()

    if all_buyers.exists():
        buyer2.delete()

    # Фильтрация объектов в базе данных
    young_buyers = Buyer.objects.filter(age__lt=18)
    age_limited_games = Game.objects.filter(age_limited=True)

    context = {
        'young_buyers': young_buyers,
        'age_limited_games': age_limited_games,
    }

    return render(request, 'task6/records_created.html', context)

# Это чисто для удобства))


def clear_database(request):
    Buyer.objects.all().delete()
    Game.objects.all().delete()
    return render(request, 'task6/database_cleared.html')
