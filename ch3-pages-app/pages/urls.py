from django.urls import path

from .views import AboutPageView, HomePageView, FilmsPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('films/', FilmsPageView.as_view(), name='films' ),
    path('base/', FilmsPageView.as_view(), name='base' )
]
