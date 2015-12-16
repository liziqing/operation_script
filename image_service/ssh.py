#!/usr/bin/python
from fabric.api import *

env.user = 'transdoing'
env.hosts = ['127.0.0.1']
env.password = 'bueller'

@runs_once
def restart_image_service_task():
	print 'restarting connect server'
	sudo('supervisorctl restart crawler_handler_service')
	print 'server connected!'

@task
def go():
	restart_image_service_task()