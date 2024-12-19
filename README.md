# **Service Desk**

Service Desk — это веб-приложение для обработки пользовательских обращений. Оно фиксирует обращения в базе данных, предоставляет возможность операторам принимать обращения, отвечать на них, а также закрывать их. Пользователи получают уведомления о статусе их обращений через email.

---

## **Функциональность**

### **Для пользователей**
1. Отправка обращения через email.
2. Получение автоответа о принятии обращения.
3. Получение ответа от оператора.
4. Уведомление о закрытии обращения.

### **Для операторов**
1. Просмотр списка обращений с фильтрацией по статусу и сортировкой по времени создания.
2. Назначение обращения на себя.
3. Ответ пользователю через API с отправкой сообщения на email.
4. Закрытие обращения.

---

## **Стек технологий**

- **Язык программирования**: Python 3.10+
- **Веб-фреймворк**: FastAPI
- **База данных**: PostgreSQL
- **ORM**: SQLAlchemy (async)
- **Миграции**: Alembic
- **Тестирование**: Pytest
- **Email-уведомления**: smtplib

---

## **Как запустить проект**

### **1. Клонирование репозитория**
```bash
git clone https://github.com/PoroSenok-sys/Service-Desk.git
cd Service-Desk
```

### **2. Установка зависимостей**
Создайте виртуальное окружение и установите зависимости:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### **3. Настройка переменных окружения**
Создайте файл `.env` в корне проекта и добавьте следующие переменные:
```env
DB_HOST=you_DB_HOST
DB_PORT=you_DB_PORT
DB_USER=you_DB_USER
DB_PASS=you_DB_PASS
DB_NAME=you_DB_NAME
SERVICE_EMAIL=you_SERVICE_EMAIL
```

### **4. Локальный запуск**
Если хотите запустить приложение локально:
1. Убедитесь, что PostgreSQL запущен и настроен.
2. Выполните миграции:
   ```bash
   alembic upgrade head
   ```
3. Запустите сервер:
   ```bash
   uvicorn src.main:app --reload
   ```

Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000).

---

## **Как запустить тесты**

1. Убедитесь, что база данных настроена для тестов.
2. Запустите тесты с помощью `pytest`:
   ```bash
   pytest
   ```

---

## **Документация API**

Документация доступна по адресу: [http://localhost:8000/docs](http://localhost:8000/docs).
