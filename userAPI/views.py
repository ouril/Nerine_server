from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)
from .models import (
    PersonPageRank,
    Pages,
    Persons
)
from .serializers import (
    PageRankSerializer,
    PagesSerializer,
    PersonSerializer
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics

@csrf_exempt
def ranks_list(request):
    """
    List all ranks.
    """
    if request.method == 'GET':
        ranks = PersonPageRank.objects.all()
        print(ranks)
        serializer = PageRankSerializer(ranks, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def rank_detail(request, data):
    """
    rank for date
    """
    try:
        rank = PersonPageRank.objects.filter(pageId__lastScanDate = data)
        print(rank)
    except PersonPageRank.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PageRankSerializer(rank, many=True)
        return JsonResponse(serializer.data, safe=False )

class RankViewSet(generics.ListAPIView):
    serializer_class = PersonSerializer
    queryset = Persons.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]


class DayRankViewSet(generics.RetrieveAPIView):
    serializer_class = PagesSerializer
    lookup_field = 'lastScanDate'
    lookup_url_kwarg = 'lastScanDate'
    queryset = Pages.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]

class FilterViewSet(generics.ListAPIView):
    serializer_class = PersonSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name', 'ranks_on_pages__pageId__siteId__name']
    pagination_class = LimitOffsetPagination#PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Persons.objects.all()
        query = self.request.GET.get('date')
        if query:
            queryset_list = queryset_list.filter(
                Q(ranks_on_pages__pageId__lastScanDate__icontains=query) #|
                #Q(name__incontains=query) #|
                #Q(ranks_on_pages__sites__name__incontains = query)
            ).distinct()
        return queryset_list