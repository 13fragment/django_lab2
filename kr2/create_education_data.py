import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kr2.settings')
django.setup()

from myApp.models import Student, Teacher, Classmate


def create_education_data():
    static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'kr2', 'myApp', 'static')

    # student_data = {
    #     "name": "Голубев Максим Вячеславович",
    #     "email": "mvgolubev@edu.hse.ru",
    #     "phone": "+79202998959",
    #     "program": "Бизнес-информатика",
    #     "program_description": """
    #     Бакалаврская программа «Бизнес-информатика» предназначена для выпускников, заинтересованных в таких дисциплинах, как информатика, математика, экономика, менеджмент. Данное направление ориентировано на изучение информационных процессов и связанных с ними явлений в социально-экономической и бизнес сферах. Появление образовательной программы «Бизнес-информатика» обусловлено требованиями российского рынка труда, испытывающего нехватку квалифицированных бизнес-аналитиков, менеджеров, системных аналитиков, системных архитекторов для IT-сферы.
    #     """
    # }

    # try:
    #     student = Student(**student_data)
    #     student_photo_path = os.path.join(static_dir, 'my_photo.jpg')
    #     if os.path.exists(student_photo_path):
    #         with open(student_photo_path, 'rb') as f:
    #             student.photo.save('my_photo.jpg', File(f))
    #     student.save()
    #     print(f"Успешно создан студент: {student.name}")
    # except Exception as e:
    #     print(f"Ошибка при создании студента: {str(e)}")
    #     return

    # teachers_data = [
    #     {
    #         "name": "Улитин Борис Игоревич",
    #         "photo": "ulitin.jpg",
    #         "email": "bulitin@hse.ru",
    #         "subjects": "Информационные системы, Базы данных"
    #     },
    #     {
    #         "name": "Емельянова Мария Максимовна",
    #         "photo": "emelyanova.jpg",
    #         "email": "example@hse.ru",
    #         "subjects": "Экономика, Менеджмент"
    #     }
    # ]

    # for data in teachers_data:
    #     try:
    #         teacher = Teacher(
    #             name=data['name'],
    #             email=data['email'],
    #             subjects=data['subjects']
    #         )
    #         image_path = os.path.join(static_dir, data['photo'])
    #         if os.path.exists(image_path):
    #             with open(image_path, 'rb') as f:
    #                 teacher.photo.save(data['photo'], File(f))
    #         teacher.save()
    #         print(f"Успешно создан преподаватель: {teacher.name}")
    #     except Exception as e:
    #         print(f"Ошибка при создании преподавателя {data['name']}: {str(e)}")

    # Необходимо создать экземлпяр student, так как у нас привыязка по ключу из модели (Foreign key)
    student = Student.objects.get(email="mvgolubev@edu.hse.ru")
    classmates_data = [
        {
            "name": "Заводчиков Никита Александрович",
            "photo": "student3.jpg",
            "email": "nazavodchikov@edu.hse.ru",
            "phone": "+79990771264"
        }
    ]

    for data in classmates_data:
        try:
            classmate = Classmate(
                name=data['name'],
                email=data['email'],
                phone=data['phone'],
                student=student
            )
            image_path = os.path.join(static_dir, data['photo'])
            if os.path.exists(image_path):
                with open(image_path, 'rb') as f:
                    classmate.photo.save(data['photo'], File(f))
            classmate.save()
            print(f"Успешно создан сокурсник: {classmate.name}")
        except Exception as e:
            print(f"Ошибка при создании сокурсника {data['name']}: {str(e)}")


if __name__ == '__main__':
    print("Начало заполнения базы данных...")
    create_education_data()
    print("Заполнение завершено!")