# To-Do App

A simple Django-based To-Do application with CRUD operations and custom authentication.  
- Add, update, delete, and mark tasks as completed.  
- User authentication with Django's built-in system.  

## Setup

1. Clone the repository.

2. Create a virtual environment and install dependencies:
       pip install -r requirements.txt

3. Run migrations:
       python manage.py makemigrations,
       python manage.py migrate,

4. Create the Super User to access the Django Admin Panel:
       python manage.py createsuperuser
           - fill the all necessary details.

5. Start the Server:
       python manage.py runserver

