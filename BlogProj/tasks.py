from __future__ import absolute_import, unicode_literals
from .celery import app


@app.task
def count_comments(x, y):
    return x + y
