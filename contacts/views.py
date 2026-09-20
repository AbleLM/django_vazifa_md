from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactMessageForm
from .models import ContactMessage


def contact_form(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz muvaffaqiyatli saqlandi.")
            return redirect("contacts:message_list")
    else:
        form = ContactMessageForm()

    return render(request, "contacts/contact_form.html", {"form": form})


def message_list(request):
    contact_messages = ContactMessage.objects.all()
    return render(
        request,
        "contacts/message_list.html",
        {"contact_messages": contact_messages},
    )
