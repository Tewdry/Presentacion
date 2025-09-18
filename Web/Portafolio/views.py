from django.shortcuts import render


# Vistas

def principal(request):
    return render(request, 'Principal/Base.html')



