import MySQLdb

db = MySQLdb.connect(
    host="192.168.1.74",
    user="oldblackwave",
    passwd="28Oklmfts",
    db="mysql"
)

cur = db.cursor()

cur.execute("SELECT * from user")

for row in cur.fetchall():
    print(row[0])

db.close