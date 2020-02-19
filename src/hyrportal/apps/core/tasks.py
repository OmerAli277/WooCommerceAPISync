
from datetime import timedelta
# from .woo_task import woo_fn_sync
from hyrportal.celery import app

@app.task
def see_you():
    # sync = woo_fn_sync()
    print("See you in ten seconds!")
    print('-----------------')
    print('Start syncing Customers')
    # sync.sync_customers()
    print('Start syncing products')
    # sync.sync_products()
    print('Start syncing orders')
    # sync.sync_orders()

app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "hyrportal.apps.core.tasks.see_you",
        "schedule": 10.0
    }
}