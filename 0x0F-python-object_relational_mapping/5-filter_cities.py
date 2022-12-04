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
    cursor.execute("SELECT cities.name\
        FROM cities\
        JOIN states\
        ON cities.state_id=states.id\
        WHERE states.name= %s\
        ORDER BY cities.id", (argv[4],))
    states = cursor.fetchall()
    list_of_cities = []
    for city in states:
        list_of_cities.append(city)
    print(list_of_cities, sep=',')
    cursor.close()
    db.close()
