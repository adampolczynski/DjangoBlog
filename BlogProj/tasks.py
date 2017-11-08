from celery.decorators import task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@task(name="send_feedback_email_task")
def count_comments_for_entry(id):
    """sends an email when feedback form is filled successfully"""
    logger.info("id of news")
    return print('print')