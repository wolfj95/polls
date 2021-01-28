from django.urls import path, include
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('past/', views.PastView.as_view(), name='past'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:day_id>/vote/', views.vote, name='vote'),
]

