from configparser import ConfigParser
import json


def getMusicGenres():
    genreFile = open('music_genres.json')

    genresObject = json.load(genreFile)
    genreFile.close()
    return genresObject['music_genres']


def getHobbies():
    hobbyFile = open('hobbies.json')
    hobbiesObject = json.load(hobbyFile)
    hobbyFile.close()
    return hobbiesObject['hobbies']


def getNotifications():
    notificationFile = open('notifications.json')
    notificationsObject = json.load(notificationFile)
    notificationFile.close()
    return notificationsObject['notifications']


def getPronouns():
    pronounFile = open('pronouns.json')
    pronounsObject = json.load(pronounFile)
    pronounFile.close()
    return pronounsObject['pronouns']


def getConfig(section, filename='config.ini'):
    parser = ConfigParser()
    parser.read(filename)

    config = None
    if parser.has_section(section):
        config = {}
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return config
