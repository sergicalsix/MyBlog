from django.urls import path 
from app import views 

urlpatterns = [
    path('post/',views.PostViews.as_view(), name = 'post'),
    path('post/<str:pk>/', views.PostDetailViews.as_view(), name='post-detail')
]