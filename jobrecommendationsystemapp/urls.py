from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/',views.about_view, name='about'),
    path('ourservices/',views.services_view,name='services'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('options/',views.options_view,name='options_page'),
    path('predict/', views.predict_view, name='predict_view'),
    path('enterdetails/', views.enter_details, name='enter_details'),
    path('uploadresume/', views.upload_resume, name='upload_resume'),
    path('result/',views.result_view,name='results'),
    path('logout/', views.logout_view, name='logout'),
]
