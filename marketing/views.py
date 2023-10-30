from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required

from .models import SubscribedUsers

import logging
import hashlib

from kaberg_design import settings
from marketing.forms import SubscribeForm

from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

# logger = logging.getLogger(__name__)

# mailchimp = Client()
# api_key = settings.MAILCHIMP_API_KEY
# server = settings.MAILCHIMP_DATA_CENTER
# list_id = settings.MAILCHIMP_AUDIENCE_ID


def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "You must input a proper email to subscribe")
            return redirect("home")

        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"There is a registered user with {email}. You must login to subscribe or unsubscribe.")
            return redirect("home") 

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already on our list of subscribers.")
            return redirect('home')  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("home")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} was used to subscribe to our newsletter!')
        return redirect("home")
    template = 'marketing/subscribe.html'
    return render(request, template)

@login_required
def unsubscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "You must input a proper name and email to unsubscribe")
            return redirect("home")

        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"There is a registered user with {email}. You must login to subscribe or unsubscribe.")
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

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.email = email
        subscribe_model_instance.email.delete()
        messages.success(request, f'{email} will no longer receive our newsletters')
        return redirect("home")
    template = 'marketing/unsubscribe.html'
    return render(request, template)

# def mailchimp_ping(request):
#     response = mailchimp.ping.get()
#     return JsonResponse(response)


# def subscribe(request):
#     if request.method == 'POST':
#         form = SubscribeForm(request.POST)
#         if form.is_valid():
#             try:
#                 mailchimp = Client()
#                 mailchimp.set_config({
#     "api_key": api_key,
#     "server": server})
#                 form_email = form.cleaned_data['email']
#                 member_info = {
#                     'email_address': form_email,
#                     'status': 'subscribed',
#                 }
#                 response = mailchimp.lists.add_list_member(
#                     list_id,
#                     member_info,
#                 )
#                 logger.info(f'API call successful: {response}')
#                 return redirect('home')

#             except ApiClientError as error:
#                 logger.error(f'An exception occurred: {error.text}')
#                 messages.error(
#                 request,
#                 'There was an error processing your request')
#                 return redirect('home')
#     template = 'marketing/subscribe.html'
#     context = {'form': SubscribeForm()}
#     return render(request, template, context)


# def unsubscribe(request):
#     if request.method == 'POST':
#         form = SubscribeForm(request.POST)
#         if form.is_valid():
#             try:
#                 form_email = form.cleaned_data['email']
#                 form_email_hash = hashlib.md5(form_email.encode('utf-8').lower()).hexdigest()
#                 member_update = {
#                     'status': 'unsubscribed',
#                 }
#                 response = mailchimp.lists.update_list_member(
#                     settings.MAILCHIMP_AUDIENCE_ID,
#                     form_email_hash,
#                     member_update,
#                 )
#                 logger.info(f'API call successful: {response}')
#                 messages.success(
#                 request,
#                 'You have successfully unsubscribed!')
#                 return redirect('home')

#             except ApiClientError as error:
#                 logger.error(f'An exception occurred: {error.text}')
#                 messages.error(
#                 request,
#                 'There was an error processing your request')
#                 return redirect('unsubscribe-fail')
#     template = 'marketing/unsubscribe.html'
#     return render(request, template, {
#         'form': SubscribeForm(),
#     })