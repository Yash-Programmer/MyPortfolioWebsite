from django.shortcuts import render
import os
from email.mime.text import MIMEText
from email.utils import formataddr
from django.http import HttpResponse
import emoji
import re
import wolframalpha as wf
import re
import wikipedia as wiki
import os
import datetime
from datetime import date
from .models import Messages
from .models import Contact

def comment(request):
     context = {'display': 'none', "messages_list": Messages.objects.order_by('id')}

     if request.method == "POST":
          person_name = request.POST.get('person', 'None')
          comment = request.POST.get('comment', 'None')
          if person_name == 'None' and comment == "None":
               pass
          else:
               message_instance = Messages.objects.create(name=person_name, comment=comment)
               context['display'] = "block"
               context['message_list'] = Messages.objects.order_by('id')


     return render(request, 'messages.html', context)

def index(request):
    birth_date = datetime.date(2010, 7, 17) 
    end_date = date.today()

    time_difference = end_date - birth_date

    age = time_difference.days

    context = {
         "days": age
    }
    return render(request, 'index.html', context)

def answer(request):
    message0 = request.GET.get('query', 'default')
    message1 = re.sub(emoji.get_emoji_regexp(), r"", message0)
    message1 = message0.lower()

    try:
        app_id = ''
        client = wf.Client(app_id)
        result = client.query(message1)
        answer = next(result.results).text
        return render(request, 'answer.html', {'res': answer + '  ', 'mes': message0})
    except Exception:
        try:
            answer = wiki.summary(message1, sentences=3)
            return render(request, 'answer.html', {'res': answer + '  ', 'mes': message0})
        except Exception:
            return render(request, 'answer.html', {'res': 'Sorry, I am unable to understand you. 😢' + '  ', 'mes': message0})

def send(request):
    Name = request.GET.get('name', 'None')
    User_Message = request.GET.get('text','None')
    Email = request.GET.get('email', 'None')

    message_instance = Contact.objects.create(name=Name, email=Email, message=User_Message)

    return render(request, 'sent.html')
