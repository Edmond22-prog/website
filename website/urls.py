from django.urls import path
from . import views
from .views import PortfolioDetailView

urlpatterns = [
    path('', views.index, name="home"),
    path('portfolio/<int:pk>/detail', PortfolioDetailView.as_view(), name="portfolio-detail"),

]