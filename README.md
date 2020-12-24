# ilexius_task
Tasks for ilexius done in Django

## Features
- Added an employee id field to the User model, editable only when user instance is not active, from the admin panel.
- Added a log in count, which logs how many times a user has logged in, also accessible in the admin panel.
- Added a "log in as" feature, which lets superusers log in as other users from the admin panel.

## How-to start
- Install requirements.txt;
- Run python manage.py migrate to sync database;
- Create a superuser;
- Run the server.
