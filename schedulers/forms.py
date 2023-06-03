from django import forms
from .models import Scheduler
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class SchedulerForm(forms.ModelForm):
    class Meta:
        model = Scheduler
        fields = ['event_name', 'start_date', 'end_date']

        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date' : DateTimePickerInput(options={
                    "format": "YYYY-MM-DD hh:mm:ss"}, attrs={'class': 'form-control datetimepicker-input', 'data-target': '#start_date_picker'}),

            'end_date': DateTimePickerInput(options={
                    "format": "YYYY-MM-DD hh:mm:ss"}, attrs={'class': 'form-control datetimepicker-input', 'data-target': '#start_date_picker'}),

        }



