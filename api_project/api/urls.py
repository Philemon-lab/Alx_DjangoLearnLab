from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookListCreate, BookDetail
from .views import BookList

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/',BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
