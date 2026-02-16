from django.shortcuts import render
from django.views import View


def get_all_tickets(request):
    return render(request, 'ticket/listing.html',{})

class GetAllTicketsView(View):
    """Class to render all ticket."""
    def get(self,request):
        return render(request,'ticket/listing.html')
