from django.shortcuts import render

def home_view(request):
    return render(request, 'third_task/home.html')

def shop_view(request):
    items = [
        "Игра 1",
        "Игра 2",
        "Игра 3",
    ]
    return render(request, 'third_task/shop.html', {'items': items})

def cart_view(request):
    return render(request, 'third_task/cart.html')