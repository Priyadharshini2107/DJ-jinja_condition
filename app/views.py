from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'priya','age':14,'marks':85,'grade':3,'a':15}
    return render(request,'conditions.html',context=d)
