from rest_framework import serializers
from .models import PersonPageRank, Persons, Sites, Pages, Keywords

class PageRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonPageRank
        fields = ('__all__')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = ('__all__')


class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = ('__all__')


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ('__all__')


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = ('__all__')
