from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("todos/", views.todos, name="Todos"),
    path("add/", views.add, name= "add"),
    path("sub/", views.sub, name= "sub"),
    path("calchistory/", views.history, name= "history"),
    path("cursor/", views.moveCursor, name="moveCursor"),
    path('move/', views.cursorMovement, name='moveCursor'),
    
]
