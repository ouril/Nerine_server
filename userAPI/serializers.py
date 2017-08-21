from django.contrib.auth import get_user_model
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

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Persons
        fields = ('name', 'ranks_on_pages')

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

class DaySerialiser(ModelSerializer):
    personId = PersonOneSerializer()
    pageId = PageRankSerializer()

    class Meta:
        model = PersonPageRank
        fields = ('personId', 'pageId')


class SitesSerializer(ModelSerializer):

    class Meta:
        model = Sites
        fields = ('__all__')

class PagesSerializer(ModelSerializer):

    ranks = PageRankSerializer(many=True, read_only=True)

    class Meta:
        model = Pages
        fields = ('lastScanDate', 'ranks')

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




