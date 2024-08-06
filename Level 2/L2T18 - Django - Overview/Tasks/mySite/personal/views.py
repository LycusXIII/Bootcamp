from django.shortcuts import render


# Create your views here.
def personal(request):
    return render(request, "personal.html")


def cv(request):
    return render(request, "cv.html")


def shopping(request):
    return render(request, "shopping.html")
