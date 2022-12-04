#!/usr/bin/python3
"""List all cities from the database bythe order of id """

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities JOIN states "
                   "ON states.id = cities.state_id "
                   "ORDER BY cities.id ASC")
    states = cursor.fetchall()
    for city in states:
        print(city)
    cursor.close()
    db.close()
