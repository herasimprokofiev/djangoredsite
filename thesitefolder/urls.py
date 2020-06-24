from django.urls import path, include 

from .views import MainPageView, SPageView, TPageView, NewsFieldDetail, NewsFieldUpdate, NewsFieldDelete


urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('s', SPageView.as_view(), name='s'),
    path('t', TPageView.as_view(), name='t'),
    path('t/<int:pk>', NewsFieldDetail.as_view(), name='nf_detail'),
    path('t/<int:pk>/edit/', NewsFieldUpdate.as_view(), name='nf_edit'),
    path('t/<int:pk>/delete/', NewsFieldDelete.as_view(), name='nf_delete'),
]
