import sqlite3

__onboardingRoleTableSql = """
    CREATE TABLE IF NOT EXISTS onboarding_roles (
        member_id   TEXT    NOT NULL,
        role_id     TEXT    NOT NULL,
        PRIMARY KEY(member_id, role_id)
    );
"""


__leftMemberRoleTableSql = """
    CREATE TABLE IF NOT EXISTS left_members (
        member_id   TEXT    NOT NULL,
        role_id     TEXT    NOT NULL,
        left_date   TEXT    NOT NULL,
        PRIMARY KEY(member_id, role_id)
    );
"""

__channelMessageTableSql = """
    CREATE TABLE IF NOT EXISTS channel_messages (
        message_id      INTEGER NOT NULL,
        message_code    TEXT    NOT NULL    PRIMARY KEY
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
        tableCommands = (__onboardingRoleTableSql, __leftMemberRoleTableSql, __channelMessageTableSql)

        for command in tableCommands:
            dbCursor.execute(command)

        dbConnection.commit()
        dbCursor.close()
    except (Exception) as error:
        raise error
    finally:
        if dbConnection:
            dbConnection.close()
