import sqlite3
from objects import Session

def connect():
    global conn
    conn = sqlite3.connect("session_db.sqlite")
    return conn
def close():
    if conn:
        conn.close()

def create_session():
        cursorObj = conn.cursor()
        cursorObj.execute("CREATE TABLE IF NOT EXISTS Session (sessionID INTEGER PRIMARY KEY, startTime TEXT, startMoney REAL, stopTime TEXT, stopMoney REAL);")
        x = get_last_session()
        if x ==None:
            cursorObj.execute('''INSERT INTO Session (sessionID, startTime, startMoney, stopTime, stopMoney)
                            VALUES (0, 'x', 199, 'y', 199);''')
            conn.commit()


def get_last_session():
        cursorObj=conn.cursor()
        cursorObj.execute("SELECT * FROM Session ORDER BY sessionID DESC;")
        sessionID = cursorObj.fetchone()
        sessionObj = Session(int(sessionID[0]), sessionID[1], float(sessionID[2]), sessionID[3], float(sessionID[4]))

        return sessionObj

def add_session(s):
        cursorObj=conn.cursor()
        query = ('''INSERT INTO Session (sessionID, startTime, startMoney, stopTime, stopMoney)
                                VALUES (?, ?, ?, ?, ?);''')
        cursorObj.execute(query, (s.sessionID,s.startTime,s.startMoney,s.stopTime,s.stopMoney))
        conn.commit()



