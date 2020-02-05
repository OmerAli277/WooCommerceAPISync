from celery import Celery
from datetime import timedelta
from hyrportal.celery import app


@app.task
def see_you():
    print("See you in ten seconds!")

app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "core.see_you",
        "schedule": 10.0
    }
}