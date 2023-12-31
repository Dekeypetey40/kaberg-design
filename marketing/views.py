from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from .models import SubscribedUsers


from kaberg_design import settings
from marketing.forms import SubscribeForm


def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "You must input a\
                proper email to subscribe")
            return redirect("home")

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("home")

        subscription = SubscribedUsers.objects.filter(email=email)
        if subscription.exists():
            messages.error(request, f" The email address, {email}, is already\
                           subscribed to our newsletter. You have\
                           been redirected to the unsubscribe page")
            return redirect("unsubscribe")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} was used\
            to subscribe to our newsletter!')
        return redirect("home")
    template = 'marketing/subscribe.html'
    return render(request, template)


def unsubscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "You must input a proper\
                name and email to unsubscribe")
            return redirect("home")

        unsubscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if not unsubscribe_user:
            messages.error(request, f"{email} is not on our list.")
            return redirect('home')

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("home")

        subscribe_model_instance = get_object_or_404(SubscribedUsers, email=email)  # noqa
        subscribe_model_instance.delete()
        messages.success(request, f'{email} will\
            no longer receive our newsletters')
        return redirect("home")
    template = 'marketing/unsubscribe.html'
    return render(request, template)
