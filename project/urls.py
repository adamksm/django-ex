
from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin


from welcome.views import index, health


urlpatterns = [
    # Examples:
    # re_path(r'^$', 'project.views.home', name='home'),
    # re_path(r'^blog/', include('blog.urls')),

    re_path(r'^$', index),
    re_path(r'^health$', health),
    re_path(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
