"""assembly_stuff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('member/<int:pk>', views.MemberDetailView.as_view(), name='member-detail'),
    path('member/', views.MemberListView.as_view(), name='member-list'),
    path('member/create', views.MemberCreateView.as_view(), name='member-create' ),
    path('member/delete/<int:pk>', views.MemberDeleteView.as_view(), name='member-delete')
]
