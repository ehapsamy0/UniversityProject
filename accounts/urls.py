from django.urls import path


from .views import login_page,all_doctors,all_teaching_assistants,all_users,add_new_user


app_name = 'accounts'


urlpatterns = [
    path('',login_page,name='login_page'),
    path('all/users/',all_users,name='all_users'),
    path('all/users/add/',add_new_user,name='add_new_user'),
    path('all_doctors/',all_doctors,name='all_doctors'),
    path('all_teaching_assistants/',all_teaching_assistants,name='all_teaching_assistants'),
]