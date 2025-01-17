
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from movies.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('receipes/', receipes, name="receipes"),
    path('delete_receipe/<id>', delete_receipe, name="delete_receipe"),
    path('update_receipe/<id>', update_receipe, name="update_receipe"),
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page"),
    path('logout/', logout_page, name="logout_page"), 
    path('set-favorite-movie/', set_favorite_movie, name='set_favorite_movie'),
    path('get-favorite-movie/', get_favorite_movie, name='get_favorite_movie'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#blank suggests calling default port, that is 8000

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)