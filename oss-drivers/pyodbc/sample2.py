import sqlalchemy
import urllib.parse
from sqlalchemy import create_engine
import pandas as pd

USER='datauser'
PASSWD='T3mpP4551234'
SERVER='tcp:data-test-centralus.database.windows.net,1433'
DATABASE='data-test-centralus'

params = ('Driver={ODBC Driver 17 for SQL Server}; SERVER=' + SERVER + '; PORT=<port>; DATABASE=' + DATABASE + ';UID='+ USER + ';PWD='+ PASSWD +';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=100') 
db_params = urllib.parse.quote_plus(params)
#https://inneka.com/programming/python/how-to-set-connection-timeout-in-sqlalchemy/
engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(db_params), pool_pre_ping=True, connect_args={'Remote Query Timeout': 100})    
query = "SELECT TOP 3 * From Trade.Fred_ADXTNO"

#   return pd.read_sql(query, con=engine).to_html(orient='records')
results = pd.read_sql(query, con=engine).to_html(index=False)
print(results)
