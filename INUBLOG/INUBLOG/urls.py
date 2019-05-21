"""INUBLOG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import INUBLOG_APP.views

appViews = INUBLOG_APP.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appViews.mainPage, name = "mainPage"),
    path('new/', appViews.newContentsPage, name = "newContentsPage"),
    path('modify/<int:content_id>', appViews.modifyContentsPage, name = "modifyContentsPage"),
    path('login/', appViews.loginPage, name = "loginPage"),
    path('signUp/', appViews.signUpPage, name = "signUpPage"),
    path('main/detail/', appViews.detailPage, name = "detailPage"),
    path('create/', appViews.newContents, name = "createContents"),
    path('modified/<int:content_id>', appViews.modifiedContents, name = "modifiedContents"),
    path('delete/<int:content_id>', appViews.deleteContents, name = "deleteContents"),
]
