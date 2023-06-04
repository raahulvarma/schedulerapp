from django import forms
from .models import Scheduler
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class SchedulerForm(forms.ModelForm):
    class Meta:
        model = Scheduler
        fields = [ 'user', 'event_name', 'start_date', 'end_date']

        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date' : DateTimePickerInput(options={
                    "format": "YYYY-MM-DD hh:mm:ss"}, attrs={'class': 'form-control'}),

            'end_date': DateTimePickerInput(options={
                    "format": "YYYY-MM-DD hh:mm:ss"}, attrs={'class': 'form-control'}),

        }





