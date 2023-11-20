from django.urls import path
from .import views

app_name='photo'

urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),#http://127.0.0.1:8000
    path('post/', views.CreatePhotoView.as_view(), name='post'),#http://127.0.0.1:8000/post/
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),#http://127.0.0.1:8000/post_dpne/
    path('photos/<int:category>',views.CategoryView.as_view(),name='photos_cat'),#http://127.0.0.1:8000/photos/1/
    path('photo_detail/<int:pk>',views.DetailView.as_view(),name='photo_detail'),#http://127.0.0.1:8000/photo-detail/1/
    path('mypage/',views.MypageView.as_view(),name='mypage'),
    path('photo/<int:pk>/delete/',views.PhotoDeleteView.as_view(),name='photo_delete'),
]