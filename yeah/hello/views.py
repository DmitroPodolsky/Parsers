from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics,viewsets#множество базовых классов
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView#главная вещь для представлений
from .models import Account, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import SeriaAccount
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, \
    IsAuthenticated  # это отвечает за ограничения доступа к информации
# Create your views here.
#class ViewAPIAccount(generics.ListAPIView):
    #ueryset = Account.objects.all()
    #serializer_class = SeriaAccount#создание представления
#мега упрощение api
class AccountWOW(viewsets.ModelViewSet):
    #queryset = Account.objects.all() #берёт все данные
    serializer_class = SeriaAccount
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Account.objects.all()[:3]
        return Account.objects.filter(pk=pk)
    @action(methods=['get'],detail=False)#detail отвечает заь количество записей, False-множество,True-одна запись
    def hello(self,request):
        cats = Category.objects.all()
        return Response({"cats": [c.name for c in cats]})

    @action(methods=['get'], detail=True)  # detail отвечает заь количество записей, False-множество,True-одна запись
    def han(self, request,pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({"cats": cats.name})

#упрощение APIView
class AccountCreatePagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'#указываем свой размер если size, без этого просто находить по цыфре страницу
    max_page_size = 100#создаём свою пагинацию
class AccountCreate(generics.ListCreateAPIView):
    #для Post get запросов
    queryset = Account.objects.all() #берёт все данные
    serializer_class = SeriaAccount
    pagination_class = AccountCreatePagination#подключаем свою пагинацию
    #permission_classes = (IsAuthenticatedOrReadOnly, )
    #IsAuthenticatedOrReadOnly - отвечает за то авторизован ли пользователь в джанго админ user
class AccountUpdate(generics.RetrieveUpdateAPIView):
    #для put запросов
    queryset = Account.objects.all()  # берёт только одну таблицу а не все!!
    serializer_class = SeriaAccount
    permission_classes = (IsOwnerOrReadOnly,)
    #authentication_classes = (IsAuthenticated,) - онго будет воспринимать вход только через токен, можно и наоборот
class AccountDelete(generics.RetrieveDestroyAPIView):
    #для delete запросов
    queryset = Account.objects.all()  # берёт только одну таблицу а не все!!
    serializer_class = SeriaAccount
    permission_classes = (IsAdminOrReadOnly, )
class AccountALL(generics.RetrieveUpdateDestroyAPIView):
    #обладает системой CRUD можем изменять,получать,удалять запись отдельную
    queryset = Account.objects.all()  # берёт только одну таблицу а не все!!
    serializer_class = SeriaAccount
class ViewAPIAccount(APIView):
    #APIView - базовый клас представления
    def get(self,request):
        lol= Account.objects.all()
        return Response({'login':SeriaAccount(lol,many=True).data})#принимает url и возращает ответ ввиде JSON
    #data - отвечает за преобразавание в словарь
    #RESPONCE - преобразовывает словарь в байтовую JSOn строку, lol данные бд
    def post(self,request):
        seria = SeriaAccount(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response({'post': seria.data})#но тут надо уже указывать чётко название запроса пост гет тип
        #post_new=Account.objects.create(
            #login=request.data['login'],
            #password=request.data['password'],
            #cat_id=request.data['cat_id']
        #)#сat_id - айдишник другой таб из связей, мы тут добавляем  новую таб ввиде JSON без сериализатора
        # return Response({'loln':SeriaAccount(post_new,many=True).data})
    def put(self,request,*args,**kwargs):
        pk = kwargs.get('pk',None)#pk работает как айди объекта
        if not pk:
            return Response({"Error":"ебать ты лох"})
        try:
            instance=Account.objects.get(pk=pk)
        except:
            return Response({"Error":"ебать ты лох"})
        seria = SeriaAccount(data=request.data,instance=instance)#instance то что сверху
        seria.is_valid(raise_exception=True)
        seria.save()#так как мы указали одновременно instance и data будет вызываться метод uodate
        return Response({'update': seria.data})
    def delete(self,request,*args,**kwargs):
        pk = kwargs.get('pk',None)#pk работает как айди объекта
        if not pk:
            return Response({"Error":"ебать ты лох"})
        try:
            instance=Account.objects.get(pk=pk)
        except:
            return Response({"Error":"ебать ты лох"})
        seria = SeriaAccount(data=request.data,instance=instance)#instance то что сверху
        seria.is_valid(raise_exception=True)
        seria.__delete__(instance)# вот как удалить хахахаха
        return Response({'update': f'delete {pk}'})
    #про остальные методы - если пишет что метод не разрешон в postmen то значит что такого метода нету у нас