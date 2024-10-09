# flake8: noqa
# Basic Lib Import

from django.urls import include, path
from myapp.views import *

# Routing Implement
urlpatterns = [
       path('dashboard/', dashboard, name='dashboard'),
       path('users/', user_list, name='users'),
       path('verify/<str:id>/', verify_user, name='verify-user'),

       path('groups/', groups, name='groups'),
       path('communities/', communities, name='communities'),
       path('creatCommunities/', creatCommunities, name='creatCommunities'),
       path('blogs_category/', blogs_category, name='blogs-category'),
       path('creatBlogCategory/', creatBlogCategory, name='creatBlogCategory'),
       path('blogs-category-delete/<int:id>', blogs_category_delete, name='blogs-category-delete'),
       path('blogs_delete/<int:id>', blogs_delete, name='blogs_delete'),
       path('blogs/', blogs, name='blogs'),
       path('creatBlog/', creatBlog, name='creatBlog'),
       path('compliance/', compliance, name='compliance'),
       path('selfie/', selfie, name='selfie'),
       path('selfieApprove/', selfieApprove, name='selfieApprove'),
       path('suspect/', suspect, name='suspect'),
       path('category/', category, name='category'),
       path('creatCategory/', creatCategory, name='creatCategory'),
       path('badges/', badges, name='badges'),
       path('badges/create', badges_create, name='badges_create'),
       path('badges/delete/', badge_delete, name='delete-badge'),
       # path('users/', welcome, name='users'),
       # path('users/', welcome, name='users'),
       # path('welcome/', welcome, name='welcome'),
    
]


