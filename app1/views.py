from django.shortcuts import render

# Create your views here.
def jinjaprint(request):
    d={'name':'SUNI'}
    return render(request,'jinjaprint.html',context=d)
