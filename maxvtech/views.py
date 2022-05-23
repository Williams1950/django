from django.shortcuts import render
from .models import *
# Create your views here.

#def index(request):

# dest1=Dest()
#   dest1.name= 'Lagos Nigeria'
#   dest1.img= 'destination_1.jpg'
#   dest1.desc='The country choice'
#   dest1.price=10000
#   dest1.offer=True
#
#   dest2 = Dest()
#   dest2.name = 'Abuja Nigeria'
#   dest2.img = 'destination_2.jpg'
#   dest2.desc = 'The country choice'
##   dest2.price = 10000
#  dest2.offer=False

#   dest3 = Dest()
#   dest3.name = 'Imo Nigeria'
#   dest3.img = 'destination_3.jpg'
#   dest3.desc = 'The country choice'
#   dest3.price = 10000
#   dest3.offer=True

#   dests=[dest1, dest2, dest3]

#   return render(request, 'index.html', {'dests':dests})


# To get all data from database
def index(request):
    dests = Dest.objects.all()
    sliders = slider.objects.all()
    features = feature.objects.all()
    testimonial = testimonials.objects.all()
    testimonialtops = testimonialTop.objects.all()

    return render(request, 'index.html', {'dests':dests,'sliders':sliders,'features':features,'testimonial':testimonial,'testimonialtops':testimonialtops})


def contact(request):
    return render (request, 'contact.html')

def destinations(request):
    return render(request, 'destinations.html')

def about(request):
    return render(request,'about.html')

def elements(request):
    return render(request,'elements.html')