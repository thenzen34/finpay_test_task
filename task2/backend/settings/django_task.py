import os

from .settings import *

INSTALLED_APPS.append('django_task')
TEMPLATES[0]['DIRS'].append(os.path.join('django_task', 'templates'))
