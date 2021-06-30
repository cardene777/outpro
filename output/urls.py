from django.urls import path
from . import views

app_name = "output"

urlpatterns = [
    # Output
    path("output_list/", views.OutputList.as_view(), name="output_list"),
    path("output_detail/<int:pk>/", views.OutputDetail.as_view(), name="output_detail"),
    path("output_create/", views.OutputCreate.as_view(), name="output_create"),

    # Program
    path("code_list/<int:output_id>/", views.code_list, name="code_list"),
    path("code_detail/<int:pk>/", views.CodeDetail.as_view(), name="code_detail"),
]
