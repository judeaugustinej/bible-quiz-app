from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^students/$', views.students, name='students'),
    url(r'^students/(?P<pk>\d+)/$', views.student_detail, name='student_detail'),
    url(r'^students/(?P<pk>\d+)/edit/$', views.student_edit, name='student_edit')
]

