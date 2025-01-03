from django.core.management import call_command


call_command('makemigrations', verbosity=0, interactive=False)
call_command('migrate', verbosity=0, interactive=False)
