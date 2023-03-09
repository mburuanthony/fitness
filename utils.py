import sqlite3

dbconn = sqlite3.connect('data.db')
dbconn.execute("PRAGMA foreign_keys = ON")
cursor = dbconn.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS members(
        mbrid INTEGER PRIMARY KEY,
        fName TEXT, 
        lName TEXT, 
        address TEXT, 
        mobile TEXT, 
        email TEXT
    )"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS fitness(
        fitnessid INTEGER PRIMARY KEY, 
        fitnesstype TEXT
    )"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS enrollments(
        enrollid INTEGER primary key, 
        mbrid INTEGER, 
        fitness INT, 
        FOREIGN KEY(fitness) REFERENCES fitness (fitnessid), 
        FOREIGN KEY(mbrid) REFERENCES members (mbrid)
    )"""
)

# cursor.execute(
#     """INSERT INTO fitness(fitnesstype) VALUES ("Cardio, Thursday, 3Pm - 5Pm")""")
# cursor.execute(
#     """INSERT INTO fitness(fitnesstype) VALUES ("Pilates, Friday, 9Am - 11Am")""")
# cursor.execute(
#     """INSERT INTO fitness(fitnesstype) VALUES ("Spin, Monday, 2Pm - 4Pm")""")

dbconn.commit()


def creatembr(fName: str, lName: str, address: str, mobile: str, email: str):
    cursor.execute("INSERT INTO members (fName, lName, address, mobile, email) VALUES (?,?,?,?,?)",
                   (fName, lName, address, mobile, email))
    dbconn.commit()


def deletembr(mbrid: int):
    cursor.execute("DELETE FROM members WHERE mbrid = ?", (mbrid,))
    dbconn.commit()


def createnrollmnt(mbrid: int, fitness: int):
    cursor.execute(
        "INSERT INTO enrollments (mbrid, fitness) values (?,?)", (mbrid, fitness))
    dbconn.commit()


def searchenrollmbr(mbrid: int, lastname: str):
    mbrres = cursor.execute(
        "SELECT * FROM members WHERE members.mbrid = ? OR members.lName = ?", (mbrid, lastname))

    return mbrres.fetchall()


def joinedsearch(mbrid: int, lastname: str):
    joinedres = cursor.execute(
        "SELECT members.mbrid, members.fName, members.lName, members.address, members.mobile, members.email, fitness.fitnesstype FROM members INNER JOIN enrollments ON enrollments.mbrid = members.mbrid INNER JOIN fitness ON fitness.fitnessid = enrollments.fitness WHERE members.mbrid = ? OR members.lName = ?", (
            mbrid, lastname)
    )

    return joinedres.fetchall()


def searchmbr(mbrid: int, lastname: str):
    joinedres = joinedsearch(mbrid=mbrid, lastname=lastname)

    mbrres = cursor.execute(
        "SELECT * FROM members WHERE members.mbrid = ? OR members.lName = ?", (mbrid, lastname))

    if len(joinedres) != 0:
        return joinedres
    else:
        return mbrres.fetchall()
