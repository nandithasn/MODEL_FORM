from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def insert_student(request):
    d={'ESFO':StudentForm()}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('invalid data')

    return render(request,'insert_student.html',d)