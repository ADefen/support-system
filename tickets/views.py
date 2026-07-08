from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from .services import classify_and_generate_response

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})
    
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})
    
def ticket_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if not title or not description:
            return render(request, 'tickets/ticket_form.html', {'error': 'Заполните все поля'})

        category, draft = classify_and_generate_response(title, description)

        Ticket.objects.create(
            title=title,
            description=description,
            status='new',
            category=category,
            draft_response=draft
        )
        return redirect('ticket_list')

    return render(request, 'tickets/ticket_form.html')
