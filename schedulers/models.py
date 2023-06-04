from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Scheduler(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def clean(self):
        super().clean()
        if self.start_date == self.end_date:
            raise ValidationError("Start Date and End Date should not be same")
        elif not ( self.start_date <= self.end_date):
            raise ValidationError("End Date must be greater than Start Date")


