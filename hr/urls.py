from django.urls import path
from hr import views

urlpatterns = [
    path('hrdash/', views.hrHome_views, name='hrdash'),
    path('candidate-details/', views.candidate_view, name='candidate_details'),
    path('postjob/', views.post_job_views, name='post_job'),
    path('acceptapplication/', views.acceptApplication, name='acceptapplication')

]
