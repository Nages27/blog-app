from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.home_view,name='home'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('process-login/', views.process_login, name='process_login'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('new-blog/', views.new_blog, name='new_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),

]