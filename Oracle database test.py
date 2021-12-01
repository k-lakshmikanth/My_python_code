import pandas as pd
import cx_Oracle

con = None
try:
    con = cx_Oracle.connect('scott','tiger','localhost/xe',encoding='UTF-8')
    ds = pd.read_sql("SELECT * FROM EMP",con)
    df = pd.DataFrame(ds)
    print(df[['DEPTNO','ENAME']])
    #  df.iloc(0:1,0:2)  # This gives first three columns 0,1,2 & firt two rows 0,1 
    #  df[df['ENAME'].str.contains(r'KI')]  #This gives all rows in which ENAME contains in starting or ending or contains in it
    '''
    ndf1 = df[['DEPTNO','EMPNO','ENAME']]
    filter = ndf1[ndf1['ENAME'].str.contains(r'K')]
    print(filter)'''
    # df.query('DEPTNO == 10 and SAL > 1500') #like where clause in sql
    #print(df.sort_values('ENAME'))  #like orderby in sql
except cx_Oracle.Error as Error:
    print('Error')
finally:
    con.close()