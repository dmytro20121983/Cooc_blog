from django.urls import path
from .import views
app_name = 'blog'
urlpatterns = [
    path('home', views.home, name = 'index'),
    path('<slug:slug>/', views.PostListView.as_view(), name = 'post_list'),
    path('', views.news),
    
    
]
