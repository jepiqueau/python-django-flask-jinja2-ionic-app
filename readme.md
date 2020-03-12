# Python Flask Restful SQLite

Python Flask Restful SQLite, based on the Python Flask Framework, is mainly focusing on demonstrating the implementation of an application using a Restful Api to access an SQL database (SQLite). It is also demonstrating the use of Ionic Stencil Web components into Jinja2 templates.

## Getting Started on Windows

```
git clone https://github.com/jepiqueau/python-django-flask-jinja2-ionic-app
cd python-django-flask-jinja2-ionic-app
git remote rm origin
```

### Set up a virtual environment
You can make sure that pip is up-to-date by running:
```
pip3 install --upgrade pip
```

Then check for virtualenv installed on Python

```
python3 -m virtualenv --version
```
If not

```
pip3 install virtualenv
```

Then execute ```setenv``` to set-up the environment and the application requirements.

```cmd
setenv
```
or

```powershell
./setenv
```

A virtual environment ```appenv``` should have been created.

### Activate the virtualenv

```cmd
activateenv
``` 
or

```powershell
./activateenv
```

The virtualenv ``` appenv ``` is now activated
An (appenv) prompt should have been added to your working path.
You should get the response: "workingpath"/appenv/bin/python

Then check that Flask has been installed in the ``àppenv```environment

```cmd or powershell
python
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from flask import Flask
>>> exit()
```

### Deactivate the virtualenv

To leave the virtual environment

```cmd or powershell
deactivate
```
### Create the Database

Make sure you deactivate from the virtualenv ```appenv```

```cmd
createDB
```
or
```powershell
./createDB
```

Check that the database has been created

```cmd or powershell
sqlite3 app.db
```
You should get the sqlite prompmt

```
SQLite version 3.28.0 2019-04-15 14:49:49
Enter ".help" for usage hints.
sqlite> .tables
alembic_version  components       maintenances   
sqlite> .schema
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
CREATE TABLE components (
	id INTEGER NOT NULL, 
	position INTEGER NOT NULL, 
	weight FLOAT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_components_position ON components (position);
CREATE TABLE maintenances (
	id INTEGER NOT NULL, 
	body VARCHAR(140), 
	date DATETIME, 
	component_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(component_id) REFERENCES components (id)
);
CREATE INDEX ix_maintenances_date ON maintenances (date);
sqlite> select * from components;
1|1|5.25
2|2|2.32
3|4|4.55
4|5|5.25
5|8|3.75
6|10|7.237
7|11|1.25
8|13|2.25
9|14|3.75
10|16|5.25
11|18|2.25
12|20|7.237
13|22|4.55
14|25|3.75
15|27|5.25
16|30|7.237
17|33|3.75
18|35|2.32
19|37|4.55
20|40|5.25
sqlite> select * from maintenances;
1|Test Component 1 OK|2020-02-21 13:35:44.949716|1
2|Test Component 10 OK|2020-02-23 13:35:44.949881|10
3|Test Component 17 OK|2020-02-25 13:35:44.949948|17
4|Test Component 4 OK|2020-02-27 13:35:44.950003|4
5|Test Component 15 OK|2020-02-29 13:35:44.950054|15
6|Test Component 6 OK|2020-03-02 13:35:44.950104|6
7|Test Component 4 OK|2020-03-04 13:35:44.950152|4
8|Test Component 9 OK|2020-03-06 13:35:44.950201|9
9|Test Component 1 OK|2020-03-08 13:35:44.950248|1
10|Test Component 12 OK|2020-03-10 13:35:44.950296|12
sqlite>.exit
```

### Run the App

```cmd
bootstrap
``` 
or

```powershell
./bootstrap
``` 

### Open in browser

        ```
        http://127.0.0.1:5000/
        ``` 


## Getting Started on Mac Os

```bash
git clone https://github.com/jepiqueau/python-django-flask-jinja2-ionic-app
cd python-django-flask-jinja2-ionic-app
git remote rm origin
```

### Set up a virtual environment
You can make sure that pip is up-to-date by running:
```
pip3 install --upgrade pip
```

Then check for virtualenv installed on Python

```bash
python3 -m virtualenv --version
```
If not

```bash
pip3 install virtualenv
```

Then execute ```setenv``` to set-up the environment and the application requirements.

```bash
./setenv
```
A virtual environment ```appenv``` should have been created.

### Activate the virtualenv

```bash
source appenv/bin/activate
```

An (appenv) prompt should have been added to your working path.
You should get the response: "workingpath"/appenv/bin/python

Then check that Flask has been installed in the ``àppenv```environment

```bash
python
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from flask import Flask
>>> exit()
```

### Deactivate the virtualenv

To leave the virtual environment

```bash
deactivate
```

### Create the Database

Make sure you deactivate from the virtualenv ```appenv```

```bash
./createDB
```
Check that the database has been created

```bash
sqlite3 app.db
```
You should get the sqlite prompmt

```
SQLite version 3.28.0 2019-04-15 14:49:49
Enter ".help" for usage hints.
sqlite> .tables
alembic_version  components       maintenances   
sqlite> .schema
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
CREATE TABLE components (
	id INTEGER NOT NULL, 
	position INTEGER NOT NULL, 
	weight FLOAT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_components_position ON components (position);
CREATE TABLE maintenances (
	id INTEGER NOT NULL, 
	body VARCHAR(140), 
	date DATETIME, 
	component_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(component_id) REFERENCES components (id)
);
CREATE INDEX ix_maintenances_date ON maintenances (date);
sqlite> select * from components;
1|1|5.25
2|2|2.32
3|4|4.55
4|5|5.25
5|8|3.75
6|10|7.237
7|11|1.25
8|13|2.25
9|14|3.75
10|16|5.25
11|18|2.25
12|20|7.237
13|22|4.55
14|25|3.75
15|27|5.25
16|30|7.237
17|33|3.75
18|35|2.32
19|37|4.55
20|40|5.25
sqlite> select * from maintenances;
1|Test Component 1 OK|2020-02-21 13:35:44.949716|1
2|Test Component 10 OK|2020-02-23 13:35:44.949881|10
3|Test Component 17 OK|2020-02-25 13:35:44.949948|17
4|Test Component 4 OK|2020-02-27 13:35:44.950003|4
5|Test Component 15 OK|2020-02-29 13:35:44.950054|15
6|Test Component 6 OK|2020-03-02 13:35:44.950104|6
7|Test Component 4 OK|2020-03-04 13:35:44.950152|4
8|Test Component 9 OK|2020-03-06 13:35:44.950201|9
9|Test Component 1 OK|2020-03-08 13:35:44.950248|1
10|Test Component 12 OK|2020-03-10 13:35:44.950296|12
sqlite>.exit
```


### Run the App

```bash
source appenv/bin/activate
FLASK_APP=index.py flask run
```

### Open in a Browser

```
http://127.0.0.1:5000/
```








