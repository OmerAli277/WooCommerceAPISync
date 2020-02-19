<<<<<<< HEAD
from celery import Celery
from datetime import timedelta
from hyrportal.apps.core.woo_task import woo_fn_sync
from hyrportal.apps.core.models import WooCommerceDetails
from django.db import DatabaseError

=======
>>>>>>> 6fbfd5de85c2e5ac57a227b62f3caf69e66541dc

from datetime import timedelta
# from .woo_task import woo_fn_sync
from hyrportal.celery import app

@app.task
def see_you():
<<<<<<< HEAD
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
=======
    # sync = woo_fn_sync()
    print("See you in ten seconds!")
    print('-----------------')
    print('Start syncing Customers')
    # sync.sync_customers()
    print('Start syncing products')
    # sync.sync_products()
    print('Start syncing orders')
    # sync.sync_orders()
>>>>>>> 6fbfd5de85c2e5ac57a227b62f3caf69e66541dc

app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "hyrportal.apps.core.tasks.see_you",
        "schedule": 10.0
    }
}