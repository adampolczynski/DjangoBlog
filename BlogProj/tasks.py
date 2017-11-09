# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.decorators import task
from blog.models import Entry

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@task
def count_comments_for_entry(id):
    """sends an email when feedback form is filled successfully"""
    entry = Entry.objects.get(pk=id)#.update(comments_count=4)#F('comments_count')+1)
    entry.comments_count=entry.comments_count+1
    entry.save()
    return 'something'