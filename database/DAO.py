from database.DB_connect import DBConnect
from model.team import Team

class DAO:

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        query = ("""
        SELECT DISTINCT year 
        FROM teams
        WHERE year>=1980 
        ORDER BY year DESC""")
        cursor.execute(query)
        rows = cursor.fetchall()
        years = [row[0] for row in rows]
        cursor.close()
        conn.close()
        return years

    @staticmethod
    def getAllTeams(y):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT * 
        FROM teams
        WHERE year = %s"""
        cursor.execute(query, (y,))
        listobj = []
        for dct in cursor:
            listobj.append(Team(**dct))
        cursor.close()
        conn.close()
        return listobj

    @staticmethod
    def getSalari(c, y):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        query ="""
        SELECT SUM(S.salary)
        FROM salaries S
        JOIN appearances A ON S.playerID = A.playerID AND S.year = A.year
        JOIN teams T ON A.teamID = T.ID AND A.year = T.year
        WHERE T.teamCode = %s
        AND T.year = %s
        """
        cursor.execute(query, (c, y, ))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row[0]








