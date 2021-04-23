from django.conf.urls import url

from app1.views import page1View, page2View, page3View, page4View

app_name = 'app1'

urlpatterns = [
    url(r'^page1/$', page1View, name="page1"),  # Redis'e veri ekle linki
    url(r'^page2/$', page2View, name="page2"),  # Redis'teki verileri listeleme linki
    url(r'^page3/$', page3View, name="page3"),  # Redis'teki veriyi silme linki
    url(r'^page4/$', page4View, name="page4"),  # Redis'teki tüm anahtarları(Key) getirme linki
]
