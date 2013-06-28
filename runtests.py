import os, sys
from django.conf import settings

DIRNAME = os.path.dirname(__file__)
settings.configure(DEBUG = True,
                   DATABASE_ENGINE = 'sqlite3',
                   DATABASE_NAME = os.path.join(DIRNAME, 'database.db'),
                   INSTALLED_APPS = ('jsonfield',
                                     'jsonformfieldex'))


from django.test.simple import DjangoTestSuiteRunner

runner = DjangoTestSuiteRunner(verbosity=1)
failures = runner.run_tests(['jsonfield',])
if failures:
    sys.exit(failures)
