import MySQLdb

conn = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="PixelAdvant@123",
    db="travel_crm",
    port=3306
)
print("Connection successful!")