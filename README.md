# schedulerapp

This project is used to schedule the events which contains event name, start date and end date. Also, can able to see the number of hours/day that events are scheduled for last 30 days.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)

## Project Description

This project can be used to schedule, check and analyse the hours spent per day for the events in last 30 days. This project is developed with Django(4.2.1), Python(3.11.3) and postgresql database. Refer requirements.txt for all the packages installed as part of this project.

## Installation

1. Clone the repository: 

         git clone https://github.com/raahulvarma/schedulerapp.git

2. Navigate to the project directory:

            cd project_name

3. Create a virtual environment:

            python -m venv env

4. Activate the virtual environment:

            .\env\Scripts\activate
5. Install the project dependencies:

            pip install -r requirements.txt
6. Refer .sample_env file and add .env file in the project directory and update with respective values.
7. Perform database migrations:

            python manage.py makemigrations
            python manage.py migrate

## Usage

Run the project with the command - python manage.py runserver

- Hit the localhost URL - http://127.0.0.1:8000/
- Register the User with username, email, password.
- Login to the Site with registered user to check the events.
- Click on Add events Tab in Navigation bar to add the events.
- Click on List events Tab in Navigation bar to check all the available events for the user.
- Click on Edit in the event row to edit the event.
- Click on Delete in event row to delete the event.
- Click on Event Analytics to check the hours spent on events per day in last 30 days.
- Click on Logout to logout the user from the site.

## Configurations

- Clone .sample_env file to the project folder and rename the file to .env
- Recheck the database configurations, installed packages before running the application.

## Dependencies

- All the dependencies used in this project are placed in requirements.txt file.


