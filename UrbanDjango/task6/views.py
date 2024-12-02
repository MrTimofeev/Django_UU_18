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

def create_records(request):
    # Создаем покупателей
    buyer1 = Buyer.objects.create(name="John Doe", balance=100.00, age=25)
    buyer2 = Buyer.objects.create(name="Jane Smith", balance=200.00, age=30)
    buyer3 = Buyer.objects.create(name="Alice Johnson", balance=150.00, age=17)  # Младше 18

    # Создаем игры
    game1 = Game.objects.create(title="Game 1", cost=50.00, size=5.0, description="Description 1", age_limited=True)
    game2 = Game.objects.create(title="Game 2", cost=30.00, size=3.0, description="Description 2", age_limited=False)
    game3 = Game.objects.create(title="Game 3", cost=40.00, size=4.0, description="Description 3", age_limited=True)

    # Связываем покупателей с играми
    game1.buyer.set([buyer1, buyer2])
    game2.buyer.set([buyer1, buyer2, buyer3])
    game3.buyer.set([buyer1, buyer2])

    return render(request, 'task6/records_created.html')

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
                return render(request, 'fifth_task/registration_page.html', {'success': f'Приветствуем, {username}!'})
        else:
            info['error'] = 'Форма не валидна'
    else:
        form = UserRegisterForm()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

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
            return render(request, 'fifth_task/registration_page.html', {'success': f'Приветствуем, {username}!'})

    return render(request, 'fifth_task/registration_page.html', info)