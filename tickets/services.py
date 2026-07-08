def _classify_by_keywords(text: str) -> str:
    text_lower = text.lower()
    if any(word in text_lower for word in ["оплат", "деньги", "карта", "счёт"]):
        return "оплата"
    if any(word in text_lower for word in ["не работает", "ошибк", "баг", "crash"]):
        return "ошибка"
    if any(word in text_lower for word in ["хочу", "добавьте", "сделайте", "фич"]):
        return "фича"
    if any(word in text_lower for word in ["вход", "пароль", "аккаунт", "логин"]):
        return "аккаунт"
    return "другое"

def _generate_draft_response(category: str, title: str, description: str) -> str:
    templates = {
        "оплата": f"Здравствуйте! Мы получили вашу заявку по теме «{title}». Проверим статус платежа и вернёмся к вам в течение 24 часов.",
        "ошибка": f"Спасибо за сообщение об ошибке в заявке «{title}». Мы уже передали информацию команде разработки. Ориентировочный срок исправления — 3 рабочих дня.",
        "фича": f"Благодарим за предложение по заявке «{title}»! Это интересная идея. Мы добавим её в бэклог и оценим сроки реализации.",
        "аккаунт": f"По вопросу аккаунта в заявке «{title}»: пожалуйста, уточните email или логин, чтобы мы могли быстрее помочь.",
        "другое": f"Мы получили ваше обращение «{title}». Сейчас изучаем ситуацию и скоро вернёмся с ответом.",
    }
    return templates.get(category, templates["другое"])

def classify_and_generate_response(title: str, description: str):
    category = _classify_by_keywords(description or title)
    draft = _generate_draft_response(category, title, description or "")
    return category, draft
