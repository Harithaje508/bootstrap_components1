from django.shortcuts import render

# Create your views here.
def b1(request):
    return render(request,'b1.html')
def b2(request):
    return render(request,'b2.html')
def b3(request):
    return render(request,'b3.html')
def collapse(request):
    return render(request,'collapse.html')
def collapse_hz(request):
    return render(request,'collapse-hz.html')
def dropdowns(request):
    return render(request,'dropdowns.html')
def forms(request):
    return render(request,'forms.html')
def inputgroup(request):
    return render(request,'inputgroup.html')
def listgroup(request):
    return render(request,'listgroup.html')
def mediaobj(request):
    return render(request,'mediaobj.html')