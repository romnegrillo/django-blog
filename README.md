# Python Django Blog
 
<img src="/django_logo.png " width="350" alt = "Django-Logo">

### About

Almost complete...

This is my first full-featured web application written using Django 
Python Framework. This is a blog app where most of the common 
functionalities of a web application can be built such as:

- [x] Web Fundamentals (HTML/CSS/JS)
- [x] Bootstrap
- [x] Jinja
- [x] Model-View-Template Design Pattern
- [x] User Registration
- [x] User Authentication
- [x] Forgot Password Email Reset Feature (I used Gmail SMTP.)
- [x] Database
- [x] Object Relational Mapping
- [x] CRUD Operations
- [x] File Upload
- [ ] Connect Files to Amazon Web Services, S3 Bucket
- [X] Deployment (I used Heroku)

### Stack

* Python, Django
* HTML/CSS/JS
* Bootstrap
* SQLite for development. PostgreSQL for deployment.
* Amazon S3 Bucket

### How to Use

Some features might not work if you clone this in your computer.
I have some values inside my local machine's environment variables:
* SECRET_KEY
* EMAIL_HOST_USER
* EMAIL_HOST_PASSWORD

You need to supply value for this in settings.py.

This is written in Python 3.8.3
You need to install the following in requirements.txt
```pip install -r requirements.txt```
or you configured your system to use pip3 command then:
```pip3 install -r requirements.txt```

To run the server, type:

```python manage.py runserver```

or if you configured your system to use python3 command then:

```python3 manage.py runserver```

Then access it through your browser by the address:

```localhost:8000```

### Sample Output

<img src="/django_blog.PNG " width="1000px" alt = "Django-Logo">

