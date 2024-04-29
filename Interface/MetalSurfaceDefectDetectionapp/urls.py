from django.urls import path
from MetalSurfaceDefectDetectionapp import views

app_name="detection"

urlpatterns = [
    path("predict/", views.predict, name="predict"),
    path("classes/", views.list_classes, name="list_classes"),
    
]
