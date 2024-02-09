
from conecction import *

def delete():
    sql_delete ='''DELETE FROM USERS WHERE user_id = '1' 
                '''
    print(sql_delete)
    connection.execute(sql_delete)
    conn.commit()

