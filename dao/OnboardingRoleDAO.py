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
    try:
        dbConnection = DBUtils.getDBConnection()

        with dbConnection:
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


def insertMany(role_list: list):
    try:
        dbConnection = DBUtils.getDBConnection()

        with dbConnection:
            dbConnection.executemany(
                __onboardingRoleInsertSql, role_list)
            dbConnection.commit()
    except (Exception) as error:
        raise error


def deleteOnboardingRolesByMember(memberID: str):
    try:
        dbConnection = DBUtils.getDBConnection()

        with dbConnection:
            dbConnection.execute(
                __onboardingRoleDeleteByMemberSql, (memberID,))
            dbConnection.commit()
    except (Exception) as error:
        raise error
