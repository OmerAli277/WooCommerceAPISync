from celery import Celery
from datetime import timedelta
from hyrportal.apps.core.woo_task import woo_fn_sync
from hyrportal.apps.core.models import WooCommerceDetails
from django.db import DatabaseError
from datetime import date

from datetime import timedelta
import pytz

# from .woo_task import woo_fn_sync
from hyrportal.celery import app

@app.task
def see_you():
    woo_details = None
    start_date = None
    try:
        woo_details = WooCommerceDetails.objects.get(id=1)
        fn_object = fortnoxSettings.objects.get(seller_id = seller_id1)
        start_date = fn_object.start_date
    except DatabaseError as e:
        print('Database error: ' + str(e))

    local_tz = pytz.timezone('Europe/Austria')
    loacl_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)

    if start_date and start_date <=  loacl_dt
        if woo_details is not None:
            sync = woo_fn_sync(woo_details.p_url, woo_details.p_consumer_key, woo_details.p_consumer_secret)
            print("See you in ten seconds!")
            print('-----------------')
            print('Start syncing Customers')
            sync.sync_customers()
            print('Start syncing products')
            sync.sync_products()
            print('Start syncing orders')
            sync.sync_orders()

app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "hyrportal.apps.core.tasks.see_you",
        "schedule": 10.0
    }
}