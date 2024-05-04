from django.urls import path
from .views import vlog_list, vlog_detail
from .views import create, update, delete
from .views import category_filter
from .views import signup, user_login


urlpatterns=[
    path('blogs/', vlog_list, name='vlog_list'),
    path('blogs/<int:pk>/', vlog_detail, name='vlog_detail'),
    path('blogs/create/', create, name='create'),
    path('blogs/<int:pk>/update/', update, name='update'),
    path('blogs/<int:pk>/delete/', delete, name='delete'),
    path('blogs/category/<int:pk>/', category_filter, name='category'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
]