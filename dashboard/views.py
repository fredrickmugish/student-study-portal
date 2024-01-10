from django.shortcuts import render, redirect
from .models import Notes, Homework, Youtube
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import generic
from youtubesearchpython import VideosSearch



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
        messages.success(request, f"{request.user.username}, your notes are added successfully!")
        return HttpResponseRedirect('/notes')

def deleteNote(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('/notes')

class NotesDetailView(generic.DetailView):
    model = Notes

def homework(request):
    homework = Homework.objects.filter(user=request.user)

    if len(homework) == 0:
        homework_done = True
    else:
         homework_done = False

    context = {'homeworks':homework, 'homeworks_done':homework_done,}
    return render(request, 'dashboard/homework.html', context)


def addHomework(request):
    if request.method=="POST":
        s=request.POST['subject']
        t=request.POST['title']
        d=request.POST['description']
        u=request.POST['due']

        if 'is_finish' in request.POST:
            f = request.POST['is_finish']
        else:
            
            f = False

        user=request.user
        homework = Homework()
        homework.title=t
        homework.description=d
        homework.subject=s
        homework.due=u
        homework.is_finish=f
        homework.user=user
        homework.save()
        messages.success(request, f"{request.user.username}, your homework are added successfully!")
        return HttpResponseRedirect('/homework')
    
def deleteHomework(request, pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('/homework')

def update_homework(request, pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('/homework')

def youtube(request):
    youtube = Youtube.objects.filter(user=request.user)
    return render(request, 'dashboard/youtube.html')

def searchYoutube(request):
    context = {}
    if request.method=="POST":
        text=request.POST.get('text','')
        video = VideosSearch(text, limit=10)

        result_list = []
        for i in video.result()['result']:
            result_dict = {
             'input': text,
             'title': i['title'],
             'duration': i['duration'],
             'thumbnail': i['thumbnails'][0]['url'],
             'channel': i['channel']['name'],
             'link': i['link'],
             'views': i['viewCount']['short'],
             'published': i['publishedTime'],
            }

            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            result_list.append(result_dict)
            context = {
               'results': result_list
            }
        
        user=request.user
        youtube = Youtube()
        youtube.text = text
        youtube.user = user
        youtube.save()
        
        
    return render(request, 'dashboard/youtube.html', context)
