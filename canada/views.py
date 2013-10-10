from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if errors:
            messages.error(request,
                           '<h4>Error with contact form submission:</h4>' +
                           '<li>' + '</li><li>'.join(errors) + '</li>',
                           extra_tags='htmlsafe')
        else:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                fail_silently=True,
                )
            messages.success(request, "Thanks! Your message has been sent.")
    return render(request, 'canada/contact.html')
