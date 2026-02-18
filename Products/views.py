from django.shortcuts import render


def  products(request):
    return render(request, 'product.html')
# Create your views here.
def next_page(request):
    return render(request,'next_page.html')
