#!/usr/bin/python
from fabric.api import *
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')

if os.path.isfile(dotenv_path):
    load_dotenv(dotenv_path)
else:
    dotenv_path = join('/data/scrapyd/', '.env')
    if os.path.isfile(dotenv_path):
        load_dotenv(dotenv_path)

env.user = os.environ.get('USER')
env.hosts = os.environ.get('HOSTS')
env.password = os.environ.get('PASSWORD')

@runs_once
def restart_image_service_task():
	print '-----------restarting connect server------------'
	sudo('supervisorctl restart crawler_handler_service')
	print '-----------server reconnected!------------------'

@task
def go():
	restart_image_service_task()