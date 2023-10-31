from django.shortcuts import render
from .forms import ContactUsForm
from django.contrib import messages
from django.core.mail import send_mail


def index(request):
    """ View for the home page """

    return render(request, 'home/index.html')


def contact_us(request):
    """
    A view to return the contact us page
    """
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data
            ['message'] + 'Contact Form Submission from {}'.format(name)
            form.save()

            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=email,  # customer's email
                    recipient_list=['kmichaelmikhail@gmail.com'],
                    )
                send_mail(
                    subject=subject,
                    message='Thank you for contacting us,\
                        we will get back to you shortly.',
                    from_email=email,  # customer's email
                    recipient_list=[email],  # Sends to my email
                )
                messages.success(
                    request,
                    'Message sent!')
            except Exception as e:
                messages.error(
                    request,
                    "There was an error sending your message!"
                    )
        else:
            messages.error(
                    request,
                    "There was an error in the form."
                    )
    form = ContactUsForm()
    context = {'form': form}
    template = 'home/contact_us.html'

    return render(request, template, context)
