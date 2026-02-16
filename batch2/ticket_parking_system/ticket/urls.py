from django.urls import path
from . import views

urlpatterns = [
    path('',views.GetAllTicketsView.as_view(), name='ticket_list'),
    # path('',views.get_all_tickets, name='ticket_list'),
]