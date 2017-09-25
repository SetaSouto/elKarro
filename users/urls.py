from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^$', views.Homeview.as_view(), name="home"),
    url(r'^create$', views.CreateOrderView.as_view(), name="create"),
    url(r'^deliver$', views.DeliverOrderView.as_view(), name="deliver")
]
