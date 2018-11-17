
from django.conf.urls import url

from cart import views

urlpatterns = [
    # 加入购物车
    url(r'add_cart/', views.add_cart, name='add_cart'),
    # 购物车
    url(r'cart/', views.cart, name='cart'),
    # 结算
    url(r'place_order/', views.place_order, name='place_order'),
    url(r'^count/', views.count, name='count'),
    # 购物车+-商品
    url(r'^add_good_num/', views.add_good_num, name='add_good_num'),
    url(r'^sub_good_num/', views.sub_good_num, name='sub_good_num'),
    # <li>的商品选中修改is_select状态
    url(r'^is_select/', views.is_select, name='is_select'),
    url(r'^is_select_foo/', views.is_select_foo, name='is_select_foo'),
]