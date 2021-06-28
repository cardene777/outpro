from django.urls import path
from . import views

app_name = "output"

urlpatterns = [
    # Output
    path("output_list/", views.OutputList.as_view(), name="output_list"),
    path("output_detail/<int:pk>/", views.OutputDetail.as_view(), name="output_detail")
]
