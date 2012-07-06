import os
import sys
sys.path.append('/usr/local/src')
sys.path.append('/usr/local/src/osqa')
# The first part of this module name should be identical to the directory name
# of the OSQA source.  For instance, if the full path to OSQA is
# /home/osqa/osqa-server, then the DJANGO_SETTINGS_MODULE should have a value
# of 'osqa-server.settings'.
os.environ['DJANGO_SETTINGS_MODULE'] = 'osqa.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()