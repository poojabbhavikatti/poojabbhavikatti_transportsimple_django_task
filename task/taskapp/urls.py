from django.urls import path
from taskapp import views
app_name="taskapp"

urlpatterns=[
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('ask/', views.ask_question, name='ask_question'),
    path('answer/', views.answer_question, name='answer'),
    path('answer/like/', views.like_answer, name='like_answer'),
]  

# <int:question_id>/              like/<int:answer_id>/
