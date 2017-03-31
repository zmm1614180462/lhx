from django.conf.urls import url, include
from student import views
#通用视图
# from .views import index
from django.views.generic import TemplateView,RedirectView


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^archive/$', views.archive, name='archive'),
    # url(r'^about$',views.about, name='about'),
    # url(r'^article/$', views.article, name='article'),
    # url(r'^title/$', views.title, name='article'),
    # url(r'^comment/post/$', views.comment_post, name='comment_post'),
    # url(r'^logout$', views.do_logout, name='logout'),
    # # url(r'^reg', do_reg, name='reg'),
    # # url(r'^login', do_login, name='login'),
    # url(r'^category/$', views.category, name='category'),
    # url(r'^my/test$',TemplateView.as_view(template_name='wx/article.html')),

]