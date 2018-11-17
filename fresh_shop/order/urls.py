
from django.conf.urls import url

from order import views

urlpatterns = [
    # 下单
    url(r'^order/', views.order, name='order'),
]

