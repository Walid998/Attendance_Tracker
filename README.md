<h1> Attendance Tracker </h1>

## Simple tracking system for Employees and Managers

The idea of this application to track attendance of employees 
For Employees:
<ul>
  <li> In the srart of a day employee login to the system at a time</li>  
  <li> after working hours each employee make request to leave the company</li>
  <li> the employee have to wait for manager response</li>
  <li> may the manager 'accept' or 'cancel' leave request</li>
  <li> if the employee permitted to leave the log session terminated automatically</li>
  <li> and the system log him out</li>
</ul>

For Managers - In The Dashboard each manager:
<ul>
  <li>can see number of employees loged in</li>
  <li>can see number of leaving requests of employees</li>
  <li>can be notified with leaving requests</li>
  <li>not have to reload page of requests because it's worked synchronously</li>
</ul>

## Usage:

<ol>
<li> required pachages:

``` 
pip install django==2.2.0
pip install channels==2.0.0
pip install channels-redis==2.2.0
pip install django_crispy_forms
pip install djangorestframework
```
</li>
</ol>
