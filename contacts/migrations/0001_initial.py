# Generated for the Contact Form assignment
from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=100, verbose_name="Ism")),
                ("last_name", models.CharField(max_length=100, verbose_name="Familiya")),
                ("phone", models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Telefon raqamini to‘g‘ri kiriting. Masalan: +998901234567", regex=r"^\+?[0-9][0-9\s\-()]{6,19}$")], verbose_name="Telefon raqam")),
                ("email", models.EmailField(max_length=254, verbose_name="Email manzil")),
                ("message", models.TextField(max_length=2000, verbose_name="Yuborilgan xabar")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")),
            ],
            options={
                "verbose_name": "Xabar",
                "verbose_name_plural": "Xabarlar",
                "ordering": ["-created_at", "-id"],
            },
        ),
    ]
