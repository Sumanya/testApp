from re import template
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
from .views import index

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', index)
]


urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]

# urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {"document_root": settings.STATIC_ROOT}),
#         re_path(r'^.*$', TemplateView.as_view(template_name='base.html'),)
# ]

