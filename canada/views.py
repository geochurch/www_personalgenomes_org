from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.contrib import messages

def contact(request):
    errors = []
    if request.method == 'POST':
        has_req_entries = True
        if not request.POST.get('subject', ''):
            has_req_entries = False
            errors.append('Enter a subject.')
        if not (request.POST.get('sender_email', '') and '@' in request.POST['sender_email']):
            has_req_entries = False
            errors.append('Enter a valid e-mail address.')
        if not request.POST.get('message', ''):
            has_req_entries = False
            errors.append('Enter a message.')
        if ('<' in request.POST.get('sender_name', '') or '>' in request.POST.get('sender_name', '')):
            has_req_entries = False
            errors.append('Please do not put angle brackets in your name.')
        if has_req_entries:
            if request.POST.get('sender_name'):
                sender = (request.POST.get('sender_name') +
                          ' <' + request.POST.get('sender_email') + '>')
            else:
                sender = request.POST.get('sender_email')
            try:
                send_mail(
                    request.POST['subject'],
                    request.POST['message'],
                    sender,
                    ['crm@sickkids.ca'],
                    fail_silently=False,
                )
                messages.success(request, "Thanks! Your message has been sent.")
            except BadHeaderError:
                errors.append('Do not use newlines in subject or email.')
    if errors:
        messages.error(request, '<h4>Error with contact form submission:</h4>' +
                                '<li>' + '</li><li>'.join(errors) + '</li>',
                                extra_tags='htmlsafe')
    return render(request, 'canada/contact-us.html')
