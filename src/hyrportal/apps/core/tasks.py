from celery import Celery
from datetime import timedelta
from hyrportal.apps.core.woo_task import woo_fn_sync
from hyrportal.apps.core.models import WooCommerceDetails
from django.db import DatabaseError


app = Celery()
app.config_from_object('celeryconfig', namespace='CELERY')

@app.task
def see_you():
    woo_details = None
    try:
        woo_details = WooCommerceDetails.objects.get(id=1)
    except DatabaseError as e:
        print('Database error: ' + str(e))

    if woo_details is not None:
        sync = woo_fn_sync(woo_details.p_url, woo_details.p_consumer_key, woo_details.p_consumer_secret)
        print("See you in ten seconds!")
        print('-----------------')
        print('Start syncing Customers')
        sync.sync_customers()
        print('Start syncing products')
        # sync.sync_products()
        print('Start syncing orders')
        # sync.sync_orders()

app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "core.see_you",
        "schedule": 10.0
    }
}