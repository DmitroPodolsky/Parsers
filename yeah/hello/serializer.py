import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Account
#class AccountModel:
    #def __init__(self,login,password):
        #self.login=login
        #self.password=password

class SeriaAccount(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())#скрывает поле для глаз и устанавливает текущее значение ключа user
    class Meta():
        model = Account
        #fields = ['user','login','password','cat']#на этот раз мы указываем не cat_id,он принимает внешний ключ
        fields = '__all__'#ты понимаешь
#обычный-неудобный метод сериализатора
#class SeriaAccount(serializers.Serializer):
    #базовый класс сериализатора
    #login = serializers.CharField(max_length=20)
    #password = serializers.CharField()
    #time_create = serializers.DateTimeField(read_only=True)
    #time_update = serializers.DateTimeField(read_only=True)# здесь не должно быть параметров некоторых
    #is_published = serializers.BooleanField(default=True)  # опубликована запись или нет
    #cat_id = serializers.IntegerField()#условия сериализатора вынуждают айди преабразовывать в число
    #def create(self, validated_data):
        #return Account.objects.create(**validated_data)#распаковывает словарь ** validated_data который создался с помощью seria.is_valid(raise_exception=True)
    #def update(self, instance: Account, validated_data):
        #изменение существующих данных
        #instance - это наша модель Account - тоесть он имеет все его атрибуты и функционал
        #validated_data - словарь который создался при проверке
        #instance.login=validated_data.get("login",instance.login)#,instance.login) в случае если будет что-то не так или пустая строка будет возращено то же самое значение
        #instance.password = validated_data.get("password", instance.password)
        #instance.time_create = validated_data.get("time_create", instance.time_create)
        #instance.time_update = validated_data.get("time_update",instance.time_update)
        #instance.cat_id = validated_data.get("cat_id",instance.cat_id)
        #instance.save()
        #return instance
    #def __delete__(self, instance):
        #instance.delete()
        #instance.save()
        #return instance
#процесс формата JSON
#def decode(jom):
    ##перерабатываем строку JSON
    #goro = io.BytesIO(jom) #делает бит читабельным
    #data = JSONParser().parse(goro) #парсируем строку
    #seria = SeriaAccount(data=data)#сопоставляет значения с ключами
    #seria.is_valid()#проверяем на правильность
    #print(seria.validated_data) # вернули в прежний ввид ввиде списка с кортежами
#def encode():
    #создаём Json строку
    #model = AccountModel('hello', '1234')
    #model_han = SeriaAccount(model)
    #print(model_han.data, type(model_han.data))  # это ввиде словаря
    #json = JSONRenderer().render(model_han.data)  # байтовая строка JSON
    #print(json, type(json))
    #decode(json)


#class SeriaAccount(serializers.ModelSerializer):
    #перерабатывем базы данных в JSON-формат
    #создание сериализатора
    #class Meta:
        #model = Account
        #fields = ('login','cat')#поля сериализации которые вернуться обратно пользователю ввиде JSON