"""expensetracker URL Configuration

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
from django.urls import path, re_path
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from expenses.models import Member, Category, Expense
from expenses.views import reports, expense_split_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="expenses/home.html")),
    path('member_create/', CreateView.as_view(
    		model=Member,
    		fields="__all__",
    		success_url="/members"
    	) ),
    re_path('member_update/(?P<pk>[0-9]+)/', UpdateView.as_view(
    		model=Member,
    		fields="__all__",
    		success_url="/members"
    	) ),
   	re_path('member_delete/(?P<pk>[0-9]+)/', DeleteView.as_view(
    		model=Member,
    		success_url="/members"
    	) ),
   	path('members', ListView.as_view(
    		model=Member,
    	) ),
   	path('categery_create/', CreateView.as_view(
    		model=Category,
    		fields="__all__",
    		success_url="/categeries"
    	) ),
    re_path('categery_update/(?P<pk>[0-9]+)/', UpdateView.as_view(
    		model=Category,
    		fields="__all__",
    		success_url="/categeries"
    	) ),
   	re_path('categery_delete/(?P<pk>[0-9]+)/', DeleteView.as_view(
    		model=Category,
    		success_url="/categeries"
    	) ),
   	path('categeries', ListView.as_view(
    		model=Category,
    	) ),

   	path('expense_create/', CreateView.as_view(
    		model=Expense,
    		fields="__all__",
    		success_url="/expenses"
    	) ),
    re_path('expense_update/(?P<pk>[0-9]+)/', UpdateView.as_view(
    		model=Expense,
    		fields="__all__",
    		success_url="/expenses"
    	) ),
   	re_path('expense_delete/(?P<pk>[0-9]+)/', DeleteView.as_view(
    		model=Expense,
    		success_url="/expenses"
    	) ),
    re_path('expense_split/([0-9]+)', expense_split_view),
   	path('expenses', ListView.as_view(
    		model=Expense,
    	) ),
   	path('reports', reports),
]
