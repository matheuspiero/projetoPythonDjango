from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.galeria.urls')),
    path('', include('apps.usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

#para a AWS precisaria retirar a parte + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) do urlpatterns
#alterar todos os "/assets/" de todos os arquivos do nosso projeto para "assets/", com ctrl F
#depois utilizar o comando python manage.py collectstatic para mandar para AWS