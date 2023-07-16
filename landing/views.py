"""
    Цей файл містить визначення класу "Index", який є класом перегляду
    (View) у фреймворку Django. Клас "Index" відповідає за обробку
    HTTP-запитів і повернення відповіді для сторінки "index.html".
"""

from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self, request, *args, **kwargs):
        """
            Обробка GET-запиту для сторінки "index.html".

            Параметри:
            - request: об'єкт, що містить дані про HTTP-запит

            Повертає:
            - Відповідь у вигляді рендерингу шаблону "index.html"
        """
        return render(request, 'landing/index.html')
