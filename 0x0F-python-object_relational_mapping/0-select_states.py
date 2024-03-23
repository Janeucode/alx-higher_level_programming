#!/usr/bin/python3

"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    """
    Connects to MySQL server and fetches all states from hbtn_0e_0_usa database.
    Prints the results.
    """
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    root, root, db_name = sys.argv[1:4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=root,
                             passwd=root, db=db_name)
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        for row in cur.fetchall():
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)


if __name__ == "__main__":
    main()]i
