import MySQLdb

db = MySQLdb.connect(
    host="yukaichou.com",
    user="octalysistool",
    passwd="bnTHT2jpn2HVhSCf",
    db="yukaichou"
)

cur = db.cursor()
cur.execute("SELECT * FROM ot_users")

for row in cur.fetchall():
    for x in row:
        print x

db.close()

