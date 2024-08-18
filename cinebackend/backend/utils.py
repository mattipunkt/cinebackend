from platformdirs import *


appname = "cinebackend"
appauthor = "matti"


import requests
import json
import configparser
# Create an instance of the ConfigParser class
config = configparser.ConfigParser()  
config.read(user_config_dir(appname) + '/config.ini')


config = configparser.ConfigParser()
testconfig = configparser.ConfigParser()  
config.read(user_config_dir(appname) + '/config.ini')


###### CONFIG #######

def writeConfig(section, key, value):
    config.read(user_config_dir(appname) + '/config.ini')
    config[section][key] = value
    with open(user_config_dir(appname) + '/config.ini', 'w') as configfile:
        config.write(configfile)
    return

def readConfig(section, key):
    testconfig.read(user_config_dir(appname) + '/config.ini')
    return config[section][key]


def tmdb_requests(movie):
    url = "https://api.themoviedb.org/3/search/movie?query="+ movie +"&include_adult=false&language=de-DE&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": ""
    }
    response = requests.get(url, headers=headers)
    return response.json()


def credit_request(id):
    url = "https://api.themoviedb.org/3/movie/" + str(id) + "/credits?language=de-DE"
    headers = {
        "accept": "application/json",
        "Authorization": ""
    }
    response = requests.get(url, headers=headers)
    return response.json()


def movie_request(id):
    url = "https://api.themoviedb.org/3/movie/" + str(id) + "?language=de-DE"
    headers = {
        "accept": "application/json",
        "Authorization": ""
    }
    response = requests.get(url, headers=headers)
    return response.json()

def cover_request(id):
    url = "https://api.themoviedb.org/3/movie/" + str(id) + "/images"
    headers = {
        "accept": "application/json",
        "Authorization": ""
    }
    response = requests.get(url, headers=headers)
    return response.json()