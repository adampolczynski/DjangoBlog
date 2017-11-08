from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('proj',
	broker='amqp://localhost',
	backend='amqp://localhost',
	include=['BlogProj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
	result_expires=3600,
	)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))