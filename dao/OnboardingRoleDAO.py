from utils import DBUtils
from model import OnboardingRole
from psycopg2 import DatabaseError

__onboardingRoleInsertSql = """
    INSERT INTO onboarding_roles (
        member_id,
        role_id
    ) VALUES (
        %s,
        %s
    );
"""

__onboardingRoleDeleteByMemberSql = """
    DELETE FROM onboarding_roles
    WHERE member_id = %s
    RETURNING *;
"""


def insert(memberID: str, roleID: str):
    dbConnection = None
    try:
        dbConnection = DBUtils.getDBConnection()
        dbCursor = dbConnection.cursor()

        dbCursor.execute(__onboardingRoleInsertSql, (memberID, roleID))

        dbConnection.commit()
        dbCursor.close()
    except (Exception, DatabaseError) as error:
        raise error
    finally:
        if dbConnection is not None:
            dbConnection.close()


def deleteOnboardingRolesByMember(memberID: str):
    dbConnection = None
    try:
        dbConnection = DBUtils.getDBConnection()
        dbCursor = dbConnection.cursor()

        dbCursor.execute(__onboardingRoleDeleteByMemberSql, (memberID,))
        deletedRows = dbCursor.fetchall()
        
        dbConnection.commit()
        dbCursor.close()
        
        if deletedRows:
            deletedRoles = []
            for row in deletedRows:
                deletedRoles.append(OnboardingRole(
                    row[0],
                    row[1]
                ))

            return deletedRoles
    except (Exception, DatabaseError) as error:
        raise error
    finally:
        if dbConnection is not None:
            dbConnection.close()
