from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('list/<int:book_id>/', views.ListComment.as_view(), name='comment_list'),
    path('create/<int:book_id>/', views.CreateComment.as_view(), name='comment_create'),
]
