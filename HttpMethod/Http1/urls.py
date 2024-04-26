from django.urls import path
from . import views

urlpatterns = [
    path("GET&POST/",views.method1, name="GP"),
    path("Home/",views.simple, name='Home'),
    path('<int:id>/', views.method2, name='update_data'), 
    path('', views.method2, name='data_insert'),
    path('delete/<int:id>/', views.method3, name='data_delete'), 
    path('view/',views.my_view),
    path('view1/',views.response_error_handler),
    path('date&time/',views.current_datetime)
]