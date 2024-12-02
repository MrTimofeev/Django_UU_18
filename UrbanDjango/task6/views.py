from django.shortcuts import render
from .models import Buyer, Game

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