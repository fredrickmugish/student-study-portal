from django.urls import path
from .import views

urlpatterns = [

    path('', views.home),
    path('notes/',views.notes),
    path('notes/add',views.addNotes),
    path('delete_note/<int:pk>',views.deleteNote, name='delete_note'),
    path('notes_detail/<int:pk>',views.NotesDetailView.as_view(), name='notes_detail'),
    path('homework/', views.homework, name="homework"),
    path('homework/add', views.addHomework),
    path('delete_homework/<int:pk>',views.deleteHomework, name='delete_homework'),
    path('update_homework/<int:pk>', views.update_homework, name="update_homework"),
    path('youtube/',views.youtube, name="youtube"),
    path('youtube/search', views.searchYoutube),
    path('todo/',views.todo),
    path('todo/add',views.addTodo),
    path('update_todo/<int:pk>', views.update_todo, name="update_todo"),
    path('delete_todo/<int:pk>',views.deleteTodo, name='delete_todo'),
]