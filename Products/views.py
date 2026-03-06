from django.shortcuts import render,get_object_or_404


from .models import Car


# Create your views here.

def Products(request):
    return render(request, 'product.html')


def next_page(request):
    cars = Car.objects.all()
    context = {
        'cars':cars
    }
    return render(request, 'next_page.html', context)




def second_page(request, id):
    car = get_object_or_404(Car, id=id)


    context = {
        'car': car
    }
    return  render(request, 'second_page.html', context)