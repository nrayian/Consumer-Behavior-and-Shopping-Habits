from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('make-prediction/', views.make_prediction, name='make-prediction'),
    path('prediction-history/', views.prediction_history,
         name='prediction-history'),
    path('prediction/', views.prediction, name='prediction'),
    path('feedback/', views.feedback, name='feedback')
]
