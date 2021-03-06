from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/<int:pk>',views.user_profile,name='profile'),
    path('update_profile/',views.update_profile,name="update_profile"),
    path('post/<int:pk>',views.post,name='post'),
    path('search',views.search_profile,name="search"),
    path('follow/<int:pk>',views.FollowView,name="follow"),
    path('image/<int:pk>',views.view_image,name = 'image'),
    path('comment/<int:pk>',views.comment,name="comment"),
    path('like/<int:pk>',views.like,name="like"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)