from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create_author/', views.create_author, name="create_author"),
    path('create_book/', views.create_book, name="create_book"),
    path('update_author/<str:pk>', views.update_author, name="update_author"),
    path('update_book/<str:pk>', views.update_book, name="update_book"),
    path('delete_author/<str:pk>', views.delete_author, name="delete_author"),
    path('delete_book/<str:pk>', views.delete_book, name="delete_book")
]
