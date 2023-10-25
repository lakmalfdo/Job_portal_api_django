# Job Portal Backend - DJango Based RESTful API

## Introduction
In this tutorial, I will guide you through the process of creating a Django project for a backend of an online job portal. We'll set up a virtual environment to isolate our project's dependencies, install necessary packages, create a Django project and app, define models, views, serializers, and configure URLs. This project allows job seekers to search for job listings, employers to post job openings, and job applicants to submit applications.

## Database Design
### Tables
To kickstart our project, I first designed our database by identifying key tables for the system. Here's a list of tables I've identified for our job portal:

- Users
- Employers
- JobSeekers
- JobListings
- Applications
- Skills
- JobSeekerSkills
- EmployersJobListings
- Categories
- JobCategoryMapping
- Messages
- Notifications
  
You can find the database schema creation script in the database_schema.sql file under the sql_scripts folder. This list includes the core tables required for a job portal, but it can be extended by adding more tables to meet specific requirements.

## Development

### Setting Up a Project Folder and Virtual Environment
#### Why Use a Virtual Environment?
A virtual environment, created with .venv, allows you to isolate your project's dependencies. This means you can have separate sets of Python packages for different projects. This is essential for keeping your project self-contained and preventing conflicts with globally installed packages.

1. Create a project folder:
<pre>mkdir job_portal_api_django
cd job_portal_api_django</pre>

2. Create a virtual environment (.venv) for your project:
<pre>python -m venv .venv</pre>

3. Activate the virtual environment:
<pre>.venv\Scripts\activate</pre>

### Installing Python and Django Packages
Before working on your Django project, you need to install Python and the required packages inside your virtual environment.

1. Install Python (if not already installed):
<pre># On macOS and Linux:
sudo apt-get install python3

# On Windows, download Python from python.org and install it.</pre>

2. Install Django and Django REST framework:
<pre>pip install django djangorestframework</pre>

Now you have Python, Django, and the necessary packages installed in your virtual environment.

### Creating a Django Project and App
1. Create a Django project named "job_portal_api":
<pre>django-admin startproject job_portal_api</pre>

2. Create a Django app named "job_portal_api_app" within your project:
<pre>python manage.py startapp job_portal_api_app</pre>

### Defining Models
In your Django app, you can define models in the models.py file. Models define the structure of your database tables.

### Creating Views
In Django, views define the logic for handling HTTP requests and returning responses. You can create views for your API in the views.py file.

### Adding Serializers
Serializers allow you to convert complex data types, such as Django model instances, into native Python data types. You can add serializers in the serializers.py file.

### Configuring URLs
URLs are mapped to views in Django to define how the application responds to different HTTP requests. You can configure URLs in the urls.py file.

## Setting Up the Database
In this project, we use a MySQL database to store our data. However, you can use your preferred database system. Here, we'll guide you through installing the MySQL client package, which is essential if you're using MySQL as your database system. If you're using a different database, follow the corresponding installation instructions for that database.

1. Install the MySQL client package:
<pre>pip install mysqlclient</pre>

2. Update your project's database settings in job_portal_api/settings.py. In the DATABASES configuration, specify your database connection details:
<pre>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',  # Replace with your MySQL server host
        'PORT': '3306',       # Replace with your MySQL server port
    }
}</pre>
Make sure to replace 'your_database_name', 'your_mysql_username', 'your_mysql_password', 'localhost', and '3306' with your specific MySQL configuration.

3. Create the initial database tables and apply migrations:
<pre>python manage.py makemigrations
python manage.py migrate</pre>

Now, your project is configured to use a MySQL database, and the necessary tables have been created.

## Deployment and Testing
You have successfully set up your Django job portal API project, and now it's time to deploy and test it.

### Local Deployment:
1. Start your Django development server:
<pre>python manage.py runserver</pre>
Your Django project will be available locally at http://127.0.0.1:8000/.

2. To test your RESTful APIs, you can use tools like Postman or curl. Here's how you can make a sample request with curl:

Now, your Django job portal API is deployed locally for development. You can access it on your machine and test the RESTful APIs using Postman or curl. Enjoy building and using your job portal API!

I've built a professional DJango RESTful API for an online job portal. Feel free to extend this project by adding features such as user authentication, real-time notifications, and more to make it even more impressive. Happy coding!
