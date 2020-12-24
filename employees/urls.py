from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.employee_detail),
    path('prev_winners/', views.prev_winners),
]
