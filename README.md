# Contact Form — Django

Mohirdev vazifasi uchun tayyor Django loyiha.

## Imkoniyatlar

- `/` — ism, familiya, telefon, email va xabar maydonlari bo‘lgan forma.
- Forma `POST` orqali yuboriladi.
- To‘g‘ri ma’lumotlar SQLite bazasiga saqlanadi.
- Saqlangandan keyin `/xabarlar` sahifasiga yo‘naltiradi.
- `/xabarlar` — barcha xabarlarni jadval ko‘rinishida chiqaradi.
- Django admin orqali xabarlarni ko‘rish mumkin.
- Server-side validation va CSRF himoyasi mavjud.
- Responsive CSS dizayn.
- Avtomatik testlar mavjud.

## Windows’da ishga tushirish

```bat
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Brauzerda:

- Forma: http://127.0.0.1:8000/
- Xabarlar: http://127.0.0.1:8000/xabarlar

## Testlarni ishga tushirish

```bat
python manage.py test
```

## Admin (ixtiyoriy)

```bat
python manage.py createsuperuser
python manage.py runserver
```

Keyin: http://127.0.0.1:8000/admin/

## GitHub’ga yuklash

```bat
git init
git add .
git commit -m "Complete Django contact form assignment"
git branch -M main
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git push -u origin main
```
