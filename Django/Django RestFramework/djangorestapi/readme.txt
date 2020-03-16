Check the same project running on heroku - 
https://djangorestframework.herokuapp.com/

Steps to Follow before using this project - 
1. This project is using Django Rest Framwork for creating rest api for courses app. Its a good learning project to understand how it works.
2. sqllite.db file is not added into this project so after downloading project, run python manage.py migrate to move all the schema into 
your local DB.
3. Install all the packages mentioned in requirements.txt file.
3. Most important thing in DJ REST FW to understand is that how to expose this API to third party to use. And that's where the concept of 
TokenAuthentication comes into picture. 
To authenticate your api follow these tutorials - 
https://www.youtube.com/watch?v=PFcnQbOfbUU
https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html
