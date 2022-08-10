from utils import DBUtils
from model import OnboardingRole

__onboardingRoleSelectByMemberSql = """
    SELECT * FROM onboarding_roles
    WHERE member_id = ?;
"""

__onboardingRoleInsertSql = """
    INSERT OR IGNORE INTO onboarding_roles (
        member_id,
        role_id
    ) VALUES (
        ?,
        ?
    );
"""

__onboardingRoleDeleteByMemberSql = """
    DELETE FROM onboarding_roles
    WHERE member_id = ?;
"""


def getOnboardingRolesByMember(memberID: str):
    dbConnection = None
    dbCursor = None
    try:
        dbConnection = DBUtils.getDBConnection()

        dbCursor = dbConnection.execute(
            __onboardingRoleSelectByMemberSql, (memberID,))
        rows = dbCursor.fetchall()

        if rows:
            roles = []
            for row in rows:
                roles.append(OnboardingRole(
                    row['member_id'],
                    row['role_id']
                ))

            return roles
    except (Exception) as error:
        raise error
    finally:
        if dbCursor:
            dbCursor.close()
        if dbConnection:
            dbConnection.close()


def insertMany(role_list: list):
    dbConnection = None
    try:
        dbConnection = DBUtils.getDBConnection()

        with dbConnection:
            dbCursor = dbConnection.executemany(
                __onboardingRoleInsertSql, role_list)
            dbConnection.commit()
    except (Exception) as error:
        raise error
    finally:
        if dbCursor:
            dbCursor.close()
        if dbConnection:
            dbConnection.close()


def deleteOnboardingRolesByMember(memberID: str):
    dbConnection = None
    dbCursor = None
    try:
        dbConnection = DBUtils.getDBConnection()

        with dbConnection:
            dbCursor = dbConnection.execute(
                __onboardingRoleDeleteByMemberSql, (memberID,))
            dbConnection.commit()
    except (Exception) as error:
        raise error
    finally:
        if dbCursor:
            dbCursor.close()
        if dbConnection:
            dbConnection.close()
