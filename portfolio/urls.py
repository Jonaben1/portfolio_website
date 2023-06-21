from django.urls import path
from .views import project_list, full_view, ContactView


urlpatterns = [
    path('', project_list, name='index'),
    path('<int:pk>/', full_view, name='full_view'),
    path('contact', ContactView.as_view(), name='contact'),
]

