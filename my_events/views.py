from django.shortcuts import render, get_object_or_404
from django import forms
from .models import Event
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import json

class AddEventForm(forms.ModelForm):
    """
    Event form for adding a new Event
    """
    class Meta:
        model = Event
        exclude = ['is_liked']
        widgets = {
            "data": forms.Textarea(),
            "time": forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),

        }

def index(request): 
    """
    Renders the events stored in the database
    """
    # like button ajax request handling
    if request.method == "POST":
        if request.POST.get("operation") == "like_event":
            # swapping the like of the event
            event_id = request.POST.get("event_id")
            event = get_object_or_404(Event, pk=event_id)
            event.is_liked = not event.is_liked
            event.save()
            
            # json response
            data = {
                "is_liked": event.is_liked,
                "event_id": event_id
            }
            return HttpResponse(json.dumps(data), content_type="json")

    return render(request, 'my_events/index.html', {
        "events": Event.objects.all()
    })

def add(request): 
    """
    A form for adding more events to the database
    """
    # processing the input
    if request.method == "POST":
        form = AddEventForm(request.POST, request.FILES)
        form.is_liked = False
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'my_events/add.html', {
                "form": form
            })
    
    return render(request, 'my_events/add.html', {
        "form": AddEventForm()
    })

