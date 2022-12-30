# MODULE: Data Representation
## AUTHOR: Ante Dujic

***

This repository contains the work done as a project for the Data Representation module as part of the HDip in Data Analytics, ATU. The aim of the project was to demonstrate the understanding how to create and consume RESTful APIs. This repository has the following structure:

```
data-representation-BigProject
│   .gitignore
│   README.md
│   dao.py 
│   dbconfigtemplate.py 
│   requirements.txt
│   server.py 
│
└───createDB
│   │   createDatabase.py
│   │   createTable.py
│   
└───pages
│   │   index.html
│   │   indexOne.html
│   │   login.html
│   │   profile.html
│   
└───staticpages
│   │   login.html
│   │
│   └───img
│       │   destination.jpg
│       │   hand.jpg
│       │   paperplane.jpg
│       │   plane.jpg
│       │   world.jpg
```

### FILE DETAILS
***

File | Description
-|-
server.py | Main app to define login and Flask commands
dao.py | Program to connect server to the mySQL queries
dbconfigtemplate.py | Program for setting mySQL details - rename to dbconfig.py and fill your details when running the project
requirements.txt | Libraries used to run the app - use to install to your local machine (or VM)
README.md | This readme

##### createDB

File | Description
-|-
createDatabase.py | Program to create database on your machine
createTable.py | Program to create table on your machine

##### pages

File | Description
-|-
login.html | Page to redirect to when credentials are incorect
profile.html | Home page, entered when logged in correctly
index.html | Page that handles the created restAPI, using AJAX
indexOne.html | Page that handles third party restAPI, using AJAX

##### staticpages

File | Description
-|-
login.html | Initial login page
img folder | Contains images for html

### THIRD PARTY restAPI
***

https://developer.roadgoat.com/#introduction

This api requires the credentials (access and secret key) to make requests. They can be obtained by registering to the page. Keys obtained of the free registration are limited to a 1000 requests, which is deemed sufficient for this project. Keys are included in the AJAX calls in *indexOne.html*. Having keys publicly visible is not a recommendation but considering it's free and only used for demonstration perposes it is included in the code.

### HOW TO RUN THE PROJECT
***

Autentification details:
Username | Password
-|-
Andrew | lecturer
Ante | student

#### 1. PYTHONANYWHERE

LINK: http://antedujic.pythonanywhere.com/

#### 2. LOCALLY

1. Clone this repository
2. Install the libraries from *requirements.txt*
3. Add your mySQL details to the *dbconfigtemplate.py* file and rename it to dbconfig.py
5. Run *createDatabase.py*
6. Run *createTable.py*
7. Run *server.py*
8. Open your browser and run http://127.0.0.1:5000/