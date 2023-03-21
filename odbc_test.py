import pyodbc
server = '<sqlserver name>.database.windows.net'
database = '<Database name>'
username = '<Username>'
password = '<password>'   
driver= '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM V4.Load_log")
# row = cursor.fetchone()
# while row:
#     print (str(row[0]) + " " + str(row[1]))
#     row = cursor.fetchone()

import pandas as pd

pd.read_sql_query("SELECT * FROM V4.Load_log", conn)
