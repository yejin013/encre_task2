from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('list', views.GameList.as_view(), name='gameList'),
    path('<int:pk>', views.GameDetail.as_view(), name='gameDetail'),
    path('skill', views.SkillList.as_view(), name='skill'),
    path('character', views.CharacterList.as_view(), name='characterList'),
    path('character/<int:pk>', views.CharacterDetail.as_view(), name='characterDetail'),
    path('comment', views.CommentList.as_view(), name='commentList'),
    path('comment/<int:pk>', views.CommentDetail.as_view(), name='commentDetail'),
]