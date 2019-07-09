#coding=utf-8
__author__ = 'Li Baoshan'
__date__ = "2019/5/18 15:53"
from django.urls import path,include,re_path
from .views import OrgView,AddUserAskView,OrgHomeView,OrgCourseView,OrgDescView,\
    OrgTeacherView,AddFavView,TeacherListView,TeacherDetailView

#课程机构首页
app_name = 'organization'

urlpatterns = [
    path('list/', OrgView.as_view(), name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name='add_ask'),
    re_path(r'^home/(?P<org_id>\d+)/$',OrgHomeView.as_view(),name="org_home"),
    re_path(r'^course/(?P<org_id>\d+)/$',OrgCourseView.as_view(),name="org_course"),
    re_path(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),
    #教师详情页，不同于下
    re_path(r'^org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="org_teacher"),
    #机构收藏
    path('add_fav/', AddFavView.as_view(), name='add_fav'),

    #讲师列表页
    path('teacher/list/', TeacherListView.as_view(), name='teacher_list'),

    #教师详情页
    re_path(r'^teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name="teacher_detail"),

]