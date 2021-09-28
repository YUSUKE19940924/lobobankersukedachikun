import mysql.connector,time

from linebot.models import (
   TextSendMessage,TemplateSendMessage, PostbackAction,ButtonsTemplate
)

class Openingcost_management:

  def openingcost_search_error_message():
    reply_message = (TextSendMessage(text="入力頂いたメッセージに間違いがあるため処理できません。\n「()」「:」文字が半角になっているか、余分な余白が入っているか、入力した内容が登録されているか等の確認をお願いします。"))

    return reply_message

  def openingcost_operation_error_message():
    reply_message = (TextSendMessage(text="入力頂いたメッセージに間違いがあるため処理できません。\n「~~」「:」文字が半角になっているか、余分な余白が入っているか、入力した内容が登録されているか等の確認をお願いします。"))

    return reply_message

  def operation_module(receive_message):
    try:
        split_message = receive_message.split("~")
        openingfee_details = split_message[2].split("\n")
        openingfee_details.pop(0)
        reply_message = []
        for openingfee_detail in openingfee_details:
            openingfee_detail_split = openingfee_detail.split(":")
            reply_message.append(openingfee_detail_split[1])
    except:
        reply_message = Openingcost_management.borrowing_operation_error_message()

    return reply_message

  @classmethod
  def openingcost_management_handle(self,receive_message):
    reply_message = []

    user_id = receive_message[1]
        
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

    try:
        #conn = mysql.connector.connect(**config_local)
        conn = mysql.connector.connect(**config_local)
        conn.ping(reconnect=True)
        cur = conn.cursor(buffered=True)

    except:
        reply_message.append(TextSendMessage(text="データサーバーにアクセスできません。\n恐れ入りますが、もう一度メッセージの送信をお願いします。"))



    if receive_message[0] == "開業費管理システム起動":
        reply_message.append(TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            text='選択肢をタップしてください',
            actions=[
                PostbackAction(
                    label="開業費を確認する",
                    data="開業費管理システム_確認"
                ),
                PostbackAction(
                    label="開業費を計算する",
                    data="開業費管理システム_計算"
                ),
                PostbackAction(
                    label="開業費を操作する",
                    data="開業費管理システム_操作"
                )
            ]
        )
    ))

    elif ("開業費ID(開業費の検索)" in  receive_message[0]) == True:
        try:
            split_message = receive_message[0].split(":")
            id = split_message[1]
            cur.execute(f"select * from 開業費管理{user_id} where id = %s",(id,))
            row= cur.fetchone()
            res = (f"開業費ID:{row[0]}\n登録日時:{row[1]}\n支払日:{row[2]}\n費用項目:{row[3]}\n支払金額:{row[4]:,}円\n----------------------------------------\n")

            reply_message.append(TextSendMessage(text=(f"{res}開業費ID:{id}の検索結果を表示しています。")))
        except:
            reply_message.append(Openingcost_management.openingcost_search_error_message())


    elif ("開業費支払日(開業費の計算)" in  receive_message[0]) == True:
        try:
            split_message = receive_message[0].split(":")
            e_date = split_message [1]
            sum = 0
            cur.execute(f"select price from 開業費管理{user_id} where e_date = %s",(e_date,))
            rows= cur.fetchall()
            for row in rows:
                sum += row[0]
            res = f"現在の開業費総額:{sum:,}円"
            reply_message.append(TextSendMessage(text=res))
        except:
            reply_message.append(Openingcost_management.openingcost_search_error_message())

    elif ("~開業費を新規登録する~" in receive_message[0]) == True:   
        
        openingfee_conditions= Openingcost_management.operation_module(receive_message[0])
        time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(f"INSERT INTO 開業費管理{user_id} VALUES (id,%s,%s,%s,%s)",(time_stamp,openingfee_conditions[0],openingfee_conditions[1],openingfee_conditions[2]))
        conn.commit()
        cur.execute(f"SELECT * FROM 開業費管理{user_id} ORDER BY id DESC")
        row= cur.fetchone()
        res = (f"開業費ID:{row[0]}\n登録日時:{row[1]}\n支払日:{row[2]}\n費用項目:{row[3]}\n支払金額:{row[4]:,}円\n----------------------------------------\n")
        reply_message.append(TextSendMessage(text=(f"{res}登録が完了致しました。")))

    elif ("~支払日を変更する~" in receive_message[0]) == True: 
        openingfee_conditions= Openingcost_management.operation_module(receive_message[0])
        time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(f"UPDATE 開業費管理{user_id} SET r_date=%s,e_date=%s WHERE id=%s", (time_stamp,openingfee_conditions[1],openingfee_conditions[0]))

        conn.commit()
    
        cur.execute(f"select * from 開業費管理{user_id} where id = %s",(openingfee_conditions[0],))
        row= cur.fetchone()
        res = (f"開業費ID:{row[0]}\n登録日時:{row[1]}\n支払日:{row[2]}\n費用項目:{row[3]}\n支払金額:{row[4]:,}円\n----------------------------------------\n")
        reply_message.append(TextSendMessage(text=(f"{res}変更が完了致しました。")))

    elif ("~名目を変更する~" in receive_message[0]) == True: 
        openingfee_conditions= Openingcost_management.operation_module(receive_message[0])
        time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(f"UPDATE 開業費管理{user_id} SET r_date=%s,nominal=%s WHERE id=%s", (time_stamp,openingfee_conditions[1],openingfee_conditions[0]))

        conn.commit()
    
        cur.execute(f"select * from 開業費管理{user_id} where id = %s",(openingfee_conditions[0],))
        row= cur.fetchone()
        res = (f"開業費ID:{row[0]}\n登録日時:{row[1]}\n支払日:{row[2]}\n費用項目:{row[3]}\n支払金額:{row[4]:,}円\n----------------------------------------\n")
        reply_message.append(TextSendMessage(text=(f"{res}変更が完了致しました。")))

    elif ("~金額を変更する~" in receive_message[0]) == True: 
        openingfee_conditions= Openingcost_management.operation_module(receive_message[0])
        time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(f"UPDATE 開業費管理{user_id} SET r_date=%s,price=%s WHERE id=%s", (time_stamp,openingfee_conditions[1],openingfee_conditions[0]))

        conn.commit()
    
        cur.execute(f"select * from 開業費管理{user_id} where id = %s",(openingfee_conditions[0],))
        row= cur.fetchone()
        res = (f"開業費ID:{row[0]}\n登録日時:{row[1]}\n支払日:{row[2]}\n費用項目:{row[3]}\n支払金額:{row[4]:,}円\n----------------------------------------\n")
        reply_message.append(TextSendMessage(text=(f"{res}変更が完了致しました。")))

    elif ("~開業費を一括変更する~" in receive_message[0]) == True: 
        openingfee_conditions= Openingcost_management.operation_module(receive_message[0])
        time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(f"UPDATE 開業費管理{user_id} SET r_date=%s,e_date=%s,nominal=%s,price=%s WHERE id=%s", (time_stamp,openingfee_conditions[1],openingfee_conditions[2],openingfee_conditions[3],openingfee_conditions[0]))

        conn.commit()
    
        cur.execute(f"select * from 開業費管理{user_id} where id = %s",(openingfee_conditions[0],))
        row= cur.fetchone()
        res = (f"開業費ID:{row[0]}\n登録日時:{row[1]}\n支払日:{row[2]}\n費用項目:{row[3]}\n支払金額:{row[4]:,}円\n----------------------------------------\n")
        reply_message.append(TextSendMessage(text=(f"{res}変更が完了致しました。")))

    elif ("~開業費を削除する~" in receive_message[0]) == True: 
        try:
            split_message = receive_message[0].split(":")
            cur.execute((f"DELETE FROM 開業費管理{user_id} WHERE id = %s"),(split_message[1],))

            conn.commit()

            message0 = ""
            cur.execute(f"SELECT * FROM 開業費管理{user_id} ORDER BY id ")
            rows= cur.fetchall()
            for row in rows: 
                res = (f"開業費ID:{row[0]}\n登録日時:{row[1]}\n支払日:{row[2]}\n費用項目:{row[3]}\n支払金額:{row[4]:,}円\n----------------------------------------\n")
                message0 += res

            reply_message.append(TextSendMessage(text=(f"{message0}削除が完了致しました。")))
        except:
            reply_message.append(Openingcost_management.openingcost_operation_error_message())
            
    #操作================================================================================


    cur.close()
    conn.close()
    try:
        return reply_message
    except UnboundLocalError:
        return None

  @classmethod
  def openingcost_management_postback(self,postback_data):
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

    try:
        #conn = mysql.connector.connect(**config_local)
        conn = mysql.connector.connect(**config_local)
        conn.ping(reconnect=True)
        cur = conn.cursor(buffered=True)

    except:
        reply_message.append(TextSendMessage(text="データサーバーにアクセスできません。\n恐れ入りますが、もう一度メッセージの送信をお願いします。"))

    if postback_datum[0] == "開業費管理システム":
        if len(postback_datum) == 2:
            if postback_datum[1] == "確認":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="開業費の一覧を確認",
                            data="開業費管理システム_確認_一覧確認"
                        ),
                        PostbackAction(
                            label="開業費IDで内容を確認",
                            data="開業費管理システム_確認_開業費ID確認"
                        )
                    ]
                )
                ))


            elif postback_datum[1] == "計算":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="開業費の総額を計算",
                            data="開業費管理システム_計算_総額計算"
                        ),
                        PostbackAction(
                            label="支払日で借入内容を計算",
                            data="開業費管理システム_計算_支払日計算"
                        )
                    ]
                )
                ))
            
            elif postback_datum[1] == "操作":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="開業費を新規登録",
                            data="開業費管理システム_操作_新規登録"
                        ),
                        PostbackAction(
                            label="開業費を変更",
                            data="開業費管理システム_操作_変更"
                        ),
                        PostbackAction(
                            label="開業費を削除",
                            data="開業費管理システム_操作_削除"
                        )
                    ]
                )
                ))

        elif len(postback_datum) == 3:
            if postback_datum[2] == "変更":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="開業費の一部を変更",
                            data="開業費管理システム_操作_変更_一部変更"
                        ),
                        PostbackAction(
                            label="開業費の一括変更",
                            data="開業費管理システム_操作_変更_一括変更"
                        )
                    ]
                )
                ))

            elif postback_datum[2] == "一覧確認":
                message0 = ""
                cur.execute(f"SELECT * FROM 開業費管理{user_id} ORDER BY id ")
                rows= cur.fetchall()
                for row in rows: 
                    a = (f"開業費ID:{row[0]}\n登録日時:{row[1]}\n支払日:{row[2]}\n費用項目:{row[3]}\n支払金額:{row[4]:,}円\n----------------------------------------\nこちらが現在登録されている開業費の一覧です。")
                    message0 += a

                reply_message.append(TextSendMessage(text=message0))

            elif postback_datum[2] == "総額計算":
                sum = 0
                cur.execute(f"select * from 開業費管理{user_id}")
                rows= cur.fetchall()
                for row in rows:
                    sum += row[4]
                res = f"現在の開業費総額:{sum:,}円"
                reply_message.append(TextSendMessage(text=res))

            else:
                cur.execute("select content from 開業費管理一覧 where title = %s", (postback_datum[2],))
                res = cur.fetchone()
                reply_message.append(TextSendMessage(text=res[0]))



        elif len(postback_datum) == 4:
            if postback_datum[3] == "一部変更":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="開業費の支払日を変更",
                            data="開業費管理システム_操作_変更_一部変更_一部変更支払日"
                        ),
                        PostbackAction(
                            label="開業費の名目を変更",
                            data="開業費管理システム_操作_変更_一部変更_一部変更名目"
                        ),
                        PostbackAction(
                            label="開業費の金額を変更",
                            data="開業費管理システム_操作_変更_一部変更_一部変更金額"
                        )
                    ]
                )
                ))

            else:                      
                cur.execute("select content from 開業費管理一覧 where title = %s", (postback_datum[3],))
                res = cur.fetchone()
                reply_message.append(TextSendMessage(text=res[0]))

        elif len(postback_datum) == 5:
            cur.execute("select content from 開業費管理一覧 where title = %s", (postback_datum[4],))
            res = cur.fetchone()
            reply_message.append(TextSendMessage(text=res[0]))


    cur.close()
    conn.close()

    try:
        return reply_message
    except UnboundLocalError:
        return None