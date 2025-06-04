import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kr2.settings')
django.setup()

from myApp.models import Furniture


def create_furniture():
    furniture_data = [
        {"name": "ROCK TABLE MINI", "price": 30000, "image": "catalogue1.jpg"},
        {"name": "ROCK TABLE MAXI", "price": 50000, "image": "catalogue2.jpg"},
        {"name": "FRAMMENTI", "price": 25000, "image": "catalogue3.jpg"},
        {"name": "TATAMI", "price": 27000, "image": "catalogue4.jpg"},
        {"name": "UNIVERSAL COLLECTION", "price": 21000, "image": "catalogue5.jpg"},
        {"name": "COSY ISLAND", "price": 200000, "image": "catalogue6.jpg"},
        {"name": "COSY CURVE", "price": 180000, "image": "catalogue7.jpg"},
        {"name": "NEIL DENIM CHAIR'", "price": 16200, "image": "catalogue8.jpg"},
        {"name": "NVL TABLE", "price": 58500, "image": "catalogue9.jpg"},
    ]

    static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'kr2', 'myApp', 'static')

    for data in furniture_data:
        try:
            furniture = Furniture(
                name=data['name'],
                price=data['price']
            )

            image_path = os.path.join(static_dir, data['image'])

            if os.path.exists(image_path):
                with open(image_path, 'rb') as f:
                    furniture.image.save(data['image'], File(f))
                furniture.save()
                print(f"Успешно создан букет: {furniture.name}")
            else:
                print(f"Ошибка: файл {data['image']} не найден в {static_dir}")
        except Exception as e:
            print(f"Ошибка при создании букета {data['name']}: {str(e)}")


if __name__ == '__main__':
    print("Начало заполнения базы данных...")
    create_furniture()
    print("Заполнение завершено!")