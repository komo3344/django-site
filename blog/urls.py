from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('<int:pk>/new_comment/', views.new_comment, name='comment-create'),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view(), name='comment-update'),
    path('category/<str:slug>/', views.category_page, name='category'),
    path('tag/<str:slug>/', views.tag_page, name='tag'),
    path('create_post/', views.PostCreate.as_view(), name='create'),
    path('update_post/<int:pk>/', views.PostUpdate.as_view(), name='update')

]