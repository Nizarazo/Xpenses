from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

from . import forms

def send_feedback_email(data):
    send_mail(
        "Feedback from: {}".format(data['name']),
        data['content'],
        data['email'],
        settings.MANAGERS
    )


def feedback_view(request):
    if request.method == "POST":
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            send_feedback_email(form.cleaned_data)
            messages.success(request, "Feedback sent.")
            return redirect("expenses:list")
    else:
        form = forms.FeedbackForm()

    return render(request, 'feedback/feedback_form.html', {
        'form': form,
    })
