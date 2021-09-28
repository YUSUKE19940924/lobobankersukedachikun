import mysql.connector

class Mysql_connector:
  def mysql_connector_open():
    conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='P@ssw0rd',
        database='chatbot'
        )   

  
    conn.ping(reconnect=True)
    cur = conn.cursor(buffered=True)
  
    cur.close()
    conn.close()
    
    return cur

  def mysql_connector_ping():
       conn =  mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='P@ssw0rd',
        database='chatbot'
        ) 
       conn.ping(reconnect=True)

  def mysql_connector_cursor():
    conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='P@ssw0rd',
        database='chatbot'
        )   

    
    conn.ping(reconnect=True)
    cur = conn.cursor(buffered=True)


        


  def mysql_connetor_close():
    conn = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='P@ssw0rd',
    database='chatbot'
    )   


    conn.ping(reconnect=True)
    cur = conn.cursor(buffered=True)
  
    cur.close()
    conn.close()




  def mysql_connector_cur_close():
    conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='P@ssw0rd',
        database='chatbot'
        )   


    conn.ping(reconnect=True)
    cur = conn.cursor(buffered=True)
        
    return cur

    """
    
    conn = mysql.connector.connect(
    host= "us-cdbr-east-04.cleardb.com",
    port= "3306",
    user= "b532f809ae5b5c",
    password= "c14c0399",
    database= "heroku_542c06e97c0eef1"
    )   
    """