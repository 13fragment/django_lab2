from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

# Модель это таблица, база данных состоит из таблиц

# models.py Служит для описания архитектуру таблиц базы данных

class Shop(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    description = models.TextField()
    delivery_info = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='shop_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class AboutSection(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='about_sections')

    def __str__(self):
        return self.title

class Furniture(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название мебели")
    image = models.ImageField(upload_to='furniture/', verbose_name="Изображение")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return f"{self.name}"


class ShopInfo(models.Model):
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес")
    working_hours = models.CharField(max_length=100, verbose_name="Режим работы")
    image = models.ImageField(upload_to='shop_images/', verbose_name="Изображение магазина")

    def __str__(self):
        return "Контактная информация магазина"


class Order(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    furniture = models.ForeignKey(Furniture, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], null=True)

    def save(self, *args, **kwargs):
        if self.furniture and not self.price:
            self.price = self.furniture.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заказ #{self.id} - {self.last_name} {self.first_name}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='students/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    program = models.CharField(max_length=100)
    program_description = models.TextField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='teachers/')
    email = models.EmailField()
    subjects = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Classmate(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='classmates/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='classmates')

    def __str__(self):
        return self.name