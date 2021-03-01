<h1> Attendance Tracker </h1>

## Simple tracking system for Employees and Managers

The idea of this application to track attendance of employees 
For Employees:
<ul>
  <li> In the srart of a day employee login to the system at a time.</li>  
  <li> After working hours each employee make request to leave the company.</li>
  <li> The employee have to wait for manager response.</li>
  <li> May the manager 'accept' or 'cancel' leave request.</li>
  <li> If the employee permitted to leave the log session terminated automatically.</li>
  <li> And the system log him out.</li>
</ul>

For Managers - In The Dashboard each manager:
<ul>
  <li>Can see number of employees loged in.</li>
  <li>Can see number of leaving requests of employees.</li>
  <li>Can be notified with leaving requests.</li>
  <li>Not have to reload page of requests because it's worked synchronously.</li>
</ul>

## Requirements:

<ol>
  <li>Python 3.6 or higher.</li>
  <li> you have to install this pachages in you environment:
    
  ``` 
  pip install django==2.2.0
  pip install channels==2.0.0
  pip install channels-redis==2.2.0
  pip install django_crispy_forms
  pip install djangorestframework
  ```
  </li>
</ol>

## Usage:

<ol>
<li> go to project directory and run:

``` 
python manage.py makemigrations 
python manage.py migrate
```
</li>
<li> then create superuser:

``` 
python manage.py createsuperuser
```
</li>
<li> after that run the project:

``` 
python manage.py runserver
```
</li>
<li> go to  

``` 
http://localhost:8000/Admin/
```
and login with superuser account
</li>
<li> try to add new user then choose a group of:

``` 
Employee
Manager
```
</li>
<li> last step go to:
  
``` 
http://localhost:8000/accounts/login/
```
and login with any user you want 
</li>
</ol>

##### That's all about how the application works.



