from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [



    url(r'^$', views.home_page, name='home_page'),

# BEGIN_OF_CODE_GENERATION

# END_OF_CODE_GENERATION

    url(r'^user/profile$', views.user_profile, name='user-profile'),
    url(r'^user/update/$', views.user_update, name='user_update'),
    url(r'^user/password/$', views.change_password, name='user_password_change'),

]