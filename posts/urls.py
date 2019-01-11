from posts import views
from django.urls import path
from .views import (
	post_list,

	)
from django.conf.urls import url

app_name='post'

urlpatterns = [

    #
    path("", post_list, name = "index"),

    # path("", views.search(), name = "search"),

    path('<int:pk>/', views.Detailview.as_view(), name = "detail"),

    path('add/', views.PostCreate.as_view(), name='post-add'),

]