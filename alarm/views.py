from django.shortcuts import render
import celery
from django_celery_beat.models import PeriodicTask
from django_celery_beat.models import CrontabSchedule
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def set_alarm(request):
    print("not doing it")
    return render(request, 'alarm/set_alarm.html')


def get_time_from_request(request):
    return request.POST['time'].split(':')

@csrf_exempt
def save_alarm(request):
    hour, minute = get_time_from_request(request)
    hour = str((int(hour) - 2) % 24) # Convert to Stockholm time
    schedule, created = CrontabSchedule.objects.get_or_create(hour=hour, minute=minute)
    PeriodicTask.objects.create(crontab=schedule, task='alarm.tasks.alarm', name='Alarm at {0}:{1}'.format(hour, minute))
    return render(request, 'alarm/set_alarm.html')
