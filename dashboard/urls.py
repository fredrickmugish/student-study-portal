from django.urls import path
from .import views

urlpatterns = [

    path('', views.home),
    path('notes/',views.notes),
    path('notes/add',views.addNotes),
    path('delete_note/<int:pk>',views.deleteNote, name='delete_note'),
    path('notes_detail/<int:pk>',views.NotesDetailView.as_view(), name='notes_detail')
]