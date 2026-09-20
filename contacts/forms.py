from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["first_name", "last_name", "phone", "email", "message"]
        error_messages = {
            "email": {"invalid": "To‘g‘ri email manzil kiriting."},
            "phone": {"invalid": "Telefon raqamini to‘g‘ri kiriting."},
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Ismingiz", "autocomplete": "given-name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Familiyangiz", "autocomplete": "family-name"}),
            "phone": forms.TextInput(attrs={"placeholder": "+998 90 123 45 67", "autocomplete": "tel"}),
            "email": forms.EmailInput(attrs={"placeholder": "siz@example.com", "autocomplete": "email"}),
            "message": forms.Textarea(attrs={"placeholder": "Xabaringizni yozing...", "rows": 6}),
        }

    def clean_first_name(self):
        value = self.cleaned_data["first_name"].strip()
        if len(value) < 2:
            raise forms.ValidationError("Ism kamida 2 ta belgidan iborat bo‘lsin.")
        return value

    def clean_last_name(self):
        value = self.cleaned_data["last_name"].strip()
        if len(value) < 2:
            raise forms.ValidationError("Familiya kamida 2 ta belgidan iborat bo‘lsin.")
        return value

    def clean_message(self):
        value = self.cleaned_data["message"].strip()
        if len(value) < 3:
            raise forms.ValidationError("Xabar juda qisqa.")
        return value
