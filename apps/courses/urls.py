#coding=utf-8
__author__ = 'Li Baoshan'
__date__ = "2019/5/26 13:51"

from django.urls import path,include,re_path

from courses.views import CourseListView,CourseDetailView,CourseInfoView,VideoPlayView


app_name = 'courses'

urlpatterns = [
    #课程列表页
    path('list/', CourseListView.as_view(), name='course_list'),
    #课程详情页
    re_path(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
    re_path(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),
    re_path(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video_play"),
]