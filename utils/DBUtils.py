import sqlite3

__onboardingRoleTableSql = """
    CREATE TABLE IF NOT EXISTS onboarding_roles (
        member_id   TEXT    NOT NULL,
        role_id     TEXT    NOT NULL,
        PRIMARY KEY(member_id, role_id)
    );
"""


def getDBConnection():
    dbConnection = None
    try:
        dbConnection = sqlite3.connect('pycord.db')
        dbConnection.row_factory = sqlite3.Row

        return dbConnection
    except (Exception) as error:
        if dbConnection:
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
    except (Exception) as error:
        raise error
    finally:
        if dbConnection:
            dbConnection.close()
