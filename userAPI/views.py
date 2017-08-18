from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PersonPageRank, Pages
from .serializers import PageRankSerializer, PagesSerializer
from rest_framework import viewsets
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
    serializer_class = PageRankSerializer
    queryset = PersonPageRank.objects.all()


class DayRankViewSet(generics.RetrieveAPIView):
    serializer_class = PagesSerializer
    queryset = Pages.objects.all()
    lookup_field = 'lastScanDate'
    lookup_url_kwarg = 'lastScanDate'