import mysql.connector,time,datetime

from linebot.models import(
  TextSendMessage
)

class First_time_use:
  @classmethod
  def first_time_use_handle(self,receive_message):
    reply_message = []

    user_id = receive_message[1]
    user_name = receive_message[2]
    
    config_cleardb1 = {'host':'ホスト',
    'port':'ポート',
    'user':'ユーザ',
    'password':'パスワード',
    'database':'データベース'}

    try:
        #conn = mysql.connector.connect(**config_local)
        conn = mysql.connector.connect(**config_cleardb1)
        conn.ping(reconnect=True)
        cur = conn.cursor(buffered=True)

    except:
        reply_message.append(TextSendMessage(text="データサーバーにアクセスできません。\n恐れ入りますが、もう一度メッセージの送信をお願いします。"))


    cur.execute("INSERT INTO ユーザーID管理簿 VALUES (id,%s,%s)",(user_id,user_name))

    cur.execute(f"CREATE TABLE IF NOT EXISTS 開業費管理{user_id} (\
    `id` int(11) unsigned not null auto_increment primary key,\
    `r_date` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci,\
    `e_date` date DEFAULT NULL,\
    `nominal` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,\
    `price` int DEFAULT '0')ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci")

    cur.execute(f"CREATE TABLE IF NOT EXISTS 債権管理{user_id} (\
    `id` int(11) unsigned not null auto_increment primary key,\
    `datetime` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,\
    `f_i` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,\
    `b_a` int DEFAULT NULL,\
    `r_a` int DEFAULT NULL,\
    `m_r_a` int DEFAULT NULL,\
    `b_d` date DEFAULT NULL,\
    `b_y` int DEFAULT NULL,\
    `b_m` int DEFAULT NULL,\
    `r_y` int DEFAULT NULL,\
    `r_m` int DEFAULT NULL,\
    `r_d` int DEFAULT NULL,\
    `b_i_r` double DEFAULT NULL)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci")

    cur.execute(f"CREATE TABLE IF NOT EXISTS 起業フローチャート{user_id}(\
    `id` int unsigned not null auto_increment primary key,\
    `content` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,\
    `judgement` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT '未完了')ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci")

    cur.execute("select nominal from 開業費管理")
    rows = cur.fetchall()
    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    date_stamp = datetime.date.today()
    id = 1
    for row in rows:
        cur.execute(f"INSERT INTO 開業費管理{user_id} VALUES (%s,%s,%s,%s,%s)",(id,time_stamp,date_stamp,row[0],0))
        id += 1
    id = 1
    cur.execute("select title from 起業フローチャート")
    rows = cur.fetchall()
    for row in rows:
        cur.execute(f"INSERT INTO 起業フローチャート{user_id} VALUES (%s,%s,%s)",(id,row[0],"未完了"))
        id += 1
    conn.commit()  
    reply_message.append(TextSendMessage(text=f"{user_name}様初めてのご利用ありがとうございます。"))

    cur.close()
    conn.close()
    try:
      return reply_message
    except UnboundLocalError:
      return None