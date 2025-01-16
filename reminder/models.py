from django.db import models


class Schedule(models.Model):
    schedule_text = models.CharField(max_length=20)


class DateChoice(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    datechoice_text = models.DateField("date published")
