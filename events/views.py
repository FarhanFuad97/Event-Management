from django.shortcuts import render, redirect
from events.models import Event, Participant, Category
from events.forms import EventForm, ParticipantForm, CategoryForm
from django.utils.timezone import now
from django.contrib.auth.decorators import user_passes_test, login_required,permission_required
from users.views import is_admin
def is_organizer(user):
    return user.groups.filter(name='Organizer').exists()

def is_Participant(user):
    return user.groups.filter(name='Participant').exists()

@user_passes_test(is_organizer, login_url='no-permission')
def organizer_dashboard(request):
    total_participants = Participant.objects.count()
    total_events = Event.objects.count()
    
    upcoming_events = Event.objects.filter(date__gte=now().date()).count()
    past_events = Event.objects.filter(date__lt=now().date()).count()

    
    filter_type = request.GET.get('filter', 'all')

    
    if filter_type == 'upcoming':
        filtered_events = Event.objects.filter(date__gte=now().date())
    elif filter_type == 'past':
        filtered_events = Event.objects.filter(date__lt=now().date())
    else:
        filtered_events = Event.objects.all()

    todays_events = Event.objects.filter(date=now().date())

    context = {
        'total_participants': total_participants,
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'todays_events': todays_events,
        'filtered_events': filtered_events,
        'all_events': Event.objects.all(),
        'today': now().date(),
        'filter_type': filter_type
    }

    return render(request, 'dashboard.html', context)

# ///--- Category CRUD ---///
# @login_required
# @permission_required("events.view_event",login_url ='no-permission')
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'events/category_list.html', {'categories': categories})
@login_required
@permission_required("events.add_event",login_url ='no-permission')
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'events/category_form.html', {'form': form})

@login_required
@permission_required("events.change_event",login_url ='no-permission')
def category_update(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'events/category_form.html', {'form': form})

@login_required
@permission_required("events.delete_event",login_url ='no-permission')
def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect('category_list')
    return render(request, 'events/category_confirm_delete.html', {'category': category})


# ///--- Event CRUD ---///
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

@login_required
@permission_required("events.add_event",login_url ='no-permission')
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

@login_required
@permission_required("events.change_event",login_url ='no-permission')
def event_update(request, pk):
    event = Event.objects.get(pk=pk) 
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

@login_required
@permission_required("events.delete_event",login_url ='no-permission')
def event_delete(request, pk):
    event = Event.objects.get(pk=pk) 
    if request.method == "POST":
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})


# ///--- Participant CRUD ---///
# @login_required
# @permission_required("events.view_event",login_url ='no-permission')
def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'events/participant_list.html', {'participants': participants})



def participant_create(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'events/participant_form.html', {'form': form})



def participant_update(request, pk):
    participant = Participant.objects.get(pk=pk) 
    if request.method == "POST":
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'events/participant_form.html', {'form': form})


def participant_delete(request, pk):
    participant = Participant.objects.get(pk=pk)
    if request.method == "POST":
        participant.delete()
        return redirect('participant_list')
    return render(request, 'events/participant_confirm_delete.html', {'participant': participant})




from django.shortcuts import render

def home_view(request):
    return render(request, "home.html") 



from django.shortcuts import redirect
@login_required
def dashboard(request):
    if is_organizer(request.user):
        return redirect('organizer_dashboard')
    elif is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_Participant(request.user):
        return redirect('event_list')
    return redirect('no-permission')
    
















