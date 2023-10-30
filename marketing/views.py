from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from kaberg_design import settings
from marketing.forms import SubscribeForm

from mailchimp_marketing import Client


mailchimp = Client()
mailchimp.set_config({
  'api_key': settings.MAILCHIMP_API_KEY,
  'server': settings.MAILCHIMP_REGION,
})


def mailchimp_ping(request):
    response = mailchimp.ping.get()
    return JsonResponse(response)


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data['email']
            # TODO: use Mailchimp API to subscribe
            return redirect('subscribe-success')
    template = 'marketing/subscribe.html'
    return render(request, template, {
        'form': SubscribeForm(),
    })


def unsubscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data['email']
            # TODO: use Mailchimp API to unsubscribe
            return redirect('unsubscribe-success')
    template = 'marketing/unsubscribe.html'
    return render(request, template, {
        'form': SubscribeForm(),
    })