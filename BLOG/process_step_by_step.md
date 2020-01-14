1) all the package i install is in the requirment.txt
    you will install all of them in one command
    you will use python3 
    when i say python it means pytohn3 . keep that in mind
    =>pip3 install -r requirement.txt

2) Create The project we make a blog project
    => django-admin startproject BLOG
3) this project will include a single app also name "blog"
    => python manage.py startapp blog
4) run the server and check if everything is OK
    =>python manage runserver
    OK

5) add the app to the project settings.py
    in the INSTALLED_PACKAGE

6) you have to create a model schema in the models.py
    we create two table and they are connected with foreign keys
    always remember base model goes first and then the connected model

7) after creating the models apply this command
    =>python manage.py migrate    ## this will create the user database
    =>python manage.py makemigrations  ## detect your custom database
    =>python manage.py migrate         ## create your database

8) create the admin user for the app
    => python manage.py createsuperuser

9) add the database to the admin.py

10) go to the admin panel see the database has CRUD functionality

11) data !! we need a lot of data. to do that thats where the seeder comes

do not use this seeder in production its only for developing purpose

12) add the django_seed to the settigns.py INSTALLED_APP


now this step a little bit difficult
because we use a package that is still not updated at the main pip repo


--------------------SEEDER CONFIGURATION ---------------------------
    1) you have to change a little bit of the seeder main source code

    you are using virtual environment so
    1) go to the lib/site_packages inside your virtual environment
    2) i named it venv. its the name that is inside the bracket in the shell after you activate it
    3)under the site-packages you will find the "django-seed" directory
    4)go to the __init__.py file
        go to the faker method

        under the faker method in line 35
        you find this line
        => cls.fakers[code].seed(random.randint(1, 10000))
        change the line to this
        => cls.fakers[code].seed_instance(random.randint(1, 10000))
----------------------------------------------------------------------
[in VSCODE you can find it ctrl+p and then type 'django-seed' and then select __init__.py ]



13) now stop the server and run this command

=> python manage.py shell

it will give you a shell
type this code

>>>from django_seed import Seed
>>>from blog.models import Author,Article  
>>>seeder = Seed.seeder()
>>>seeder.add_entity(Author,100,{
    'name': lambda x:seeder.faker.name(),
    'email': lambda x:seeder.faker.email(),
})
>>>seeder.add_entity(Article,200)
>>>seeder.execute()


    now exit the shell

    explanation:

    1) you import the seed package
    2) you import the database
    3) create a seed instance
    4) add 100 seed to the author and sepcify their type 
    5) add 200 data to the Article and this time no need to exlecitely describe
    6) execute that

14) run the server and go to admin you will see lot of fake data is generated

[IF THIS DIFFICULT TO YOU YOU CAN SKIP THIS AND ADD YOUR OWN DATA BY HAND]

i added the seed code in the seed.py inside the app


15) now the there are two urls.py in django 
    1) inside the project
    2) inside the app [you have to create it]

16) go to the urls.py[project]
    and add a url for accessing the app inside the project
    you can see that it shows the blog.urls
    so it will tell the program to look the urls.py inside the blog app

17) make a file urls.py inside the blog
    and go to the url

    now this url tell you to fo to the logic layer aka views.py

so you now can go to your app to the url localhost:8000/api

[dont go there now you will find error cause you dont write any logic]


18) add the logic in th views.py
but before that add another app in the settings.py INSTALLED_APP
'rest_framework'

19) lets add the logic i will explain in the comment beside the code
    go to views.py
    
    and write the get method



20) we access the app and we write  a small method but how we can access it??

21) now add the path in the urls.py inside the blog app to the logic
in the urls.py import the class that you write in the views.py
    [the logic under the comment "first"]


    so whats the url now ??

    it is the concatenation of the both project and the app

    =>localhost:8000/api/articles

go to your browser and go to the url

ERROR ?? right ??
what you think, its that easy ???

the problem you face is the data fetched from the databse is not
compatable for json to show
we need to process the data in the api language it is called "serialization"

so start the process

inside your app create another file called "serializers.py"
add the a schema again 
this is not the database schema this is serialize schema

22) now we add the serializer and rewrite the get method

under the comment [second] and comment out the first one
in there  a parmeter many=True means you want multiple data

23) run the server and test it again



