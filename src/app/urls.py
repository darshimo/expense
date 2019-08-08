"""project URL Configuration

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
from .views import ExpenseList, ExpenseCreate, ExpenseUpdate, ExpenseDelete, ExpenseDetail

urlpatterns = [
    path('list/', ExpenseList.as_view(), name='list'),
    path('create/', ExpenseCreate.as_view(), name='create'),
    path('update/<int:pk>', ExpenseUpdate.as_view(), name='update'),
    path('delete/<int:pk>', ExpenseDelete.as_view(), name='delete'),
    path('detail/<int:pk>', ExpenseDetail.as_view(), name='detail'),
]
