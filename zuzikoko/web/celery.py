import os
from celery import Celery
from django.conf import settings

#when local set to settings.local, when in production set to settings.prod
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings.prod') #command line program
app = Celery('web') #creating the instance of the application
#app = Celery('web', backend='rpc://', broker='amqp://myuser:mypassword@rabbitmq:5672')
app.config_from_object('django.conf:settings', namespace='CELERY') #loading custom conf
#app.control.purge()
#app.autodiscover_tasks(lambda: [n.name for n in app.get_app_configs()])
app.autodiscover_tasks()
#app.tasks.register())

    
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))