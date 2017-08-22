from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import (
            ModelSerializer,
            CharField,
            SerializerMethodField,
            ValidationError

)
from .models import (
                     PersonPageRank,
                     Persons,
                     Sites,
                     Pages,
                     )

User = get_user_model()

class UserInfoSerialaser(ModelSerializer):
    username = CharField(read_only=True, allow_blank=True)
    email = CharField(read_only=True, allow_blank=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        extra_kwargs = {'password':
                            {'write_only':True}
                        }
    def update(self, instance, validated_data):
        password = validated_data['password']
        password_hush = make_password(password)
        validated_data['password'] = password_hush
        return super(UserInfoSerialaser, self).update(instance, validated_data)


class PersonSerializer(ModelSerializer):
    ranks_on_pages = SerializerMethodField()
    class Meta:
        model = Persons
        fields = ('name', 'ranks_on_pages')

    def get_ranks_on_pages(self, obj):
        obj_list = obj.ranks_on_pages.filter(personId=obj.id)
        list_of_ranks = [i.rank for i in obj_list]
        return sum(list_of_ranks)


class PersonOneSerializer(ModelSerializer):
    class Meta:
        model = Persons
        fields = ('name',)

class PageRankSerializer(ModelSerializer):
    name = SerializerMethodField()

    class Meta:
        model = PersonPageRank
        fields = ('name', 'rank')

    def get_name(self, obj):
        return str(obj.personId.name)

class SitesSerializer(ModelSerializer):

    class Meta:
        model = Sites
        fields = ('__all__')

class PagesSerializer(ModelSerializer):
    ranks = PageRankSerializer(many=True)

    class Meta:
        model = Pages
        fields = ('url', 'ranks')

class UserLoginSerialiser(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'token',
        )
        extra_kwargs = {'password':
                            {'write_only':True}
                        }
    def validate(self, data):

        username = data.get('username', None)
        password = data['password']
        if not username:
            raise ValidationError("Incorrect password")
        user = User.objects.filter(username=username)
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Username is not valid!")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect password")
        data['token']=""
        return data




