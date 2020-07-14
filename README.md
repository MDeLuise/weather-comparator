# weather-comparator
A web-based weather comparator writter in python using flask framework.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Screenshots](#screenshots)

## General info
A mainly backend side project focused on multiple points, it's a web-basd app that compare weather in 2 different location.  
It use the API provided by [openweather](https://openweathermap.org/), and it incorporate an authentication mechanism to obtain more weather info.  
Weather-comparator was useful for learning:
* flask framework
* a token-based authentication mechanism
* a two-factor authentication mechanism (opt sent by mail)
* docker (image creation and compose)
* real API usage
* mongoDB

## Technologies
Weather-comparator is a dockerized web-app, so docker (and docker-compose) is needed.
	
## Setup
To run this project first obtain a API key from [openweather](https://openweathermap.org/) and place it in `vars.env` file, then:
```
$ docker build -t weather-flask . # create "weather-flask" docker image
$ docker-compose up # start project containers
```
Now go to `localhost:5000/` in order to use the web-app, and to `localhost:1080/` in order to check the (fake) email send by the web-app.

## Screenshots
<img src="docs/images/screenshot_1.gif" width="700">
