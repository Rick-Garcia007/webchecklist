from django.contrib import admin
from django.urls import path, include

from django.conf import settings
# no Django ele é usado para acessar as configurações do seu projeto Django de qualquer lugar no seu código. As configurações do Django são armazenadas em um módulo chamado settings, que contém uma série de variáveis ​​e configurações que controlam o comportamento da sua aplicação web. A importação de configurações permite acessar essas configurações e usá-las em seu código de maneira flexível.

from django.conf.urls.static import static
# é usado para configurar e fornecer manipulação de arquivos estáticos em uma aplicação web Django. Arquivos estáticos são recursos como folhas de estilo CSS, arquivos JavaScript, imagens e outros arquivos que não mudam dinamicamente com base na interação do usuário. Esses arquivos são servidos diretamente ao cliente e não requerem processamento do servidor.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('secureapp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
