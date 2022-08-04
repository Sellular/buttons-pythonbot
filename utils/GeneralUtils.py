from configparser import ConfigParser
import json


def getMusicGenres():
    genreFile = open('music_genres.json')
    genresObject = json.load(genreFile)
    return genresObject['music_genres']


def getHobbies():
    hobbyFile = open('hobbies.json')
    hobbiesObject = json.load(hobbyFile)
    return hobbiesObject['hobbies']


def getNotifications():
    notificationFile = open('notifications.json')
    notificationsObject = json.load(notificationFile)
    return notificationsObject['notifications']


def getPronouns():
    pronounFile = open('pronouns.json')
    pronounsObject = json.load(pronounFile)
    return pronounsObject['pronouns']


def getConfig(section, filename='config.ini'):
    parser = ConfigParser()
    parser.read(filename)

    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return config
