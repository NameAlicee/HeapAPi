from django.urls import path

from . import views


urlpatterns = [
    path("posts/", views.PostsListView.as_view()),
    path("posts/<int:pk>/", views.PostsDetailView.as_view()),
]
