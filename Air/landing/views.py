from django.shortcuts import render,redirect
import requests
from .models import Flight,flight1,Booking,booking2
from datetime import datetime,date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
import random

def fetch_and_store_flights():
    url = "https://my.api.mockaroo.com/airline.json?key=609fc420"
    response = requests.get(url)
    url1 = "https://api.unsplash.com/search/photos?query=airport"
    headers = {
    "Authorization": "Client-ID dEPn3okGWdCCa8sN7ec7fRjiKaQzh_eWKSdXswse8mI"
}

    response1 = requests.get(url1, headers=headers) 
    
    if response.status_code == 200:
        flight_data = response.json()
        image = response1.json()
        counter = 0
        for data in flight_data:
            flight1.objects.create(
                flight_number=data['flight_no'],
                origin=data['from'],
                destination=data['to'],
                departure_time=datetime.strptime(f"{date.today()} {data['departure']}", "%Y-%m-%d %H:%M"),
                
                airline=data['airline_name'],
                image = image['results'][counter]['urls']['regular'],
                price=data['price'],
                flight_class=data['class'],
                seats_available=data['seats'],
                )
            counter+=1


# Create your views here.
def landing1(request):
    qurey=request.GET.get('qurey')
    flights = flight1.objects.all()
    user = request.user.username

    
    if qurey:
        print(qurey)
        

    return render(request,'landing/landing1.html',{'flights':flights,'user':user})

@login_required(login_url='login')
def Booking_(request):
    flights = flight1.objects.all()
    qurey=str(request.GET.get('qurey'))
    if qurey:
        if qurey.upper()=="MORE" or qurey.upper()=="MORE FLIGHTS":
            fetch_and_store_flights()
            return redirect('booking')


    return render(request,'landing/booking.html',{'flights':flights})

@login_required(login_url='login')
def Book(request):
    flights = flight1.objects.all()
    if request.method == 'POST':
        
        flight_number= request.POST.get("flight_number")
        origin= request.POST.get("origin")
        destination= request.POST.get("destination")
        class_= request.POST.get("class_")
        flight = flight1.objects.filter(airline=flight_number)
        for f in flight:
            k = model_to_dict(f)
            seats_available = k['seats_available']

            price=k['price']
            image= k['image']
        if flight.exists():


            booking2.objects.create(
            user=request.user,
            airline=flight_number,
            origin=origin,
            destination=destination,
            flight_class=class_,
            price= price,
            seats_available= seats_available,
            image=image


        )
            return redirect('success')
        else:
            return redirect('404')


    return render(request,'landing/book.html',{'flights':flights})
login_required(login_url='login')
def mybookings(request):
    flights = flight1.objects.all()
    user = request.user
    bookings= booking2.objects.filter(user=user)
    if not bookings.exists():
        return redirect("nobooks")

    return render(request,"landing/mybookings.html",{'flights':flights,'bookings':bookings})

def success(request):
    ticket = booking2.objects.filter(user=request.user)
    for t in ticket:
        t = model_to_dict(t)
        k = t['airline']

    day = date.today()
    return render(request,'landing/success.html',{"k":k,'day':date})

def pg_404(request):
    return render(request,'landing/404.html')
    

def nobooks(request):
    return render(request,'landing/nobooks.html')