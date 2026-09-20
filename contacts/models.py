from django.core.validators import RegexValidator
from django.db import models


phone_validator = RegexValidator(
    regex=r"^\+?[0-9][0-9\s\-()]{6,19}$",
    message="Telefon raqamini to‘g‘ri kiriting. Masalan: +998901234567",
)


class ContactMessage(models.Model):
    first_name = models.CharField("Ism", max_length=100)
    last_name = models.CharField("Familiya", max_length=100)
    phone = models.CharField("Telefon raqam", max_length=20, validators=[phone_validator])
    email = models.EmailField("Email manzil")
    message = models.TextField("Yuborilgan xabar", max_length=2000)
    created_at = models.DateTimeField("Yuborilgan vaqt", auto_now_add=True)

    class Meta:
        ordering = ["-created_at", "-id"]
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.email}"
