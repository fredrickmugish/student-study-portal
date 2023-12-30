from django.shortcuts import render
from .models import Notes
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes}
    return render(request, 'dashboard/notes.html', context)

def addNotes(request):
    if request.method=="POST":
        t=request.POST['title']
        d=request.POST['description']
        user=request.user
        notes = Notes()
        notes.title=t
        notes.description=d
        notes.user=user
        notes.save()
        return HttpResponseRedirect('/notes')
