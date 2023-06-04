from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SchedulerForm
from .models import Scheduler
from django.utils.timezone import now, timedelta
from django.contrib import messages
from datetime import datetime


# Create your views here.

# List out all the events from Database
@login_required
def scheduled_events(request):
    if request.method == 'GET':
        events = Scheduler.objects.filter(user=request.user).values()
        context = {
            'events' : events,
            'user' : str(request.user).title()
        }
    return render(request, "schedulers/scheduled_events.html", context)


# Add the event to the database
@login_required
def add_event(request):
    msg = None
    events = Scheduler.objects.all()
    if request.method == 'POST':
        form = SchedulerForm(request.POST)
        if form.is_valid():
            data = request.POST
            #print(data)
            events = Scheduler.objects.filter(start_date=data['start_date'])
            if events:
                for event in events:
                    if not ((str(event.start_date.strftime("%Y-%m-%d %H:%M:%S")) == data['start_date']) and (str(event.end_date.strftime("%Y-%m-%d %H:%M:%S")) == data['end_date'])):
                        print(type(data['start_date']), type(str(event.start_date.strftime("%Y-%m-%d %H:%M:%S"))))
                        form.save()
                    else:
                        messages.error(request, 'Event already exists with same start date and end date')
                        form = SchedulerForm()
                        return render(request, 'schedulers/add_event.html', {'form' : form, "msg": msg, 'events' : events})
            else:
                form.save()

            return redirect('scheduled_events')
    else:
        form = SchedulerForm()
    return render(request, 'schedulers/add_event.html', {'form' : form, 'events' : events})


# Select the event to edit
@login_required
def edit_event(request, pk):
    event = get_object_or_404(Scheduler, pk=pk)

    if request.method == 'GET':
        form = SchedulerForm(request.GET, instance=event)
        context = {
                'pk' : pk,
                'form' : form,
                'event' : event

            }
        return render(request, 'schedulers/update_event.html', context)

    return redirect('schedulers/scheduled_events.html')

# Update the selected event with the new details
@login_required
def update_event(request, pk):
    event = Scheduler.objects.all().filter(user=request.user, pk=pk)
    print(request.POST)
    data = request.POST
    if request.method == 'POST' and (data.get('start_date') <= data.get('end_date') ):
        event.update(user=data.get('user'))
        event.update(event_name = data.get('event_name'))
        event.update(start_date = data.get('start_date'))
        event.update(end_date = data.get('end_date'))

        return redirect('scheduled_events')
    else:
        events = Scheduler.objects.all().values()
        context = {
                'events': events,}
        return render(request, 'schedulers/update_event.html', context)

    return redirect('scheduled_events')



# Delete the selected event from the database
@login_required
def delete_event(request, pk):

    # Fetch the relevant data from the model
    event = get_object_or_404(Scheduler, pk=pk)

    # Delete the selected event from the database
    if request.method == 'GET':
        event.delete()
        return redirect('scheduled_events')
    events = Scheduler.objects.all().values()
    context = {
        'events': events,}
    return render(request, 'scheduled_events.html', context)


@login_required
def analytics(request):
    end_date = now().date()
    start_date = end_date - timedelta(days=30)

    # Fetch the relevant data from the model
    data = Scheduler.objects.filter(user=request.user, start_date__gte=start_date)

    # Calculate teh hours for that day
    results = {}
    for entry in data:
        day = entry.start_date.date()
        duration = entry.end_date - entry.start_date
        hours = duration.total_seconds() / 3600  # Convert to hours
        if day in results:
            results[day] += hours
        else:
            results[day] = hours
    # Convert the Dictionary into List
    output = []
    for date, hours in results.items():
        output.append({
            'day': date.strftime("%B %d, %Y"),
            'hours': round(hours,2)
        })

    return render(request, "schedulers/analytics.html", {'output': output})
