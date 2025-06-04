import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kr2.settings')
django.setup()

from myApp.models import Shop


def load_flower_shop_data():
    print("Начало загрузки данных мебельного салона...")

    shop_data = {
        "name": "Arredare moderno",
        "tagline": "Салон дизайнерской мебели",
        "description": "Мы предлагаем широкий ассортимент стильной и функциональной мебели из высококачественных матеарилов. Наш интернет-магазин – это место, где вы найдете идеальные решения для обустройства гостиной, кухни, спальни, офиса и других помещений.",
        "delivery_info": "В нашем магазине есть доставка по всему СНГ",
        "image": "background.jpg"
    }


    static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'kr2', 'myApp', 'static')

    try:
        shop = Shop(
            name=shop_data['name'],
            tagline=shop_data['tagline'],
            description=shop_data['description'],
            delivery_info=shop_data['delivery_info']
        )

        image_path = os.path.join(static_dir, shop_data['image'])
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                shop.main_image.save(shop_data['image'], File(f))
            shop.save()
            print(f"Успешно создан магазин: {shop.name}")
        else:
            print(f"Ошибка: файл {shop_data['image']} не найден в {static_dir}")
            return

    except Exception as e:
        print(f"Ошибка при создании магазина: {str(e)}")
        return

    print("Данные успешно загружены!")


if __name__ == '__main__':
    load_flower_shop_data()