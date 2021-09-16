import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine
"""
mysql_username = 'root'
mysql_password = 'password'
mysql_ip = '192.168.1.100'
mysql_port = '3306'
mysql_db = 'db_name'
tenant_id = '1234567'
mysql_db_table = 'table_name'
task_id = '12345'
excel_location=D:/path/file.xlsx or D:\\\\path\\\\file.xlsx
"""
def mysql_query_2_excel(username, password, ip, db_name, table_name,tenant_id,task_id,limit_count, excel_location, port=3306):
    sql = '''SELECT * FROM `{}` WHERE tenant_id="{}" AND task_id={} LIMIT {};'''.format(table_name,tenant_id,task_id,limit_count)
    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(username, password, ip, port, db_name))
    df = pd.read_sql_query(sql, engine)
    query_results = DataFrame.from_records(df)
    query_results.to_excel(excel_location, sheet_name='sheet1', index=False)
    return query_results
    
