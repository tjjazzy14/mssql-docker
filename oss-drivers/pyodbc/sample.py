import pyodbc
import os

#USER='datauser'
#PASSWD='T3mpP4551234'
#SERVER='
#DATABASE='data-test-centralus'


database = '$DATABASE'
server = '$SERVER'
username = '$USER'
password = '$PASSWRD'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';Database='+database+';PORT=1443;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print ('Using the following SQL Server version:')
tsql = "SELECT @@version;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    print (str(row[0]))
