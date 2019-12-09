# Data Representation

This directory contains the files for the Big Project for Data Representation 2019

This project involved the development of the following:
 - A basic Flask server that has a
 - REST API, (to perform CRUD operation)
 - One database table and 
 - Accompanying web interface, using AJAX calls, to perform these CRUD operations

The idea of the web application is that users can:
 - Create and log their runs
 - View all logged runs
 - Update previously logged runs
 - Delete runs
 - Search for runs by name
 - View a leader board which shows the total distance ran by each user in descending order

 To get this project up and running on your own computer, there are a few things that need to be done:
 - You will need python installed on your computer.  This project was created using python 3.7
 - You will need MySQL installed on your computer
 - You will need to create the the 'running' database.  This can be done as follows:
    - Create the 'running' database: run the 'createRunningDatabase.py' file located in the 'Database Creation' folder
    - Create the 'runs' table in the 'running' database: run the 'createRunsTable.py' file located in the 'Database Creation' folder. This will create the table as follows:
        
        Field | Type | Null | Key | Default | Extra
        --- | --- | --- | --- | --- | ---
        id | int(11) | No | PRI | NULL | auto_increment
        date | date | YES | | NULL |
        name | varchar(255) | Yes | | NULL |
        distance | float | YES | | NULL |
        time | float | YES | | NULL |

 - Now that we have created the database, we will need to set up and run the virtual environment
     - Make the virtual environment by going to the 'Big Project' folder in cmder.exe and typing the following: "python -m venv venv"
     - Activate by typing: ".\venv\Scripts\activate.bat"
     - Install flask by typing: "pip install flask"
     - Pip freeze by typing: "pip freeze > requirements.txt"
     - Set the server by typing: "set FLASK_APP=server"
     - Run the server by typing: "flask run"

 - Now that we have the server up and running, we can access the web application by going to "127.0.0.1:5000/running1.html" in our browser
 - From here, the web application can be used as described above

 The code used when creating the web application can be viewed in the files "runsDAO.py", "server.py", "leaderboard.html", "running1.html" and "search.html".  The "Superceded" folder contains test files that were used during the creation of the web application.  They do not have any functionality for the final application.




