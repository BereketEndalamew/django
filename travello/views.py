from django.shortcuts import render
from .models import Destination


# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = "Addis Ababa"
    dest1.img = "destination_1.jpg"
    dest1.desc = "The country never sleeps"
    dest1.offer=True
    dest1.price = 400

    dest2 = Destination()
    dest2.name = "Bahir Dar"
    dest2.img = "destination_2.jpg"
    dest2.desc = "The country never sleeps"
    dest2.offer=True
    dest2.price = 500

    dest3 = Destination()
    dest3.name = "Dessie"
    dest3.img = "destination_3.jpg"
    dest3.desc = "The country never sleeps"
    dest3.offer=False
    dest3.price = 600

    dest4 = Destination()
    dest4.name = "Wolayita sodo"
    dest4.img = "destination_4.jpg"
    dest4.desc = "The country never sleeps"
    dest4.offer=False
    dest4.price = 700

    dest5 = Destination()
    dest5.name = "Jimma"
    dest5.img = "destination_5.jpg"
    dest5.desc = "The country never sleeps"
    dest5.offer=False
    dest5.price = 800

    dest6 = Destination()
    dest6.name = "Hawassa"
    dest6.img = "destination_6.jpg"
    dest6.desc = "The country never sleeps"
    dest6.offer=False
    dest6.price = 900

    dests = [dest1, dest2, dest3, dest4, dest5, dest6]
    return render(request, "index.html", {'dests': dests})
