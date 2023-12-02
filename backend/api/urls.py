from django.urls import path
from .views import HelloWorld , ToDoView


urlpatterns = [
    path('hello/' , HelloWorld.as_view() , name = 'HelloWorld'),
    path('todo/' , ToDoView.as_view() , name = 'ToDo-tasks'),
    path('todo/<int:sno>/' , ToDoView.as_view() , name="ToDo-Specific")
]
