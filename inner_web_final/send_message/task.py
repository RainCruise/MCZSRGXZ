#coding = utf-8
from celery.decorators import task

@task
def send(a):
    return a