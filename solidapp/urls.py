from django.urls import path
from . import views

app_name = "solidapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("inspire", views.inspire, name="inspire"),
    path("getInspired", views.gotInspired, name="getInspired"),
    path("story/<int:id>/", views.story, name="story"),
]
