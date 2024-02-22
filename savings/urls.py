from django.urls import path
from . import views

urlpatterns = [
    path('total_savings/', views.total_savings, name='total_savings'),
    path('', views.index, name='index'),
    path('update_income/', views.update_income, name='update_income'),
    path('pay_saving/<int:saving_id>/', views.pay_saving, name='pay_saving'),
]
