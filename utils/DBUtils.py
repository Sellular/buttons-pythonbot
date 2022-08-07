import psycopg2

from utils import GeneralUtils

__onboardingRoleTableSql = """
    CREATE TABLE IF NOT EXISTS onboarding_roles (
        member_id   TEXT    NOT NULL,
        role_id     TEXT    NOT NULL,
        PRIMARY KEY(member_id, role_id)
    );
"""


def getDBConnection():
    dbConfig = GeneralUtils.getConfig('postgresql')

    dbConnection = None
    try:
        dbConnection = psycopg2.connect(**dbConfig)

        return dbConnection
    except (Exception, psycopg2.DatabaseError) as error:
        if dbConnection is not None:
            dbConnection.close()
        raise error


def checkTables():
    dbConnection = getDBConnection()

    try:
        dbCursor = dbConnection.cursor()
        tableCommands = (__onboardingRoleTableSql,)

        for command in tableCommands:
            dbCursor.execute(command)

        dbConnection.commit()
        dbCursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        raise error
    finally:
        if dbConnection is not None:
            dbConnection.close()
