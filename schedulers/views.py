from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SchedulerForm
from .models import Scheduler


# Create your views here.

# List out all the events from Database
@login_required
def scheduled_events(request):
    if request.method == 'GET':
        events = Scheduler.objects.all().values()
        context = {
            'events' : events,
        }
    return render(request, "schedulers/scheduled_events.html", context)


# Add the event to the database
@login_required
def add_event(request):
    if request.method == 'POST':
        form = SchedulerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scheduled_events')
    else:
        form = SchedulerForm()
    return render(request, 'schedulers/add_event.html', {'form' : form})


# Select the event to edit
@login_required
def edit_event(request, pk):
    event = get_object_or_404(Scheduler, pk=pk)

    if request.method == 'GET':
        form = SchedulerForm(request.GET, instance=event)
        context = {
                'pk' : pk,
                'form' : form,

            }
        return render(request, 'schedulers/update_event.html', context)

    return redirect('schedulers/scheduled_events.html')

# Update the selected event with the new details
@login_required
def update_event(request, pk):
    event = Scheduler.objects.all().filter(pk=pk)
    print(request.POST)
    if request.method == 'POST':

        data = request.POST
        event.update(event_name = data.get('event_name'))
        event.update(start_date = data.get('start_date'))
        event.update(end_date = data.get('end_date'))
        #event.save()
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
    event = get_object_or_404(Scheduler, pk=pk)
    if request.method == 'GET':
        event.delete()
        return redirect('scheduled_events')
    events = Scheduler.objects.all().values()
    context = {
        'events': events,}
    return render(request, 'scheduled_events.html', context)


@login_required
def analytics(request):
    records = Scheduler.objects.all()
    total_time_per_day = {}

    for record in records:
        start_date = record.start_date.date()
        end_date = record.end_date.date()

        # Calculate the time difference
        time_difference = record.end_date - record.start_date
        hours = time_difference.total_seconds() / 3600  # Convert to hours

        # Update the total time for the day
        if start_date not in total_time_per_day:
            total_time_per_day[start_date] = hours
        else:
            total_time_per_day[start_date] += hours

    # Convert the Dictionary into List
    output = []
    for date, hours in total_time_per_day.items():
        output.append({
            'day': date.strftime("%B %d, %Y"),
            'hours': round(hours,2)
        })

    return render(request, "schedulers/analytics.html", {'output': output})
