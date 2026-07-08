import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support_system.settings')
django.setup()

from tickets.models import Ticket
from tickets.services import classify_and_generate_response

def run():
    Ticket.objects.all().delete()
    print("База очищена.")

    samples = [
        {"title": "Не работает оплата", "description": "При нажатии кнопки «Оплатить» ничего не происходит."},
        {"title": "Ошибка 500 на главной", "description": "После обновления страницы появляется Internal Server Error."},
        {"title": "Хочу тёмную тему", "description": "Добавьте переключатель на тёмную тему в профиль пользователя."},
        {"title": "Медленная загрузка", "description": "Страница списка товаров грузится больше 5 секунд."},
        {"title": "Баг в корзине", "description": "Товар удаляется из корзины только после перезагрузки страницы."},
    ]

    created_count = 0
    for s in samples:
        category, draft = classify_and_generate_response(s["title"], s["description"])
        Ticket.objects.create(
            title=s["title"],
            description=s["description"],
            status="new",
            category=category,
            draft_response=draft
        )
        created_count += 1

    print(f"Создано {created_count} тестовых заявок с заполненными ИИ‑полями.")

if __name__ == "__main__":
    run()
