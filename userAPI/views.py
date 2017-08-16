from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PersonPageRank
from .serializers import PageRankSerializer


@csrf_exempt
def ranks_list(request):
    """
    List all ranks.
    """
    if request.method == 'GET':
        ranks =PersonPageRank.objects.all()
        serializer = PageRankSerializer(ranks, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def rank_detail(request, data):
    """
    rank for date
    """
    print(data)
    try:
        rank = PersonPageRank.objects.get(lastScanData=data)
    except PersonPageRank.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PageRankSerializer(rank)
        return JsonResponse(serializer.data)
