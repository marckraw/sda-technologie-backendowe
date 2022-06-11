from django.contrib import admin
from django.urls import include, path
from mysite import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('admin/', admin.site.urls),
    path('api/', include('polls.urls_api')),
    path('polls/', include('polls.urls')),
    path('polls/', include('polls.urls_class')),
    path('movies/', include('movies.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls'))
]
