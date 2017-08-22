from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.http import QueryDict
from rest_framework.request import Request

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)
from .permission import IsOwner
from .models import (
    PersonPageRank,
    Pages,
    Persons
)
from .serializers import (
    PageRankSerializer,
    PagesSerializer,
    PersonSerializer,
    UserLoginSerialiser,
    UserInfoSerialaser
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny
)
from rest_framework import generics

User = get_user_model()
#@csrf_exempt
#def ranks_list(request):
#    List all ranks.
#    """
#    if request.method == 'GET':
#        ranks = PersonPageRank.objects.all()
#        print(ranks)
#        serializer = PageRankSerializer(ranks, many=True)
#        return JsonResponse(serializer.data, safe=False)

#@csrf_exempt
#def rank_detail(request, data):
#    """
#    rank for date
#    """
#    try:
#        rank = PersonPageRank.objects.filter(pageId__lastScanDate = data)
#        print(rank)
#    except PersonPageRank.DoesNotExist:
#        return HttpResponse(status=404)
#    if request.method == 'GET':
#        serializer = PageRankSerializer(rank, many=True)
#        return JsonResponse(serializer.data, safe=False )

#class RankViewSet(generics.ListAPIView):
#    serializer_class = PersonSerializer
#    queryset = Persons.objects.all()
#    permission_classes = [IsAdminUser, IsAuthenticated]


class DayRankViewSet(generics.RetrieveAPIView):
    serializer_class = PagesSerializer
    lookup_field = 'lastScanDate'
    lookup_url_kwarg = 'lastScanDate'
    queryset = Pages.objects.all()
    permission_classes = [IsAuthenticated]


class FilterViewSet(generics.ListAPIView):
    """
    Этот класс отвечает за отображение списка или списка с фильтром
    """
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated] #разгарничение прав
    filter_backends = [SearchFilter,OrderingFilter] # Виды фильтров
    search_fields = ['name', 'ranks_on_pages__pageId__siteId__name'] #имена для поиска search в GET
    pagination_class = LimitOffsetPagination # пагинация через limit

    def get_queryset(self, *args, **kwargs):
        """
        Метод получения объекта  Query set через параметр в GET запросе

        :return: queryset_list - сортированный queryset
        """
        queryset_list = Persons.objects.all()
        query = self.request.GET.get('date')
        if query:
            queryset_list = queryset_list.filter(
                Q(ranks_on_pages__pageId__lastScanDate__icontains=query)
            ).distinct()
        return queryset_list

class UserLogin(APIView):
    """
    Реализует передачу логина-пароля через  post и получение csrftoken для аутонтификации.
    """

    permission_classes = [AllowAny]
    serializer_class = UserLoginSerialiser

    def post(self, request, *args, **kwargs):
        data = request.data
        serialiser = UserLoginSerialiser(data=data)
        if serialiser.is_valid():
            new_data = data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serialiser.errors, status=HTTP_400_BAD_REQUEST)


class UserUpdatePassword(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserInfoSerialaser
    lookup_field = 'username'
    permission_classes = [IsAuthenticated, IsOwner]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
