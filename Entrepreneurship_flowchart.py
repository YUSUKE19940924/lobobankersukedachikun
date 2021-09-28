import mysql.connector
from mysql.connector.cursor import RE_SQL_INSERT_STMT, RE_SQL_INSERT_VALUES

from First_Choice import First_Choice

from linebot.models import (
   TextSendMessage,TemplateSendMessage,PostbackAction,ButtonsTemplate
)
class Entrepreneurship_flowchart:
  @classmethod
  def entrepreneurship_flowchart_handle(self,receive_message):
    reply_message = []
     
    config_local = {'host':'localhost',
    'port':'3306',
    'user':'root',
    'password':'P@ssw0rd',
    'database':'chatbot'}

    config_cleardb = {'host':'us-cdbr-east-04.cleardb.com',
    'port':'3306',
    'user':'b532f809ae5b5c',
    'password':'c14c0399',
    'database':'heroku_542c06e97c0eef1'}

    config_cleardb1 = {'host':'us-cdbr-east-04.cleardb.com',
    'port':'3306',
    'user':'b4ef67a1821202',
    'password':'9fb4f091',
    'database':'heroku_905ff311118e2b7'}

    try:
        #conn = mysql.connector.connect(**config_local)
        conn = mysql.connector.connect(**config_cleardb1)
        conn.ping(reconnect=True)
        cur = conn.cursor(buffered=True)

    except:
        reply_message.append(TextSendMessage(text="データサーバーにアクセスできません。\n恐れ入りますが、もう一度メッセージの送信をお願いします。"))


     
#起業フローチャート$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if receive_message[0] == "起業フローチャートシステム起動":
        reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label="起業フローチャートを確認",
                        data="起業フローチャート_確認"
                    ),
                    PostbackAction(
                        label="起業フローチャートを登録",
                        data="起業フローチャート_登録"
                    ),
                        PostbackAction(
                        label="起業フローを詳しく学ぶ",
                        data="起業フローチャート_学習"
                    )
                ]
            )
        ))
        
        cur.close()
        conn.close()
    try:
        return reply_message
    except UnboundLocalError:
        return None

  @classmethod
  def entrepreneurship_flowchart_postback(self,postback_data):
    reply_message = []
    user_id = postback_data[1]
    postback_datum = postback_data[0].split("_")
        
    config_local = {'host':'localhost',
    'port':'3306',
    'user':'root',
    'password':'P@ssw0rd',
    'database':'chatbot'}

    config_cleardb = {'host':'us-cdbr-east-04.cleardb.com',
    'port':'3306',
    'user':'b532f809ae5b5c',
    'password':'c14c0399',
    'database':'heroku_542c06e97c0eef1'}

    config_cleardb1 = {'host':'us-cdbr-east-04.cleardb.com',
    'port':'3306',
    'user':'b4ef67a1821202',
    'password':'9fb4f091',
    'database':'heroku_905ff311118e2b7'}

    try:
        #conn = mysql.connector.connect(**config_local)
        conn = mysql.connector.connect(**config_cleardb1)
        conn.ping(reconnect=True)
        cur = conn.cursor(buffered=True)

    except:
        reply_message.append(TextSendMessage(text="データサーバーにアクセスできません。\n恐れ入りますが、もう一度メッセージの送信をお願いします。"))


    if postback_datum[0] == "起業フローチャート":
        if postback_datum[1] == "確認":
            flow_message = ""
            cur.execute(f"SELECT * FROM 起業フローチャート{user_id}")
            rows= cur.fetchall()
            id = 0
            for row in rows: 
                if row[2] == "未完了":
                    id = row[0]
                    break
            cur.execute(f"SELECT * FROM 起業フローチャート{user_id}")  
            rows= cur.fetchall()    
            for row in rows:     
                a = (f"{row[1]}［{row[2]}］")
                b = ("\n         l\n         l\n        V\n")
                if row == rows[7]:
                    flow_message += a
                else:
                    flow_message += (a + b)
            cur.execute(f"SELECT content FROM 起業フローチャート{user_id} WHERE id = %s ",(id,))
            next_content = cur.fetchone()

            prev_id = id - 1
            cur.execute(f"SELECT content FROM 起業フローチャート{user_id} WHERE id = %s ",(prev_id,))
            prev_content = cur.fetchone()  

            if next_content == None:
                reply_message.append(TextSendMessage(text=f"{flow_message}\n\n起業準備は全て完了です。\nここからが本当の意味での新たなスタートです。私は最高のパートナーとして、あなたをいつまでもサポートし続けますので、なんでも聞いてくださいね。"))
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='時間があれば、ICTについて確認してみてください',
                    actions=[
                        PostbackAction(
                            label="確認する",
                            data="ICT提案システム起動::ICT提案システム起動"
                        ),
                        PostbackAction(
                            label="確認しない",
                            data="確認しない"
                        )
                    ]
                )
            ))

            
            #初めて利用する場合
            elif prev_content == None:
                reply_message.append(TextSendMessage(text=f"{flow_message}\n\nこれから起業準備のスタートです。全力でサポートしますので、一緒に頑張りましょう\n初めの第一歩として「{next_content[0]}」をしましょう。"))
                cur.execute("select title,content from {0}".format(next_content[0],))
                b = cur.fetchall()
                reply_message.append(First_Choice.first_choice(b))
                reply_message.append(TextSendMessage(text=f"「{next_content[0]}」について知りたいことがあれば上の選択肢をタップしてください。"))
            
            else:
                reply_message.append(TextSendMessage(text=f"{flow_message}\n\n「{prev_content[0]}」まで完了しています。\n次にやることは「{next_content[0]}」です。"))
                cur.execute("select title,content from {0}".format(next_content[0],))
                choices = cur.fetchall()
                reply_message.append(First_Choice.first_choice(choices))
                reply_message.append(TextSendMessage(text=f"「{next_content[0]}」について知りたいことがあれば上の選択肢をタップしてください。"))

        elif postback_datum[1] == "登録":
            id = 0
            cur.execute(f"SELECT * FROM 起業フローチャート{user_id}")
            rows= cur.fetchall()
            for row in rows: 
                if row[2] == "未完了":
                    id = row[0]
                    break

            cur.execute(f"SELECT content FROM 起業フローチャート{user_id} WHERE id = %s ",(id,))
            next_content = cur.fetchone()
            prev_id = (id - 1)
            cur.execute(f"SELECT content FROM 起業フローチャート{user_id} WHERE id = %s ",(prev_id,))
            prev_content = cur.fetchone()

            if id == 1: 
                reply_message.append(TextSendMessage(text=f"これから起業準備のスタートです。全力でサポートしますので、一緒に頑張りましょう\n初めの第一歩として「{next_content[0]}」をしましょう。"))
                cur.execute(f"select title,content from {next_content[0]}")

                reply_message.append(TextSendMessage(text=f"「{next_content[0]}」が完了している場合は'完了'をタップしてください。"))
                
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="はい",
                            data="起業フローチャート_完了"
                        ),
                        PostbackAction(
                            label="いいえ",
                            data="いいえ"
                        )
                    ]
                )
            ))

            elif next_content == None:
                if len(postback_datum) == 2:
                    reply_message.append(TemplateSendMessage(
                    alt_text='Buttons template',
                    template=ButtonsTemplate(
                        text='1つ前を未完了で登録されますか？',
                        actions=[
                            PostbackAction(
                                label="はい",
                                data="起業フローチャート_未完了"
                            ),
                            PostbackAction(
                                label="いいえ",
                                data="起業フローチャート_登録_完了"
                            )
                        ]
                    )
                    ))
                elif len(postback_datum) == 3:
                    reply_message.append(TextSendMessage(text=f"起業準備は全て完了しています。\nここからが本当の意味での新たなスタートです。私は最高のパートナーとして、あなたをいつまでもサポートし続けますので、なんでも聞いてくださいね。"))
                    reply_message.append(TemplateSendMessage(
                    alt_text='Buttons template',
                    template=ButtonsTemplate(
                        text='時間があれば、ICTについて確認してみてください',
                        actions=[
                            PostbackAction(
                                label="確認する",
                                data="ICT提案システム起動::ICT提案システム起動"
                            ),
                            PostbackAction(
                                label="確認しない",
                                data="確認しない"
                            )
                        ]
                    )
                ))



            else:
                reply_message.append(TextSendMessage(text=f"「{next_content[0]}」が完了した場合は'完了'\n\n「{prev_content[0]}」が未完了だった場合は'1つ前を未完了で登録'\n\nのそれぞれをタップしてください。"))

                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="完了",
                            data="起業フローチャート_完了"
                        ),
                        PostbackAction(
                            label="1つ前を未完了で登録",
                            data="起業フローチャート_未完了"
                        )
                    ]
                )
            ))

        elif postback_datum[1] == "完了":
            flow_message = ""
            id = 0
            cur.execute(f"SELECT * FROM 起業フローチャート{user_id}")
            rows= cur.fetchall()
            for row in rows: 
                if row[2] == "未完了":
                    id = row[0]
                    break
            if id == 0:
                reply_message.append(TextSendMessage(text="起業準備は全て完了です。\nここからが本当の意味での新たなスタートです。私は最高のパートナーとして、あなたをいつまでもサポートし続けますので、なんでも聞いてくださいね。")) 
            else:
                cur.execute(f"UPDATE 起業フローチャート{user_id} SET judgement=%s WHERE id=%s", ("完了",id))
                conn.commit()
                cur.execute(f"SELECT content FROM 起業フローチャート{user_id} where id=%s", (id,))
                register_content = cur.fetchone()
                cur.execute(f"SELECT * FROM 起業フローチャート{user_id} ORDER BY id ")
                rows= cur.fetchall()
                for row in rows: 
                    a = (f"~{row[2]}~\n{row[1]}\n----------------------------------------\n")
                    flow_message += a
                reply_message.append(TextSendMessage(text=f"{flow_message}\n「{register_content[0]}」を完了で登録しました。"))
                next_id = (id + 1)
                if next_id == 9:
                    reply_message.append(TextSendMessage(text="起業準備は全て完了です。\nここからが本当の意味での新たなスタートです。私は最高のパートナーとして、あなたをいつまでもサポートし続けますので、なんでも聞いてくださいね。"))
                else:
                    cur.execute(f"SELECT content FROM 起業フローチャート{user_id} where id=%s", (next_id,))
                    next_content = cur.fetchone() 
                    cur.execute("select title,content from {0}".format(next_content[0],))
                    choices = cur.fetchall()
                    reply_message.append(First_Choice.first_choice(choices))
                    reply_message.append(TextSendMessage(text=f"次にやることは「{next_content[0]}」です。\n「{next_content[0]}」について知りたいことがあれば上の選択肢をタップしてください。"))

        elif postback_datum[1] == "未完了":
            id = 0
            flow_message = ""
            cur.execute(f"SELECT * FROM 起業フローチャート{user_id} ORDER BY id DESC")
            rows= cur.fetchall()
            for row in rows: 
                if row[2] == "完了":
                    id = row[0]
                    break

            cur.execute(f'UPDATE 起業フローチャート{user_id} SET judgement=%s WHERE id=%s', ("未完了",id))
            conn.commit()
            cur.execute(f"SELECT content FROM 起業フローチャート{user_id} where id=%s", (id,))
            prev_content = cur.fetchone()
            cur.execute(f"SELECT * FROM 起業フローチャート{user_id}")
            rows= cur.fetchall()
            for row in rows: 
                a = (f"~{row[2]}~\n{row[1]}\n----------------------------------------\n")
                flow_message += a
            reply_message.append(TextSendMessage(text=f"{flow_message}\n「{prev_content[0]}」を'未完了'で登録しました。"))
            cur.execute("select title,content from {0}".format(prev_content[0],))
            choices = cur.fetchall()
            reply_message.append(First_Choice.first_choice(choices))
            reply_message.append(TextSendMessage(text=f"次にやることは「{prev_content[0]}」です。「{prev_content[0]}」について知りたいことがあれば上の選択肢をタップしてください。"))

        elif postback_datum[1] == "学習":
            reply_message = []
            cur.execute("select title,content from 起業フローチャート")
            res = cur.fetchall()
            choices = First_Choice.first_choice(res)
            for choice in choices:
                reply_message.append(choice)
            
            
    cur.close()
    conn.close()


    try:
        return reply_message
    except UnboundLocalError:
        return None