from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def index(request):
    # return HttpResponse("this is the home page")
    return render(request, 'index.html', {})


def services(request):
    return render(request, 'services.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
            Message: {}
            
            From: {}
        '''.format(contact_data['message'], contact_data['email'])
        send_mail(contact_data['subject'], message, '', ['adaowonsikan69@gmail.com', 'adaowonsikan6952@gmail.com'])
        # recipient emails are stated above
        return HttpResponse('THANK YOU FOR REACHING OUT TO US, we will be in touch soon')

    return render(request, 'contact.html', {})


def blog(request):
    return render(request, 'blog-home.html', {})