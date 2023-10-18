"""
URL configuration for admin_panel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from index.views import *


handler404 = "index.views.error"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login, name="login"),
    path("logout/", logout, name="logout"),
    path("index/", index, name="index"),
    path("add_client/", add_client, name="add_client"),
    path("client_delete/<int:client_id>", delete_client, name="delete_client"),
    path("edit_client/<int:client_id>", edit_client, name="edit_client"),
    path(
        "add_notification_chanels/<int:client_id>",
        add_notification,
        name="addnotification",
    ),
    path(
        "edit_notification_chanels/<int:client_id>",
        edit_notification_channels,
        name="edit_notification",
    ),
    path("add_filter_word/<int:client_id>", add_filter_words, name="add_filter_word"),
    path(
        "edit_filter_word/<int:client_id>/<int:word_id>",
        edit_filter_word,
        name="edit_filter_word",
    ),
    path("filter_word_list/<int:client_id>", filter_word_list, name="filter_word_list"),
    path(
        "delete_filter_word/<int:word_id>/<int:client_id>/",
        delete_filter_word,
        name="delete_word",
    ),
]
