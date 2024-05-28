from django.shortcuts import render

# Create your views here.
def excurse(request):
    return render(request, 'excurse.html')