from django.urls import path
from . import views
app_name = 'usermember'
urlpatterns = [
    path('', views.logins.as_view(), name="login"),
    # path('getContact/', views.getContact, name="getContact"),
    # path('thu/', views.login1.as_view(), name="login1"),
    path('file/', views.file.as_view(), name="file"),
    path('hienthi/', views.theongays.as_view(), name="hienthi"),
    path('table/', views.table.as_view(), name="table"),
    path('dudoan/', views.dudoan.as_view(), name="dudoan"),
    path('trangchu/',views.trangchu.as_view(), name="trangchu"),
    path('api/chart/data/', views.ChartData.as_view()),
    path('thingspeak/', views.thingspeak.as_view(),name='thingspeak'),
    path('api/chart/thingspeak1/', views.thingspeak1.as_view()),
    path('API/dataAPI/',views.dataAPI.as_view()),
    path('logaout/', views.logouts, name="logout"),
    path('dudoanAPI', views.dudoanAPI.as_view(), name="dudoanAPI"),
]