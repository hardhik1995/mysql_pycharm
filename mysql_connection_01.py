import pymysql
import pymysql.cursors
import pandas as pd
#import mysql.connector as sql
#import sqlalchemy

#engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/customer_order')

db=pymysql.connect(user='root', password='sprite19890', db='customer_order', host='localhost')

print("connect successful!!")

try:
    with db.cursor() as cursor:

        # SQL
        sql = "SELECT * FROM branch "

        # Execute query.
        cursor.execute(sql)

        print("cursor.description: ", cursor.description)

        print()

        for row in cursor:
            print(row)

finally:
    # Close connection.
    db.close()

df1 = pd.read_sql_query(sql, db)
df1.head()


filePath = "G:\\ANALYTICS_WORLD_R_SAS\\python_world\\pycharm projects\\mysql_pycharm\venv\\Lib\\site-packages\\pandas\\io"
datafile = ["sql"]

for f in datafile:
    df = pd.read_csv(filePath + f + ".csv")
    df.to_sql(name=f, con=db, if_exists='append', index=False)



#df1 = pd.read_sql_table('branch',engine)
#df1

########################################################################################
try:
    with db.cursor() as cursor:

        # SQL
        sql = "SELECT Id,City,Phone FROM customer "

        # Execute query.
        cursor.execute(sql)

        print("cursor.description: ", cursor.description)

        print()

        for row in cursor:
            print(row)

finally:
    # Close connection.
    db.close()

df2 = pd.read_sql_query('SELECT * FROM branch', db)
df2.head()
#########################################################################################
def conn():
    db1=pymysql.connect(user='root', password='sprite19890', db='customer_order', host='localhost')

    return db1







