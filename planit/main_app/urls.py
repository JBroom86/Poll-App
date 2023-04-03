from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('events/', views.events_index, name='index'),
    path('events/<int:event_id>/', views.events_detail, name='detail'),
    path('events/<int:event_id>/assoc_group/<int:group_id>/',
         views.assoc_group, name='assoc_group'),
    path('events/<int:event_id>/unassoc_group/<int:group_id>/',
         views.remove_group, name='remove_group'),
    path('groups/', views.GroupList.as_view(), name='groups_index'),
    path('groups/<int:pk>/', views.GroupDetail.as_view(), name='groups_detail'),
    path('groups/create/', views.GroupCreate.as_view(), name='groups_create'),
    path('groups/<int:pk>/update/',
         views.GroupUpdate.as_view(), name='groups_update'),
    path('groups/<int:pk>/delete/',
         views.GroupDelete.as_view(), name='groups_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
