import MySQLdb

db = MySQLdb.connect(
    host="192.168.1.74",
    user="oldblackwave",
    passwd="28Oklmfts"
)

cur = db.cursor()

cur.execute("CREATE DATABASE pythonSQLDB")

db.close

