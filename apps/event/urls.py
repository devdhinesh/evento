

from unicodedata import name
from django.urls import path,include
from .views import (home,signup,application,dashboard,createevent,
                    editevent,assignments,assign_people,
                    assignments_api,delete_volunteer,deleteevent)

from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='event/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('apply/<str:unique_id>/',application,name='application'), 
    path('dashboard/',dashboard,name='dashboard'),
    path('dashboard/create-event/',createevent,name='createevent'),
    path('dashboard/event/<str:unique_id>/edit/',editevent,name='editevent'),
    path('dashboard/event/<str:unique_id>/delete/',deleteevent,name='deleteevent'),
    path('dashboard/event/<str:unique_id>/applicants/',assignments,name='assignments'),

    path('dashboard/assign/',assign_people,name='assign_people'),
    path('event/get-details/',assignments_api,name='assignments_api'),
    path('delete-volunteer/',delete_volunteer,name='delete_volunteer'),

    
]
