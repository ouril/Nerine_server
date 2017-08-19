from rest_framework import serializers
from .models import (
                     PersonPageRank,
                     Persons,
                     Sites,
                     Pages,
                     Keywords
                     )


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = ('name', 'ranks_on_pages')

class PersonOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = ('name',)

class PageRankSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = PersonPageRank
        fields = ('name', 'rank')

    def get_name(self, obj):
        return str(obj.personId.name)

class SitesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sites
        fields = ('__all__')

class PagesSerializer(serializers.ModelSerializer):

    ranks = PageRankSerializer(many=True, read_only=True)

    class Meta:
        model = Pages
        fields = ('lastScanDate', 'ranks')


class DaySerialiser(serializers.ModelSerializer):
    personId = PersonOneSerializer()
    pageId = PageRankSerializer()

    class Meta:
        model = PersonPageRank
        fields = ('personId', 'pageId')
