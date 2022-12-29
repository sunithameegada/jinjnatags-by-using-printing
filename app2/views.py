from django.shortcuts import render

# Create your views here.
def jinjaprint2(request):
    d={'name':'LOKI'}
    return render(request,'jinjaprint2.html',d)

