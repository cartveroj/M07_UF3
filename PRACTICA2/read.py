
from conecction import *

def read():
    query ='''SELECT * FROM USERS'''
    print(query)
    connection.execute(query)
    result = connection.fetchall()
    print(result)



 