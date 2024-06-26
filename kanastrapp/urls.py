from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('charges', views.addPerson),
    path('read',views.getPeople),
    path('', TemplateView.as_view(template_name='index.html'))
]