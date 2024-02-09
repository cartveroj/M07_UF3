from conecction import *

def create():
    sql_insert='''INSERT INTO public.users(user_id, user_name, user_surname, user_age, user_email) 
                VALUES('1','Veronica','Cartagena',30,'vcj@gmail.com')
                '''
  
    print(sql_insert)
    connection.execute(sql_insert)
    conn.commit()

