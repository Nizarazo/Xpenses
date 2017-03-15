from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings


def send_feedback_email(data):
    send_mail(
        "Feedback from: {}".format(data['name']),
        data['content'],
        data['email'],
        settings.MANAGERS
    )


def feedback_view(request):
    if request.method == "POST":
        # TODO: validate?
        # TODO: what to do if invalid???
        # assume POST data is valid:
        # assert False, request.POST
        send_feedback_email(request.POST)
        # TODO: now what?
        assert False, "OK"

    return render(request, 'feedback/feedback_form.html')

