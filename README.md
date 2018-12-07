# iReporter
[![Build Status](https://travis-ci.org/Emmanuelaaron/iReporter.svg?branch=api-end-points)](https://travis-ci.org/Emmanuelaaron/iReporter)
[![Coverage Status](https://coveralls.io/repos/github/Emmanuelaaron/iReporter/badge.svg?branch=api-end-points)](https://coveralls.io/github/Emmanuelaaron/iReporter?branch=api-end-points)
[![Maintainability](https://api.codeclimate.com/v1/badges/16dced1073a6f03e1ed2/maintainability)](https://codeclimate.com/github/Emmanuelaaron/iReporter/maintainability)

Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

## Getting started
You can clone this [repo](https://github.com/Emmanuelaaron/iReporter.git) on your local machine or checkout the user-interface on [gh-pages](https://emmanuelaaron.github.io/iReporter/UI/temps/start_page) and the app is hoted on [heroku](https://ireportere.herokuapp.com/)

### Prerequisites
Install [python](https://www.python.org/downloads/release/python-371/) on your local machine

### Installing
Clone the this repo on your local machine
```
$ git clone https://github.com/Emmanuelaaron/iReporter.git
```
cd into the cloned directory, install the virtual environment and activate, checkout to the most stable branch and install all the dependences.
```
$ cd iReporter
$ pip install virtualenv
$ virtualenv venv
$ source venv/Scripts/activate
$ git checkout api-endpoints
$ pip install -r requirements.txt
$ python run.py
```
* copy the Url it into postman and put to run any endpoint of your preference in the table below with the url prefix ('/api/v1') for each endpoint.

HTTP Method | Endpoint | Functionality | Parameters 
------------|----------|---------------|------------
POST | /signup | User able to signup | None
POST | /red-flags | Creates a red flag| None
GET | /red-flags | Gets all red flags | None
GET | /red-flags/<int:flag_id> | Gets a specific red flag | Flag_id
DELETE | /red-flags/<int:flag_id> | deletes a specific red flag | Flag_id

## Running Tests
Install pytest, activate the virtual environment and then run the tests
```
$ pip install pytest
$ pytest
```
You can checkout the code coverage by using the code below
```
$ pytest --cov=.
```
Make sure your virtual environment is activated

## Deployment
The application is hosted on [heroku](https://ireportere.herokuapp.com/)

## Tools Used
* [python](https://www.python.org/downloads/release/python-371/)
* [Flask](http://flask.pocoo.org/) Micro web framework for python
* [pip](https://pip.pypa.io/en/stable/) package installer for python
* [Virtualenv](https://virtualenv.pypa.io/en/stable/) Tool used to created isolated programs for python

## Built with
So far this application has been built with
* [Python](https://www.python.org/downloads/release/python-371/)
* [Flask](http://flask.pocoo.org/)
* HTML
* CSS

## Contributions
To contribute to this project please create a branch off the api-end-points after which you will create a pull request before it is merged back.

## Aurthor
By Emmanuel Isabirye
