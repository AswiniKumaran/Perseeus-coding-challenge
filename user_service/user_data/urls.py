from django.conf.urls import url
from user_data.views import *

urlpatterns=[
    url(r'users/$', UserListView.as_view()),
    url(r'users/(?P<pk>\d+)/$', UserView.as_view()),
    url(r'mails/$', EmailListView.as_view()),
    url(r'mails/(?P<pk>\d+)/$', EmailView.as_view()),
    url(r'numbers/$', PhoneNumberListView.as_view()),
    url(r'numbers/(?P<pk>\d+)/$', PhoneNumberView.as_view()),
]
