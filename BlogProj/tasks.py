from celery.decorators import task
from celery.utils.log import get_task_logger
from blog.models import Entry

logger = get_task_logger(__name__)


@task(name="send_feedback_email_task")
def count_comments_for_entry(id):
    """sends an email when feedback form is filled successfully"""
    Entry.objects.filter(pk=id).update(comments_count=F('comments_count')+1)
    logger.info("id of news")
    return print('print')