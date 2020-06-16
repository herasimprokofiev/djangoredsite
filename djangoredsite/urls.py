from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views import logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('thesitefolder.urls')),
    path('users/', include('users.urls')),  # /users/signup
    path('logout/', logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_field_name='main'),
         name='login'),
]
