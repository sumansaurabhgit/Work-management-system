from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Worker(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)

    role = models.CharField(max_length=300, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True, default=3.7)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    assigned = models.ManyToManyField('Work', blank=True)
    AVAILABILITY_CHOICES = ((True, 'Yes'), (False, 'No'))


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']


class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    # number of workers required with default value 1
    numberOfWorker = models.IntegerField(default=1)
    startDate = models.DateField(default=timezone.now().date())
    duration = models.IntegerField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=300, null=True, blank=True)
    status = models.CharField(max_length=300, null=True, blank=True, default='pending')
    created = models.DateTimeField(auto_now_add=True)
    assignee = models.ManyToManyField(Worker, blank=True)



    STATUS_CHOICES = (('pending', 'Pending'), ('progress', 'In Progress'), ('completed', 'Completed'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']
