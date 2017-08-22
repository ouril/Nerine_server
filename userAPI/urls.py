from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from .views import (
   #RankViewSet,
   DayRankViewSet,
   FilterViewSet,
   UserLogin,
   UserUpdatePassword
)

router = DefaultRouter()
#router.register(r'rank/$', RankViewSet)
#router.register(r'^rank/(?P<data>(\d{4}-\d{2}-\d{2}))/$', DayRankViewSet)

#urlpatterns = router.urls

urlpatterns = [
   url(r'^dailyrank/(?P<lastScanDate>(\d{4}-\d{2}-\d{2}))/$', DayRankViewSet.as_view()),
  # url(r'^rank/(?P<pk>([0-9]+))/$', DayRankViewSet.as_view()),
  # url(r'^rank/$', RankViewSet.as_view()),url(r'api/v1/auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
   url(r'api-token-auth/', obtain_jwt_token),
   url(r'personrank/', FilterViewSet.as_view()),
   url(r'login/$', UserLogin.as_view()),
   url(r'user_pass/(?P<username>\w+)/$', UserUpdatePassword.as_view()),
]


#Для теста:
#curl -X POST -d "username=test2&password=Dragonage" http://127.0.0.1:8000/api/login/
#curl -H "Authorization: JWT <token>" http://127.0.0.1:8000/personrank/