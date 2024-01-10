from django.urls import path
from . import views
app_name='books'
urlpatterns=[
    path('',views.home,name='home'),
    path('view',views.view_book,name='view'),
    path('add',views.add_book,name='add'),
    path('add2',views.add_book2,name='add2'),
    path('book_detail<int:p>',views.book_detail,name='book_detail'),
    path('book_delete<int:p>',views.book_delete,name='book_delete'),
    path('book_edit<int:p>',views.book_edit,name='book_edit'),
    path('search_view',views.search_view,name='search_view'),
    path('search',views.search,name='search'),
    path('register/',views.register,name='register'),

]

# static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)