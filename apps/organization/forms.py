#coding=utf-8
__author__ = 'Li Baoshan'
__date__ = "2019/5/18 16:40"
from django import forms
from django.forms import ModelForm
from operation.models import UserAsk

import re

#利用ModelFrom将Model转化为form,不再继承form.Form
class UserAskForm(ModelForm):
    class Meta:
        model=UserAsk
        fields=['name','mobile','course_name']

    def clean_mobile(self):
        """
        验证手机号码是否合法
        """
        mobile=self.cleaned_data['mobile']
        REGEX_MOBILE="^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p=re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码非法',code="mobile_invalid")

