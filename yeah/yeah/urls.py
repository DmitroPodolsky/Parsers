"""yeah URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from hello.views import *
from rest_framework import routers
#про роуты
#router = routers.SimpleRouter()#мы по сути ссылку обычную создаём с именем Dude
router = routers.DefaultRouter()#создаёт две ссылки на себя с помощью домена и на SimpleRouter()
router.register(r'Dude',AccountWOW,basename='account')#даём название и регистрируем с помощью того класса который создали будет api/v1/Account/Dude, вспомни проект thrird
print(router.urls)
#маршрутизатор
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/autorization/',include('rest_framework.urls')),
    #path('api/v1/Account/',include(router.urls)),
    path('api/v1/Account/',AccountCreate.as_view()),
    #он будет в себе в включать все функции и иметь свой индитификатор api/v1/Account/Dude/3/ - можно менять,удалять,получать колонку данных, а без этого добавить новую колонку или получить все
    #ReadOnlyModeViewSet - отменит возможность изменять данные и создавать новые
    path('api/v1/Account/<int:pk>/',AccountUpdate.as_view()),
    path('api/v1/Account/del/<int:pk>/',AccountDelete.as_view()),
    path('api/v1/Account+/<int:pk>/',AccountALL.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')) # отвечает за токены
    #заключение с помощью токена можно получать инфу без авторизации самого пользователя и он может с любого устройства с ним взаимодействовать
]
#path('api/v1/Account/<int:pk>/',AccountUpdate.as_view())#класс сам поймёт какая функция к нему поступает, в данном случае put
#yeah - обозначен как рабочая директория, тоесть благодаря єтому не вызывая главную дерикторию спокой
#но обращаемся к другой папке/файле
#path('api/v1/autorization/',include('rest_framework.urls')) - авторизация по сессии, добавляет кнопку логина и выйти с логина, также появляется csrftoken=45iCZDBbMno4K60SUknWitem4ayS0wX8; sessionid=5qvny1wktv14moad6vqk6wlj1zjujyhv