from django.conf.urls import url
from user import views


app_name = 'user'
urlpatterns = [
    url(r'^registro/$', views.register, name='registro'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^userEdit/(?P<pk>\d+)$', views.userEdit, name='userEdit'),
    url(r'^userDelete/(?P<pk>\d+)$', views.userDelete, name='userDelete'),
    url(r'^aceitarUsuarios/$',views.listRequests,name='listRequests')

]
