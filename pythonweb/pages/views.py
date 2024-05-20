from django.http import HttpResponseRedirect
from django.shortcuts import render



from django.core.mail import send_mail
from .forms import EmailForm

def home(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(sender)
            send_mail(subject+"/"+sender, message, from_email=sender, recipient_list=["dominiktravnicek281@gmail.com"], )
            
    else:
        form = EmailForm()
    return render(request, 'pages/home.html', {'form': form})