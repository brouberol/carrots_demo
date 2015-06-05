## Database setup in Django 1.8

I'd like to use Django 1.8 as part of the tutorial, not Django 1.6.4, as currently stated in the Django Carrots website.
The main difference as the trainees are concerned is in the way to setup the database. As South is now part of the django core modules, we must considered ``syncdb`` as deprecated, and should use the following sequence of commands:

```bash
# Create the django project
$ django-admin startproject projectname
$ cd projectname
# Creating django standard tables and applying related default migrations
$ python manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, contenttypes, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying sessions.0001_initial... OK
# Create superuser account
$ python manage.py createsuperuser
Username (leave blank to use 'br'): admin
Email address: admin@admin.com
Password:
Password (again):
Superuser created successfully.
# Create the polls app
$ python manage.py startapp polls
# ... add models in polls.models ...
# Create initial migrations for polls models
$ python manage.py makemigrations
Migrations for 'polls':
  0001_initial.py:
    - Create model Choice
    - Create model Poll
    - Add field poll to choice
# Create tables for all models in polls app, by applying the migrations we just created
$ python manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, contenttypes, polls, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying polls.0001_initial... OK
```

## Spicing up the Poll model?
The ``polls.Poll`` model can be spiced up by adding the [``auto_now_add``](https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.DateField), to automatically set the ``pub_date`` attribute on save.
