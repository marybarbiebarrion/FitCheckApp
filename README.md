# FitCheckApp

## INSTALLATION

1. Follow the CSCI 40 slideset on how to setup a virtual environment and install 
the necessary dependencies (Django, dotenv, etc.). This is just archived in Canvas.

2. When installing dependencies, **be sure to include psycopg2-binary.** (pip install psycopg2-binary)
This is necessary for getting PostgreSQL to work.

3. Instead of doing startproject, **clone this repo into the virtual environment folder.** Don't forget to do the necessary steps for making the .env file. Secret Key will be pinned in the group chat.

4. To add your section, **make an app.** This means there should only be 5 apps in total.

## RUNNING THE SERVER

1. If on a fresh install, run the fitcheck-setup.sql in postgres using the command:

        psql -U user_name -d postgres

        DROP DATABASE fitcheck_db;
        
        CREATE DATABASE fitcheck_db;
        \c fitcheck_db
        \i fitcheck-setup.sql
    
    Note that this **deletes** the database and all data inside it. This is also configured such that the postgres user is just named "postgres", so make the necessary changes both in the file and in settings.py.

3. Make migrations for **each app.**

        python manage.py makemigrations UserProfile
        python manage.py makemigrations FoodAnalysis
        python manage.py makemigrations FitnessPlanning
        python manage.py makemigrations NutritionGuidance
        python manage.py makemigrations [wellnesstracker]
    Doing only makemigrations outputs no changes detected, and even I'm unsure why. You can run a normal makemigrations afterwards just to be sure.

4. Migrate, then run the fitcheck-populate.sql file inside postgres.

        python manage.py migrate
        [IN POSTGRES]
        /i fitcheck-populate.sql
    [NOTE: fitcheck-populate.sql doesn't have anything yet, so skip this for now.]
5. Run the server.

        python manage.py runserver


Additional resources:
[Complete Tutorial: Set-up PostgreSQL Database with Django Application](https://medium.com/django-unleashed/complete-tutorial-set-up-postgresql-database-with-django-application-d9e789ffa384)

If any errors arise, feel free to message the group chat.

Thank you, and here's to (as close to) no errors or bugs!
