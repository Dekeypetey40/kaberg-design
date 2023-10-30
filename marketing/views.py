from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

import logging
import hashlib

from kaberg_design import settings
from marketing.forms import SubscribeForm

from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

logger = logging.getLogger(__name__)

mailchimp = Client()
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_AUDIENCE_ID


def mailchimp_ping(request):
    response = mailchimp.ping.get()
    return JsonResponse(response)


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            try:
                mailchimp = Client()
                mailchimp.set_config({
    "api_key": api_key,
    "server": server})
                form_email = form.cleaned_data['email']
                member_info = {
                    'email_address': form_email,
                    'status': 'subscribed',
                }
                response = mailchimp.lists.add_list_member(
                    list_id,
                    member_info,
                )
                logger.info(f'API call successful: {response}')
                return redirect('home')

            except ApiClientError as error:
                logger.error(f'An exception occurred: {error.text}')
                messages.error(
                request,
                'There was an error processing your request')
                return redirect('subcribe')
    template = 'marketing/subscribe.html'
    context = {'form': SubscribeForm()}
    return render(request, template, context)


def unsubscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            try:
                form_email = form.cleaned_data['email']
                form_email_hash = hashlib.md5(form_email.encode('utf-8').lower()).hexdigest()
                member_update = {
                    'status': 'unsubscribed',
                }
                response = mailchimp.lists.update_list_member(
                    settings.MAILCHIMP_AUDIENCE_ID,
                    form_email_hash,
                    member_update,
                )
                logger.info(f'API call successful: {response}')
                messages.success(
                request,
                'You have successfully unsubscribed!')
                return redirect('home')

            except ApiClientError as error:
                logger.error(f'An exception occurred: {error.text}')
                messages.error(
                request,
                'There was an error processing your request')
                return redirect('unsubscribe-fail')
    template = 'marketing/unsubscribe.html'
    return render(request, template, {
        'form': SubscribeForm(),
    })