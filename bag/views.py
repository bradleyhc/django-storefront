from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to view the bag entries """

    return render(request, 'bag/bag.html')