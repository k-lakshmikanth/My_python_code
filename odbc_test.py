import pyodbc
server = 'bizagipoc.database.windows.net'
database = 'Bizagipoc'
username = 'sv-admin'
password = 'Sv-@dm1n'   
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
