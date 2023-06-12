from django.shortcuts import render, redirect
from . import models
from . import handlers

from django.http import HttpResponse


# Create your views here.

def main_page(request):
    # получаем все данные о категориях из базы
    all_categories = models.Category.objects.all()
    all_products = models.Product.objects.all()

    # получить переменную из фронт части, если есть
    search_value_from_front = request.GET.get('search')
    print(search_value_from_front)
    if search_value_from_front:
        all_products = models.Product.objects.filter(name__contains=search_value_from_front)

    # передача переменных из бэка на фронт
    context = {'all_categories': all_categories, 'all_products': all_products}

    # получить продукты из конкретной категории
    return render(request, 'index.html', context)


def get_category_products(request, pk):
    # получить все товары из конкретной категории
    exact_category_products = models.Product.objects.filter(category_name__id=pk)

    # передача переменных из бэка на фронт

    context = {'category_products': exact_category_products}

    # указать html

    # обработка из html файла
    return render(request, 'category.html', context)


def about_page(request):
    # обработка из html файла
    return render(request, 'category.html')


def settings_page(request):
    return HttpResponse('Page settings')

    # функция получения определенного продукта


def get_exact_product(request, name, pk):
    # находим из баы продукт
    exact_product = models.Product.objects.get(name=name, id=pk)

    # передача переменных из бэка на фронт
    context = {'product': exact_product}

    # вывод html
    return render(request, 'product.html', context)


def add_pr_to_cart(request, pk):
    # получить выбранное количество продукта из фронт части
    quantity = request.POST.get('pr_count')

    # находим сам продукт
    product_to_add = models.Product.objects.get(id=pk)

    # добавление данные
    models.UserCart.objects.create(user_id=request.user.id,
                                   user_product=product_to_add,
                                   user_product_quantity=quantity)

    return redirect('/')


def get_user_cart(request):
    products_from_cart = models.UserCart.objects.filter(user_id=request.user.id)

    context = {'cart_products': products_from_cart}

    return render(request, 'user_cart.html', context)


# оформление заказов

def complete_order(request):
    user_cart = models.UserCart.objects.filter(user_id=request.user.id)

    # собираем сообщение бота для админа
    if request.method == 'POST':
        result_message = 'новый заказ(из сайта)\n\n'
        for cart in user_cart:
            result_message += f'название товара{cart.user_product}\n' \
                              f'количество{cart.user_product_quantity}'
        handlers.bot.send_message(79088303, result_message)
        user_cart.delete()
        return redirect('/')
    return render(request, 'user_cart.html', {'user': user_cart})


#
def delete_from_user_cart(request, pk):
    product_to_delete = models.Product.objects.get
    return redirect('/cart')
