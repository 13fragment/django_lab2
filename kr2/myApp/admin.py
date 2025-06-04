from django.contrib import admin
from .models import Furniture, Order, Student, Classmate, Teacher, Shop, AboutSection, ShopInfo

# Файл регистрирующий модели

admin.site.register(Furniture)
admin.site.register(Order)
admin.site.register(Student)
admin.site.register(Classmate)
admin.site.register(Teacher)
admin.site.register(Shop)
admin.site.register(AboutSection)
admin.site.register(ShopInfo)