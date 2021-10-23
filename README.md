# Awwards-App

## Build by [Kolem Edwin]

## Description

This is an application like Awwards where users can signup, login and post a project to be reviewed and rated.

## Screenshot images

<img src="static/../instagram/static/images/Screenshot%20from%202021-10-17%2016-22-48.png">

<img src="static/../instagram/static/images/002.png">

## Live page

https://github.com/edwinkipchumba/Awwards-app

## User stories

Users would like to:

1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/review other users' projects
4. Search for projects
5. View projects overall score
6. View my profile page

## Behaviour Driven Development (BDD)

| Behaviour | Input | Output |
| :-----------------| :-----------------: | ------------------: |
| Admin Authentication | On demand | Access Admin dashboard |
| Admin Authentication | On demand,Verify emails before proceeding | Access Admin dashboard |
| Display all projects | Home page | Clickable links to open live projects in different sites |
| To add a project | Through Admin dashboard and homepage | Click on add and upload respectively |
| To edit project | Through Admin dashboard | Redirected to the project form details and editing happens |
| To delete the project | Through Admin dashboard | click on project object and confirm by delete button |
| To search projects by title | Enter text in search bar | Users can search by project title |
| Comment on projects | Add comments below respectively project | Users can add comments on any project |
| Vote on projects | Vote | Users can review projects they like and comment |

## Setup | Installation Requirements

1. python3.8
2. virtualenv
3. requirements.txt
4. django3.2.8

## Cloning

* Open Terminal {Ctrl+Alt+T}

```
$git clone https://github.com/edwinkipchumba/Awwards-app

```
```
$cd awwards-app
```

* open based on the text editor you have.

## Running the Application

* Creating the virtual environment

 ```
$ pip install virtualenv 
```

```
$ virtualenv venv
```

$ source venv/bin/activate

* Install Django Dependencies

```
$ pip install -r requirements.txt
```

## Setup Database

* setup your database User,Password, Host then make migrations

```
$ python manage.py makemigrations
```

## Now migrate

```
$python manage.py migrate
```

* To run the application, in your terminal:

$ python3 manage.py runserver

## Technology used

* django3.2.8 and postgresql
* HTML5
* CSS3
* Bootsrap3
* python3.8

## Known Bugs

If you find a bug, kindly feel free to comment an issue here and inlcude their corresponding results.

## Contact  Information

 Feel free to contact me incase of any issue or questions, ideas and concern towards the same.

* Contact Number:+254728357619
  
* E-Mail: edwinkolem5@gmail.com.

## License
