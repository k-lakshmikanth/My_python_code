import pandas as pd
import cx_Oracle
def db_conn():
    try:
        username = input("USERNAME:")
        password = input("PASSWORD:")
        host = input("HOST:")
        conn = cx_Oracle.connect(username,password,host,encoding = "UTF-8")
        print("CONNECTION:SUCCESS")
        return conn
    except cx_Oracle.DatabaseError :
        db_conn()
        print("CONNECTION:FAIL")
conn = db_conn()
while 1<2:
    query = input("QUERY:\n")
    if query == '0':
        break
    else:
        ds = pd.read_sql(query,conn)
        df = pd.DataFrame(ds)
        print()
        print(df)
        print()
input()