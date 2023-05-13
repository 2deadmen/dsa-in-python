import mysql.connector

cnx = mysql.connector.connect(host='database-2.cianwtn8ivvm.eu-north-1.rds.amazonaws.com',
                              database='mydb',
                              user='admin',
                              password='7338210933')

cursor = cnx.cursor()

cursor.execute('insert into `test` values ("kartik")')
cnx.commit()
query = "SELECT * FROM `test`"
cursor.execute(query)

for row in cursor:
    print(row)

cursor.close()
cnx.close()
