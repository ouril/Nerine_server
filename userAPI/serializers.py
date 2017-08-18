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
        fields = ('personId', 'rank')


class PagesSerializer(serializers.ModelSerializer):
    page = PageRankSerializer(many=True, read_only=True)
    class Meta:
        model = Pages
        fields = ('url', 'lastScanDate', 'FoundDateTime', 'page')


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = ('__all__')
