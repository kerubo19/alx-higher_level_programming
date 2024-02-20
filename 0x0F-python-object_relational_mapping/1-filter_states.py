#!/usr/biin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host = "localhost", port = 3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
            cur = db.cursor()
                cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

                    # Fetch all records
                        rows = cur.fetchall()

                            # Print each record
                                for row in rows:
                                            print(row)

                                                # Close the cursor and the database
                                                    cur.close()
                                                        db.close()

