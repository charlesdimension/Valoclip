from django.urls import path

from .views import HomePageView, UploadClipView
from videos import views

urlpatterns = [
    path('upload/', UploadClipView.as_view(), name='upload'),
    path('', HomePageView.as_view(), name='home'),
    path('thumbs/', views.thumbs, name='thumbs'),

]