from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("add-record", views.add_record, name="add_record"),
    path("update-record/<int:pk>/", views.update_record, name="update_record"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("delete/<int:pk>/", views.delete_record, name="delete"),
    path("record-detail/<int:pk>/", views.record_detail, name="record_detail")
]
