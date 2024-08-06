from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('user/trees/', views.user_planted_trees, name='user_planted_trees'),
    path('tree/<int:tree_id>/', views.planted_tree_detail, name='planted_tree_detail'),
    path('tree/add/', views.add_planted_tree, name='add_planted_tree'),
    path('account/trees/', views.account_planted_trees, name='account_planted_trees'),
    path('api/user/trees/', views.UserPlantedTreesView.as_view(), name='api_user_planted_trees'),
]
