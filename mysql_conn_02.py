import pandas as pd
import sqlalchemy

engine1 = sqlalchemy.create_engine('mysql+pymysql://root:sprite19890@localhost:3306/customer_order')
connection1 = engine1.raw_connection()
df1 = pd.read_sql("SELECT * FROM branch", connection1)
df1.head()

##############################################################################################################################

engine2 = sqlalchemy.create_engine('mysql+pymysql://root:sprite19890@localhost:3306/student_database')
connection2 = engine2.raw_connection()
df2 = pd.read_sql("SELECT * FROM student", connection2)

df2.head()
df2.dtypes

df2 = pd.read_sql("SELECT student_name,phone FROM student", connection2)
df2.head()








