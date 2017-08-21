from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import (
   #RankViewSet,
   #DayRankViewSet,
   FilterViewSet,
   UserLogin
)

router = DefaultRouter()
#router.register(r'rank/$', RankViewSet)
#router.register(r'^rank/(?P<data>(\d{4}-\d{2}-\d{2}))/$', DayRankViewSet)

#urlpatterns = router.urls

urlpatterns = [
  # url(r'^rank/(?P<lastScanDate>(\d{4}-\d{2}-\d{2}))/$', DayRankViewSet.as_view()),
  # url(r'^rank/(?P<pk>([0-9]+))/$', DayRankViewSet.as_view()),
  # url(r'^rank/$', RankViewSet.as_view()),
   url(r'personrank/', FilterViewSet.as_view()),
   url(r'login/$', UserLogin.as_view(), )
]
