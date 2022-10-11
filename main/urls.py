from django.urls import path,include
from main.views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('get_head/', HeaderView.as_view()),
    path('team/', TeamView.as_view()),
    path('team/<int:pk/', TeamDetail.as_view()),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('all-auth/', include('allauth.urls'))
]
urlpatterns = format_suffix_patterns(urlpatterns)
