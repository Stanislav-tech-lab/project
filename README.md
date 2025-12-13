
Это Django‑проект с несколькими приложениями:

```
project/
├── authApp/            # регистрация, логин, аутентификация
├── core/               # базовая логика проекта
├── indexApp/           # главная страница
├── payments/           # платежи
├── personalAccount/    # личный кабинет пользователя
├── users/              # пользовательская модель
├── manage.py
├── requirements.txt
└── README.md
```

Рабочая ветка: **settings-page**

---



## 📥 Клонирование проекта

1. Создайте папку, например:

```
C:\projects
```

2. Откройте её

3. **Shift + ПКМ → Открыть терминал**

4. Выполните:

```bash
git clone https://github.com/Stanislav-tech-lab/project.git
```

5. Перейдите в проект:

```bash
cd project
```

6. Переключитесь на нужную ветку:

```bash
git checkout settings-page
```

---

## 🖥️ Открытие проекта в VS Code

В папке `project` выполните:

```bash
code .
```

---

## 🧪 Виртуальное окружение (ОБЯЗАТЕЛЬНО)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Если в терминале появилось `(venv)` — всё ок ✅

---

## 📦 Установка зависимостей

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Если будет ошибка с изображениями:

```bash
pip install pillow
```

---

## ⚙️ Подготовка базы данных

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Создание администратора (рекомендуется)

```bash
python manage.py createsuperuser
```

Введите логин / email и пароль.

---

## ▶️ Запуск сервера

```bash
python manage.py runserver
```

Если видите:

```
Starting development server at http://127.0.0.1:8000/
```

🎉 **Проект успешно запущен!**

---

## 🌐 Доступные страницы

* Главная:

```
http://127.0.0.1:8000/
```

* Админ‑панель:

```
http://127.0.0.1:8000/admin/
```

* Личный кабинет:

```
http://127.0.0.1:8000/personalAccount/
```

---

## ⛔ Частые проблемы

### Python не найден

➡️ Переустановите Python с галочкой **Add Python to PATH**

---

### pip не работает

```bash
python -m ensurepip --upgrade
```

---

### Ошибка ImageField / Pillow

```bash
pip install pillow
```

---

## 🛑 Остановка сервера

```text
CTRL + C
```

---

## ❤️ Итог

Если вы читаете это — **вы смогли запустить Django‑проект**, даже если сделали это **впервые в жизни** 🔥

Удачной разработки 🚀
