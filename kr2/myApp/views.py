# Create your views here.
import re

from django.shortcuts import render, redirect
from .models import Furniture, Order, Student, Classmate,Teacher, Shop, ShopInfo
from django.db.models import Sum, Avg, Count, Max
from django.contrib import messages

def home(request):
    shop = Shop.objects.first()
    return render(request, 'home.html', {'shop': shop})

def catalogue(request):
    furniture = Furniture.objects.all()

    search_query = request.GET.get('search', '')
    if search_query:
        furniture = furniture.filter(name__icontains=search_query)

    sort_by = request.GET.get('sort', '')
    print(f"Sort by: {sort_by}")

    if sort_by == 'name_asc':
        furniture = furniture.order_by('name')
    elif sort_by == 'name_desc':
        furniture = furniture.order_by('-name')
    elif sort_by == 'price_asc':
        furniture = furniture.order_by('price')
    elif sort_by == 'price_desc':
        furniture = furniture.order_by('-price')

    context = {
        'furniture': furniture,
        'search_query': search_query,
        'current_sort': sort_by,
    }
    return render(request, "catalogue.html", context)


def contacts(request):
    shop_info = ShopInfo.objects.first()
    furniture_items = Furniture.objects.all()
    search_query = request.GET.get('search', '').strip()
    client_orders = None
    expensive_order = None
    cheap_order = None

    if search_query:
        client_orders = Order.objects.filter(
            last_name__icontains=search_query
        ).order_by('-created_at')

        if client_orders.exists():
            expensive_order = client_orders.order_by('-price').first()
            cheap_order = client_orders.order_by('price').first()

            show_option = request.GET.get('show')
            if show_option == 'expensive':
                client_orders = [expensive_order]
            elif show_option == 'cheap':
                client_orders = [cheap_order]

    if request.method == 'POST':
        try:
            last_name = request.POST.get('last_name', '').strip()
            first_name = request.POST.get('first_name', '').strip()
            phone = request.POST.get('phone', '').strip()
            furniture_id = request.POST.get('furniture')
            comment = request.POST.get('comment', '').strip()

            errors = []

            if not last_name:
                errors.append('Фамилия обязательна для заполнения')
            elif not re.fullmatch(r'[А-ЯЁ][А-Яа-яЁё\s\-]*', last_name):
                errors.append('Фамилия должна начинаться с заглавной буквы')

            if not first_name:
                errors.append('Имя обязательно для заполнения')
            elif not re.fullmatch(r'[А-ЯЁ][А-Яа-яЁё\s\-]*', first_name):
                errors.append('Имя должно начинаться с заглавной буквы')

            if not phone:
                errors.append('Телефон обязателен для заполнения')
            else:
                phone_digits = re.sub(r'\D', '', phone)
                if phone_digits.startswith('8'):
                    phone_digits = '7' + phone_digits[1:]
                if not phone_digits.startswith('7'):
                    errors.append('Телефон должен начинаться с +7')
                elif len(phone_digits) != 11:
                    errors.append('Номер телефона должен содержать 11 цифр')
                else:
                    phone = f"+7({phone_digits[1:4]}){phone_digits[4:7]}-{phone_digits[7:9]}-{phone_digits[9:11]}"

            if not furniture_id:
                errors.append('Необходимо выбрать мебель')

            if errors:
                for error in errors:
                    messages.error(request, error)
            else:
                furniture = Furniture.objects.get(id=furniture_id)
                Order.objects.create(
                    last_name=last_name.capitalize(),
                    first_name=first_name.capitalize(),
                    phone=phone,
                    furniture=furniture,
                    comment=comment,
                    price=furniture.price
                )
                messages.success(request, 'Ваш заказ успешно оформлен!')
                return redirect(request.path)

        except Furniture.DoesNotExist:
            messages.error(request, 'Выбранная мебель не найдена')
        except Exception as e:
            messages.error(request, f'Произошла ошибка: {str(e)}')
        return redirect(request.path)

    # Статистика заказов
    order_stats = Order.objects.aggregate(
        total_orders=Count('id'),
        total_revenue=Sum('price'),
        avg_order=Avg('price'),
        max_order=Max('price'),
        # min_order=Min('price')
    )

    # Популярная мебель
    popular_furniture = Furniture.objects.annotate(
        order_count=Count('order')
    ).order_by('-order_count')[:5]

    # Последние заказы
    recent_orders = Order.objects.select_related('furniture').order_by('-created_at')[:10]

    context = {
        'shop_info': shop_info,
        'furniture': furniture_items,
        'recent_orders': recent_orders,
        'order_stats': order_stats,
        'popular_furniture': popular_furniture,
        'search_query': search_query,
        'client_orders': client_orders,
        'expensive_order': expensive_order,
        'cheap_order': cheap_order
    }

    return render(request, 'contacts.html', context)


def about(request):
    student = Student.objects.first()
    teachers = Teacher.objects.all()
    classmates = Classmate.objects.filter(student=student)

    name_filter = request.GET.get('name')
    sort_by = request.GET.get('sort')

    if name_filter:
        teachers = teachers.filter(name__icontains=name_filter)
        classmates = classmates.filter(name__icontains=name_filter)

    if sort_by:
        teachers = teachers.order_by(sort_by)
        classmates = classmates.order_by(sort_by)

    context = {
        "student": student,
        "teachers": teachers,
        "classmates": classmates,
        "filters": {
            "name": name_filter or '',
            "sort": sort_by or ''
        }
    }

    return render(request, "about.html", context)