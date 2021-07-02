from django.urls import path
from . import views

app_name = "output"

urlpatterns = [
    # Output
    path("output_list/", views.OutputList.as_view(), name="output_list"),
    path("output_detail/<int:pk>/", views.OutputDetail.as_view(), name="output_detail"),
    path("output_update/<int:pk>/", views.OutputUpdate.as_view(), name="output_update"),
    path("output_delete/<int:pk>/", views.OutputDelete.as_view(), name="output_delete"),
    path("output_create/", views.OutputCreate.as_view(), name="output_create"),

    # Program
    path("code_list/<int:output_id>/", views.code_list, name="code_list"),
    path("code_detail/<int:pk>/", views.CodeDetail.as_view(), name="code_detail"),
    path("code_update/<int:pk>/<int:output_id>/<slug:good>/", views.CodeUpdate.as_view(), name="code_update"),
    path("code_delete/<int:pk>/<int:output_id>/", views.CodeDelete.as_view(), name="code_delete"),
    path("code_create/<int:output_id>/", views.CodeCreate.as_view(), name="code_create"),

    # good
    path("good/", views.good, name="good"),
]
