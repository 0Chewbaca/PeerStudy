from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Tutor
from django.core.mail import send_mail
from .models import Tutor
from django.views.generic import View, TemplateView
from django.http import JsonResponse

def home(request):
    return render(request, 'request/home.html', {'navbar': 'home'})

def tutor(request):
    if request.method == "POST":
        tutor = Tutor()
        
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        grade = request.POST.get('grade')
        lesson = request.POST.get('lessons')

        tutor.fname = fname
        tutor.lname = lname
        tutor.email = email
        tutor.grade = grade
        tutor.lesson = lesson

        tutor.save()
        
        return render(request, 'request/tutor.html', {'navbar': 'tutor', 'post': '1'})

    return render(request, 'request/tutor.html', {'navbar': 'tutor'})

def contact(request):
    if request.method == "POST":
        contact = Contact()
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.fname = fname
        contact.lname = lname
        contact.email = email
        contact.message = message
        contact.save()

        
        send_mail("Peer Study New Mail", message, email, ['eren.meric@stu.enka.k12.tr'])

        return render(request, 'request/contact.html', {'navbar': 'contact', 'post': '1'})

    return render(request, 'request/contact.html', {'navbar': 'contact'})

def reqHelp(request):
        return render(request, 'request/reqhelp.html', {'navbar': 'reqhelp'})

#class ReqHelp(TemplateView):
#    template_name = 'request/reqhelp.html'
    
    


class Eren(View):
    def get(self, *args, **kwargs):
        tutors = list(Tutor.objects.values())
        return JsonResponse({'data': tutors}, safe=False)
