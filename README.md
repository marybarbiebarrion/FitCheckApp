# FitCheckApp

## INSTALLATION

1. Follow the CSCI 40 slideset on how to setup a virtual environment and install 
the necessary dependencies (Django, dotenv, etc.). This is just archived in Canvas.

2. When installing dependencies, **be sure to include psycopg2-binary.** (pip install psycopg2-binary)
This is necessary for getting PostgreSQL to work.

3. Instead of doing startproject, **clone this repo into the virtual environment folder.** Don't forget to do the necessary steps for making the .env file. Secret Key will be pinned in the group chat.

4. To add your section, **make an app.** This means there should be 5 apps in total.

## SETTING UP THE DATABASES

1. If you haven't, add the create statements of your relations to fitcheck-setup.sql
 

2. Login to PostgreSQL in your terminal and run the command:

        /i fitcheck-setup.sql
    
    Note that the file is setup with the assumption that your Postgres system account is called **postgres**. You may make the necessary adjustments to the file according to your needs.

3. Take note as well of the necessary changes in settings.py, specifically the DATABASES section. See the additional resource below for more information.






Additional resources:
[Complete Tutorial: Set-up PostgreSQL Database with Django Application](https://medium.com/django-unleashed/complete-tutorial-set-up-postgresql-database-with-django-application-d9e789ffa384)

If any errors arise, feel free to message the group chat.

Thank you, and here's to (as close to) no errors or bugs!
