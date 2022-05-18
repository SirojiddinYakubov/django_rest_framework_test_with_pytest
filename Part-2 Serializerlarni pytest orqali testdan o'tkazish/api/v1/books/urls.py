from django.urls import path
from api.v1.books import views

app_name = 'books'

urlpatterns = [
    path('list/', views.BookListAPIView.as_view(), name='book_list'),
    path('create/', views.BookCreateAPIView.as_view(), name='book_create'),
    path('update/<int:pk>/', views.BookUpdateAPIView.as_view(), name='book_update'),
    path('detail/<int:pk>/', views.BookDetailAPIView.as_view(), name='book_detail'),
    path('delete/<int:pk>/', views.BookDeleteAPIView.as_view(), name='book_delete'),
]
