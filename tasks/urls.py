from django.urls import path
from .views import addView, eraseView, homePageView, searchExamView


urlpatterns = [
    path('', homePageView, name='home'),
    path('add/', addView, name = 'add'),
    path('delete/<int:exam_id>/', eraseView, name='delete'),
    path('search/', searchExamView, name='search')
]