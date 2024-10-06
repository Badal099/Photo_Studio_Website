from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from . import emailAPI
curl = settings.CURRENT_URL


def home(request):
    shots = Shots.objects.all()
    return render(request, 'home.html', {'shots': shots, 'curl': curl})


def about(request):
    return render(request, 'about.html', {'curl': curl})


def services(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        imagetype = request.POST['imagetype']
        imagesize = request.POST['imagesize']
        imagequantity = request.POST['imagequantity']
        message = request.POST['message']
        address = request.POST['address']
        image = request.FILES['image']
        date = request.POST['date']
        time = request.POST['time']
        service = Services(name=name, phone=phone,
                           email=email, imagetype=imagetype, imagesize=imagesize, imagequantity=imagequantity, message=message, address=address, image=image, date=date, time=time)
        service.save()
        import requests

        url = "https://www.fast2sms.com/dev/bulkV2"

        querystring = {"authorization": "mK1Z6CIRiJBzjQvSLNdMysTt2WD8HoehbPrn9uVEk3pUOl5faAZVKH6lItGh1Y9sBF4OcmMa0iNPxAdU",
                       "message": ("Hello Chouhan Ji! Welcome to PhotoShop, "+name+" needs an Urgent Photo.Their email is "+email+". "
                                    " Click here to reply: http://localhost:8000/reply/"),"language": "english", "route": "q", "numbers": "6264982416"}

        headers = {
            'cache-control': "no-cache"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        print(response.text)
        return render(request, 'services.html', {'curl': curl, 'msg': 'Your request send successfully! Please wait 5 Minutes for our reply.We send an Email to you.'})

    else:
        return render(request, 'services.html', {'curl': curl, 'msg': ''})


def booking(request):
    pricing = Pricing.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        event = request.POST['event']
        address = request.POST['address']
        message = request.POST['message']
        date = request.POST['date']
        time = request.POST['time']
        booking = Booking(name=name, phone=phone,
                          email=email, event=event, address=address, message=message, date=date, time=time)
        booking.save()
        import requests

        url = "https://www.fast2sms.com/dev/bulkV2"

        querystring = {"authorization": "mK1Z6CIRiJBzjQvSLNdMysTt2WD8HoehbPrn9uVEk3pUOl5faAZVKH6lItGh1Y9sBF4OcmMa0iNPxAdU",
                       "message": ("Hello Chouhan Ji! Welcome to PhotoShop, "+name+" book an Event.Their email is "+email+". "
                       " Click here to reply: http://localhost:8000/reply/"), "language": "english", "route": "q", "numbers": "8085119177"}

        headers = {
            'cache-control': "no-cache"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        print(response.text)
        return render(request, 'booking.html', {'pricing': pricing, 'curl': curl, 'msg': "Your booking request send seccessfully! Please wait 1 hour for our reply. We send an Email to you."})

    else:
        return render(request, 'booking.html', {'pricing': pricing, 'curl': curl, 'msg': ''})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contacts = Contact(name=name, phone=phone,
                           email=email, message=message)
        contacts.save()
        import requests

        url = "https://www.fast2sms.com/dev/bulkV2"

        querystring = {"authorization": "mK1Z6CIRiJBzjQvSLNdMysTt2WD8HoehbPrn9uVEk3pUOl5faAZVKH6lItGh1Y9sBF4OcmMa0iNPxAdU",
                       "message": ("Hello Chouhan Ji! Welcome to PhotoShop, "+name+" send a message."), "language": "english", "route": "q", "numbers": "8085119177"}

        headers = {
            'cache-control': "no-cache"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        print(response.text)
        return render(request, 'contact.html', {'curl': curl, 'msg': 'Your Message Send Successfully.'})

    else:
        return render(request, 'contact.html', {'curl': curl, 'msg': ''})


def shots(request):
    shots = Shots.objects.all()
    return render(request, 'shots.html', {'shots': shots, 'curl': curl})


def creative(request):
    creative = Creative.objects.all()
    return render(request, 'creative.html', {'creative': creative, 'curl': curl})


def wedding(request):
    wedding = Wedding.objects.all()
    return render(request, 'wedding.html', {'wedding': wedding, 'curl': curl})


def birthday(request):
    birthday = Birthday.objects.all()
    return render(request, 'birthday.html', {'birthday': birthday, 'curl': curl})


def fashion(request):
    fashion = Fashion.objects.all()
    return render(request, 'fashion.html', {'fashion': fashion, 'curl': curl})


def agricultural(request):
    agricultural = Agricultural.objects.all()
    return render(request, 'agricultural.html', {'agricultural': agricultural, 'curl': curl})


def adventural(request):
    adventural = Adventural.objects.all()
    return render(request, 'adventural.html', {'adventural': adventural, 'curl': curl})


def festival(request):
    festival = Festival.objects.all()
    return render(request, 'festival.html', {'festival': festival, 'curl': curl})


def newborn(request):
    newborn = Newborn.objects.all()
    return render(request, 'newborn.html', {'newborn': newborn, 'curl': curl})


def reply(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        reply = Reply(name=name, phone=phone,email=email, message=message)
        reply.save()
        emailAPI.sendEMAIL(email,name,phone,message)
        return render(request, 'reply.html', {'curl': curl, 'msg': 'Your Message Send Successfully.'})
        
    else:
        return render(request, 'reply.html', {'curl': curl, 'msg': ''})

    

