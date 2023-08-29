from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Thesis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Account Auth.
    path('accounts/signup/', views.signup, name='signup'),
    path('', include('Thesis.urls')),  # Including the Thesis app's URLs here
    path('user_tezleri/', views.user_tezleri, name='user_tezleri'),
    path('accounts/logout/', views.custom_logout, name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)