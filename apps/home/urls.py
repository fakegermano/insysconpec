from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'insysconpec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'$', 'apps.home.views.home'),
)
