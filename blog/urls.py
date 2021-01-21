from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='blog-home'),
#     path('<int:id>/', views.records, name='blog-update'),
#     path('delete/<int:id>/', views.records_delete, name='blog-delete'),
#     path('register/', views.register, name='blog-register'),
#     path('login/', views.login, name='blog-login'),
#      path('logout/', views.logout, name='blog-logout'),
#     path('records/', views.records, name='blog-records'),
# ]
urlpatterns = [
    path('', views.register, name='blog-register'),
    path('login/', views.login, name='blog-login'),
    path('home/', views.home, name='blog-home'),
    path('<int:id>/', views.records, name='blog-update'),
    path('delete/<int:id>/', views.records_delete, name='blog-delete'),
    path('logout/', views.logout, name='blog-logout'),
    path('records/', views.records, name='blog-records'),
]