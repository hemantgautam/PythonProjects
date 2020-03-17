from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<list_id>', views.delete_items, name='delete_item'),
    path('cross_off/<list_id>', views.cross_off, name='cross_off'),
    path('uncross/<list_id>', views.uncross, name='uncross'),
    path('logout', views.logout, name='logout'),
    path('board/<board_id>/', views.board, name='board'),
    path('boards', views.boards, name='boards'),
    path('deleteboard/<board_id>', views.deleteboard, name='deleteboard'),
    path('addboard', views.addboard, name='addboard'),
    path('ajax_item_submit', views.ajax_item_submit, name='ajax_item_submit'),
]
