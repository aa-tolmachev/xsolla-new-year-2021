from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('employees/', include('employees.urls')),
]
