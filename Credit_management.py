import math,mysql.connector,time

from linebot.models import (
   TextSendMessage,TemplateSendMessage, PostbackAction,ButtonsTemplate
)

class Credit_management:

  def borrowing_search_error_message():
    reply_message = (TextSendMessage(text="入力頂いたメッセージに間違いがあるため処理できません。\n「()」「:」文字が半角になっているか、余分な余白が入っているか、入力した内容が登録されているか等の確認をお願いします。"))

    return reply_message

  def borrowing_operation_error_message():
    reply_message = (TextSendMessage(text="入力頂いたメッセージに間違いがあるため処理できません。\n「~~」「:」文字が半角になっているか、余分な余白が入っているか、入力した内容が登録されているか等の確認をお願いします。"))

    return reply_message

  def operation_module(receive_message):
    try:
        split_message = receive_message.split("~")
        bollowing_details = split_message[2].split("\n")
        bollowing_details.pop(0)
        reply_message = []
        for bollowing_detail in bollowing_details:
            bollowing_detail_split = bollowing_detail.split(":")
            reply_message.append(bollowing_detail_split[1])
    except:
        reply_message = Credit_management.borrowing_operation_error_message()

    return reply_message

  @classmethod
  def credit_management_handle(self,receive_message):
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




     if receive_message[0] == "債権管理システム起動":
        reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label="借入内容を確認する",
                        data="債権管理システム_確認"
                    ),
                    PostbackAction(
                        label="借入内容を計算する",
                        data="債権管理システム_計算"
                    ),
                    PostbackAction(
                        label="借入内容を操作する",
                        data="債権管理システム_操作"
                    )
                ]
            )
        ))



     elif ("借入ID(借入内容の検索)" in  receive_message[0]) == True:
        try:
            split_message = receive_message[0].split(":")
            id = split_message[1]
            cur.execute(f"select * from 債権管理{user_id} where id = %s",(id,))
            row= cur.fetchone()
            borrowing_information = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}月\n返済日:{row[11]}\n借入利率:{row[12]}\n----------------------------------------\n")
            reply_message.append(TextSendMessage(text=f"{borrowing_information}\n借入ID:{id}の検索結果を表示してます。"))
        except:
            reply_message.append(Credit_management.borrowing_search_error_message())


     elif ("借入金融機関(借入内容の検索)" in  receive_message[0]):
        try:
            split_message = receive_message[0].split(":")
            f_i = split_message[1]
            cur.execute(f"select * from 債権管理{user_id} where f_i = %s",(f_i,))
        except:
            reply_message.append(Credit_management.borrowing_search_error_message())
            rows= cur.fetchall()
            borrowing_detail = ""

            if len(rows) == 1:
                row = rows[0]
                borrowing_details = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}月\n返済日:{row[11]}\n借入利率:{row[12]}")
                reply_message.append(TextSendMessage(text=borrowing_details))
            else:
                for row in rows:
                    borrowing_details = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}月\n返済日:{row[11]}\n借入利率:{row[12]}\n----------------------------------------\n")
                    borrowing_detail += borrowing_details
                reply_message.append(TextSendMessage(text=borrowing_detail))


     elif ("借入金融機関(当初借入金総額)" in  receive_message[0]) == True:
        try:
            split_message = receive_message[0].split(":")         
            f_i = split_message[1]
            b = 0
            cur.execute(f"select b_a from 債権管理{user_id} where f_i = %s",(f_i,))
            rows= cur.fetchall()
            for row in rows:
                b += row[0]
                d = "{}の当初の借入金総額:{:,}円".format(f_i,b)
            reply_message.append(TextSendMessage(text=d))
        except:
            reply_message.append(Credit_management.borrowing_search_error_message())

     elif ("借入金融機関(現在借入金総額)" in  receive_message[0]) == True:
        try:
            split_message = receive_message[0].split(":")    
            f_i = split_message[1]
            b = 0
            cur.execute(f"select r_a from 債権管理{user_id} where f_i = %s",(f_i,))
            rows= cur.fetchall()
            for row in rows:
                b += row[0]
                d = "{}の現在の借入金総額:{:,}円".format(f_i,b)
            reply_message.append(TextSendMessage(text=d))
        except:
            reply_message.append(Credit_management.borrowing_search_error_message())

     elif ("借入金融機関(毎月の返済額)" in  receive_message[0]) == True:
        try:
            split_message = receive_message[0].split(":")    
            f_i = split_message[1]
            b = 0
            cur.execute(f"select m_r_a from 債権管理{user_id} where f_i = %s",(f_i,))
            rows= cur.fetchall()
            for row in rows:
                b += row[0]
                d = "{}の毎月の返済額:{:,}円".format(f_i,b)
            reply_message.append(TextSendMessage(text=d))
        except:
            reply_message.append(Credit_management.borrowing_search_error_message())
    
     elif ("借入ID(当初の支払利子計算)"in  receive_message[0]) == True:
        try:
            split_message = receive_message[0].split(":")    
            id = split_message[1]
            cur.execute(f"SELECT * FROM 債権管理{user_id} WHERE id = %s ",(id,))
            row= cur.fetchone()
            r_a = row[3]
            i_a = 0
            for c in range(row[7]*12 + row[8]):
                i_a = i_a + r_a*(row[12]/100/12)
                r_a = r_a-row[5]
            reply_i_a = math.ceil(i_a)
            d = (f"借入ID:{id}の当初の借入から完済までの支払利子は{reply_i_a}円です。\n※本シミュレーションにより試算される利子はあくまでも目安となりますことをご了承ください。")
            reply_message.append(TextSendMessage(text=d))
        except:
            reply_message.append(Credit_management.borrowing_search_error_message())


     elif ("借入ID(現在の支払利子計算)"in  receive_message[0]) == True:
        try:
            split_message = receive_message[0].split(":")    
            id = split_message[1]
            cur.execute(f"SELECT * FROM 債権管理{user_id} WHERE id = %s ",(id,))
            row= cur.fetchone()
            r_a = row[4]
            i_a = 0
            for c in range(row[9]*12 + row[10]):
                i_a = i_a + r_a*(row[12]/100/12)
                r_a = r_a-row[5]
            reply_i_a = math.ceil(i_a)
            d = (f"借入ID:{id}の現在から完済までの支払利子は{reply_i_a}円です。\n※本シミュレーションにより試算される利子はあくまでも目安となりますことをご了承ください。")
            reply_message.append(TextSendMessage(text=d))
        except:
            reply_message.append(Credit_management.borrowing_search_error_message())

     elif ("~借入内容を新規登録する~" in receive_message[0]) == True: 
         bollowing_conditions = Credit_management.operation_module(receive_message[0])
         if type(bollowing_conditions) == TextSendMessage:
            reply_message.append(bollowing_conditions)
         else:
            try:
                bollowing_conditions = Credit_management.operation_module(receive_message[0])
                time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
                cur.execute(f"INSERT INTO 債権管理{user_id} VALUES (id,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(time_stamp,bollowing_conditions[0],bollowing_conditions[1],bollowing_conditions[2],bollowing_conditions[3],bollowing_conditions[4],bollowing_conditions[5],bollowing_conditions[6],bollowing_conditions[7],bollowing_conditions[8],bollowing_conditions[9],bollowing_conditions[10]))
                conn.commit()

                cur.execute(f"SELECT * FROM 債権管理{user_id} ORDER BY id DESC")
                row= cur.fetchone()
                a = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}ヶ月\n返済日:{row[11]}\n借入利率:{row[12]}%\n----------------------------------------\n")
                reply_message.append(TextSendMessage(text=(f"{a}登録が完了致しました。")))
            except:
                reply_message.append(TextSendMessage(text="入力頂いたメッセージでは検索できません。\n「~~」「:」文字が半角になっているか、余分な余白が入っているか、入力した内容が登録されているか等の確認をお願いします。"))

     elif ("~借入内容を一括変更する~" in receive_message[0]) == True: 
        bollowing_conditions = Credit_management.operation_module(receive_message[0])
        if type(bollowing_conditions) == TextSendMessage:
            reply_message.append(bollowing_conditions)
        else:
            bollowing_conditions = Credit_management.operation_module(receive_message[0])
            time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
            cur.execute(f'UPDATE 債権管理{user_id} SET datetime=%s,f_i=%s,b_a=%s,r_a=%s,m_r_a=%s,b_d=%s,b_y=%s,b_m=%s,r_y=%s,r_m=%s,r_d=%s,b_i_r=%s WHERE id=%s', (time_stamp,bollowing_conditions[1],bollowing_conditions[2],bollowing_conditions[3],bollowing_conditions[4],bollowing_conditions[5],bollowing_conditions[6],bollowing_conditions[7],bollowing_conditions[8],bollowing_conditions[9],bollowing_conditions[10],bollowing_conditions[11],bollowing_conditions[0]))
            conn.commit()

            cur.execute(f"SELECT * FROM 債権管理{user_id} WHERE id=%s",(bollowing_conditions[0],))
            row= cur.fetchone()
            a = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}ヶ月\n返済日:{row[11]}\n借入利率:{row[12]}%\n----------------------------------------\n")

            reply_message.append(TextSendMessage(text=(f"{a}一括変更が完了致しました。")))
    
     elif ("~借入金額を変更する~" in receive_message[0]) == True: 
            bollowing_conditions = Credit_management.operation_module(receive_message[0])
            if type(bollowing_conditions) == TextSendMessage:
                reply_message.append(bollowing_conditions)
            else:
                time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
                cur.execute(f'UPDATE 債権管理{user_id} SET datetime=%s,b_a=%s WHERE id=%s', (time_stamp,bollowing_conditions[1],bollowing_conditions[0]))
                conn.commit()
                cur.execute(f"SELECT * FROM 債権管理{user_id} WHERE id=%s",(bollowing_conditions[0],))
                row= cur.fetchone()
                a = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}ヶ月\n返済日:{row[11]}\n借入利率:{row[12]}%\n----------------------------------------\n")
                reply_message.append(TextSendMessage(text=(f"{a}借入金額の変更を完了致しました。")))

        
     elif ("~借入残額を変更する~" in receive_message[0]) == True: 
            bollowing_conditions = Credit_management.operation_module(receive_message[0])
            if type(bollowing_conditions) == TextSendMessage:
                reply_message.append(bollowing_conditions)
            else:
                time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
                cur.execute(f'UPDATE 債権管理{user_id} SET datetime=%s,r_a=%s WHERE id=%s', (time_stamp,bollowing_conditions[1],bollowing_conditions[0]))
                conn.commit()

                cur.execute(f"SELECT * FROM 債権管理{user_id} WHERE id=%s",(bollowing_conditions[0],))
                row= cur.fetchone()
                a = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}ヶ月\n返済日:{row[11]}\n借入利率:{row[12]}%\n----------------------------------------\n")


                reply_message.append(TextSendMessage(text=(f"{a}借入残額の変更を完了致しました。")))

     elif ("~毎月の返済額を変更する~" in receive_message[0]) == True: 
        bollowing_conditions = Credit_management.operation_module(receive_message[0])
        if type(bollowing_conditions) == TextSendMessage:
            reply_message.append(bollowing_conditions)
        else:
            time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
            cur.execute(f'UPDATE 債権管理{user_id} SET datetime=%s,m_r_a=%s WHERE id=%s', (time_stamp,bollowing_conditions[1],bollowing_conditions[0]))
            conn.commit()

            cur.execute(f"SELECT * FROM 債権管理{user_id} WHERE id=%s",(bollowing_conditions[0],))
            row= cur.fetchone()
            a = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}ヶ月\n返済日:{row[11]}\n借入利率:{row[12]}%\n----------------------------------------\n")

            reply_message.append(TextSendMessage(text=(f"{a}毎月の返済額の変更を完了致しました。")))

     elif ("~借入日を変更する~" in receive_message[0]) == True: 
        bollowing_conditions = Credit_management.operation_module(receive_message[0])
        if type(bollowing_conditions) == TextSendMessage:
            reply_message.append(bollowing_conditions)
        else:
            time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
            cur.execute(f'UPDATE 債権管理{user_id} SET datetime=%s,b_d=%s WHERE id=%s', (time_stamp,bollowing_conditions[1],bollowing_conditions[0]))
            conn.commit()

            cur.execute(f"SELECT * FROM 債権管理{user_id} WHERE id=%s",(bollowing_conditions[0],))
            row= cur.fetchone()
            a = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}ヶ月\n返済日:{row[11]}\n借入利率:{row[12]}%\n----------------------------------------\n")

            reply_message.append(TextSendMessage(text=(f"{a}借入日の変更を完了致しました。")))

     elif ("~借入期間を変更する~" in receive_message[0]) == True: 
        bollowing_conditions = Credit_management.operation_module(receive_message[0])
        if type(bollowing_conditions) == TextSendMessage:
            reply_message.append(bollowing_conditions)
        else:
            time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
            cur.execute(f'UPDATE 債権管理{user_id} SET datetime=%s,b_y=%s,b_m=%s WHERE id=%s', (time_stamp,bollowing_conditions[1],bollowing_conditions[2],bollowing_conditions[0]))
            conn.commit()

            cur.execute(f"SELECT * FROM 債権管理{user_id} WHERE id=%s",(bollowing_conditions[0],))
            row= cur.fetchone()
            a = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}ヶ月\n返済日:{row[11]}\n借入利率:{row[12]}%\n----------------------------------------\n")

            reply_message .append(TextSendMessage(text=(f"{a}借入期間の変更を完了致しました。")))

     elif ("~残存期間を変更する~" in receive_message[0]) == True: 
        bollowing_conditions = Credit_management.operation_module(receive_message[0])
        if type(bollowing_conditions) == TextSendMessage:
            reply_message.append(bollowing_conditions)
        else:
            time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
            cur.execute(f'UPDATE 債権管理{user_id} SET datetime=%s,r_y=%s,r_m=%s WHERE id=%s', (time_stamp,bollowing_conditions[1],bollowing_conditions[2],bollowing_conditions[0]))
            conn.commit()

            cur.execute(f"SELECT * FROM 債権管理{user_id} WHERE id=%s",(bollowing_conditions[0],))
            row= cur.fetchone()
            a = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}ヶ月\n返済日:{row[11]}\n借入利率:{row[12]}%\n----------------------------------------\n")

            reply_message.append(TextSendMessage(text=(f"{a}残存期間の変更を完了致しました。")))

     elif ("~金融機関名を変更する~" in receive_message[0]) == True: 
        bollowing_conditions = Credit_management.operation_module(receive_message[0])
        if type(bollowing_conditions) == TextSendMessage:
            reply_message.append(bollowing_conditions)
        else:
            time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
            cur.execute(f'UPDATE 債権管理{user_id} SET datetime=%s,f_i=%s WHERE id=%s', (time_stamp,bollowing_conditions[1],bollowing_conditions[0]))
            conn.commit()
            cur.execute(f"SELECT * FROM 債権管理{user_id} WHERE id=%s",(bollowing_conditions[0],))
            row= cur.fetchone()
            a = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}ヶ月\n返済日:{row[11]}\n借入利率:{row[12]}%\n----------------------------------------\n")

            reply_message.append(TextSendMessage(text= (f"{a}金融機関名の変更を完了致しました。")))

     elif ("~返済日を変更する~" in receive_message[0]) == True: 
        bollowing_conditions = Credit_management.operation_module(receive_message[0])
        if type(bollowing_conditions) == TextSendMessage:
            reply_message.append(bollowing_conditions)
        else:
            time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
            cur.execute(f'UPDATE 債権管理{user_id} SET datetime=%s,r_d WHERE id=%s', (time_stamp,bollowing_conditions[1],bollowing_conditions[0]))
            conn.commit()

            cur.execute(f"SELECT * FROM 債権管理{user_id} WHERE id=%s",(bollowing_conditions[0],))
            row= cur.fetchone()
            a = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}ヶ月\n返済日:{row[11]}\n借入利率:{row[12]}%\n----------------------------------------\n")

            reply_message.append(TextSendMessage(text=(f"{a}返済日の変更を完了致しました。")))

     elif ("~借入利率を変更する~" in receive_message[0]) == True: 
        bollowing_conditions = Credit_management.operation_module(receive_message[0])
        if type(bollowing_conditions) == TextSendMessage:
            reply_message.append(bollowing_conditions)
        else:
            time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
            cur.execute(f'UPDATE 債権管理{user_id} SET datetime=%s,r_y=b_i_r WHERE id=%s', (time_stamp,bollowing_conditions[1],bollowing_conditions[0]))
            
            conn.commit()

            cur.execute(f"SELECT * FROM 債権管理{user_id} WHERE id=%s",(bollowing_conditions[0],))
            row= cur.fetchone()
            a = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}ヶ月\n返済日:{row[11]}\n借入利率:{row[12]}%\n----------------------------------------\n")

            reply_message.append(TextSendMessage(text=(f"{a}借入利率の変更を完了致しました。")))

     elif ("~借入内容を削除する~" in receive_message[0]) == True:
        try:  
            split_message = receive_message[0].split(":")
            cur.execute((f"DELETE FROM 債権管理{user_id} WHERE id = %s"),(split_message[1],))
            conn.commit()
            message_0 = ""
            cur.execute(f"SELECT * FROM 債権管理{user_id} ORDER BY id ")
            rows= cur.fetchall()
            for row in rows: 
                a = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}月\n返済日:{row[11]}\n借入利率:{row[12]}%\n----------------------------------------\n")
                message_0 += a
            reply_message.append(TextSendMessage(text=(f"{message_0}削除が完了致しました。")))
        except:
            reply_message.append(Credit_management.borrowing_search_error_message())


     cur.close()
     conn.close()
     try:
        return reply_message
     except UnboundLocalError:
        return None









  @classmethod
  def credit_management_postback(self,postback_data):
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
        


    if postback_datum[0] == "債権管理システム":
        if len(postback_datum) == 2:
            if postback_datum[1] == "確認":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="借入内容の一覧を確認",
                            data="債権管理システム_確認_一覧確認"
                        ),
                        PostbackAction(
                            label="借入IDで借入内容を確認",
                            data="債権管理システム_確認_借入ID確認"
                        ),
                        PostbackAction(
                            label="金融機関で借入内容を確認",
                            data="債権管理システム_確認_借入金融機関確認"
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
                            label="借入金を計算",
                            data="債権管理システム_計算_借入金計算"
                        ),
                        PostbackAction(
                            label="毎月の返済額を計算",
                            data="債権管理システム_計算_毎月の返済額計算"
                        ),
                        PostbackAction(
                            label="支払い利子を計算",
                            data="債権管理システム_計算_支払利子計算"
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
                            label="借入内容を新規登録",
                            data="債権管理システム_操作_新規登録"
                        ),
                        PostbackAction(
                            label="借入内容を変更",
                            data="債権管理システム_操作_変更"
                        ),
                        PostbackAction(
                            label="借入内容を削除",
                            data="債権管理システム_操作_削除"
                        )
                    ]
                )
            ))

        elif len(postback_datum) == 3:
            if postback_datum[2] == "借入金計算":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="当初の借入金総額を計算",
                            data="債権管理システム_計算_借入金計算_当初借入金総額計算"
                        ),
                        PostbackAction(
                            label="金融機関毎の当初の借入金総額を計算",
                            data="債権管理システム_計算_借入金計算_金融機関毎当初借入金総額計算"
                        ),
                        PostbackAction(
                            label="現在の借入金総額を計算",
                            data="債権管理システム_計算_借入金計算_現在借入金総額計算"
                        ),
                        PostbackAction(
                            label="金融機関毎の現在の借入金総額を計算",
                            data="債権管理システム_計算_借入金計算_金融機関毎現在借入金総額計算"
                        )
                    ]
                )
            ))

            elif postback_datum[2] == "毎月の返済額計算":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="毎月の返済額を計算",
                            data="債権管理システム_計算_毎月返済額計算_毎月返済額計算"
                        ),
                        PostbackAction(
                            label="金融機関毎の毎月の返済を額を計算",
                            data="債権管理システム_計算_毎月返済額計算_金融機関毎毎月返済額計算"
                        )
                    ]
                )
            ))
            elif postback_datum[2] == "支払利子計算":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="借入当初の支払い利子計算",
                            data="債権管理システム_計算_支払利子計算_借入当初支払利子計算"
                        ),
                        PostbackAction(
                            label="現在の支払利子計算",
                            data="債権管理システム_計算_支払利子計算_現在支払利子計算"
                        )
                    ]
                )
            ))

            elif postback_datum[2] == "変更":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="借入内容の一部変更",
                            data="債権管理システム_操作_変更_一部変更"
                        ),
                        PostbackAction(
                            label="借入内容の一括変更",
                            data="債権管理システム_操作_変更_一括変更"
                        )
                    ]
                )
            ))

            elif postback_datum[2] == "一覧確認":
                message0 = ""
                cur.execute(f"SELECT * FROM 債権管理{user_id} ORDER BY id ")
                rows= cur.fetchall()
                for row in rows: 
                    a = (f"借入ID:{row[0]}\n登録日時:{row[1]}\n金融機関名:{row[2]}\n借入金額:{math.floor(row[3]/10000)}万円\n借入残額:{math.floor(row[4]/10000)}万円\n毎月の返済額:{math.floor(row[5])}円\n借入日:{row[6]}\n借入期間:{row[7]}年{row[8]}ヶ月\n残存期間:{row[9]}年{row[10]}月\n返済日:{row[11]}\n借入利率:{row[12]}%\n----------------------------------------\n")
                    message0 += a

                reply_message.append(TextSendMessage(text=f"{message0}\nこちらが現在の借入一覧となります。"))

            else:
                cur.execute("select content from 債権管理一覧 where title = %s", (postback_datum[2],))
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
                            label="金額を変更する",
                            data="債権管理システム_操作_変更_一部変更_一部変更金額"
                        ),
                        PostbackAction(
                            label="期間を変更する",
                            data="債権管理システム_操作_変更_一部変更_一部変更期間"
                        ),
                        PostbackAction(
                            label="その他を変更する",
                            data="債権管理システム_操作_変更_一部変更_一部変更その他"
                        )
                    ]
                )
            ))

            elif postback_datum[3] == "当初借入金総額計算":
                cur.execute(f"SELECT * FROM 債権管理{user_id}")
                rows= cur.fetchall()
                c = 0
                for row in rows:
                    c = c + row[3]
                    res = "当初の借入総額:{:,}円".format(c)
                reply_message.append(TextSendMessage(text=res))
            
            elif postback_datum[3] == "現在借入金総額計算":
                    cur.execute(f"SELECT * FROM 債権管理{user_id}")
                    rows= cur.fetchall()
                    borrowing_amount = 0
                    for row in rows:
                        borrowing_amount += row[4]
                        res = f"現在の借入金総額:{borrowing_amount:,}円"
                    reply_message.append(TextSendMessage(text=res))

            elif postback_datum[3] == "毎月返済額計算":
                cur.execute(f"SELECT * FROM 債権管理{user_id}")
                rows= cur.fetchall()
                repayment_amount = 0
                for row in rows:
                    repayment_amount += row[5]
                    res = f"毎月の返済金総額:{repayment_amount:,}円"
                reply_message.append(TextSendMessage(text=res))


            else:
                cur.execute("select content from 債権管理一覧 where title = %s", (postback_datum[3],))
                res = cur.fetchone()
                reply_message.append(TextSendMessage(text=res[0]))


        elif len(postback_datum) == 5:
            if postback_datum[4] == "一部変更金額":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="借入金額を変更する",
                            data="債権管理システム_操作_変更_一部変更_一部変更金額_一部変更借入金額"
                        ),
                        PostbackAction(
                            label="借入残額を変更する",
                            data="債権管理システム_操作_変更_一部変更_一部変更金額_一部変更借入残額"
                        ),
                        PostbackAction(
                            label="毎月の返済額を変更する",
                            data="債権管理システム_操作_変更_一部変更_一部変更金額_一部変更毎月の返済額"
                        )
                    ]
                )
            ))
        

            elif postback_datum[4] == "一部変更期間":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="借入日を変更する",
                            data="債権管理システム_操作_変更_一部変更_一部変更期間_一部変更借入日"
                        ),
                        PostbackAction(
                            label="借入期間を変更する",
                            data="債権管理システム_操作_変更_一部変更_一部変更期間_一部変更借入期間"
                        ),
                        PostbackAction(
                            label="残存期間を変更する",
                            data="債権管理システム_操作_変更_一部変更_一部変更期間_一部変更残存期間"
                        )
                    ]
                )
            ))

            elif postback_datum[4] == "一部変更その他":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="金融機関を変更する",
                            data="債権管理システム_操作_変更_一部変更_一部変更その他_一部変更金融機関名"
                        ),
                        PostbackAction(
                            label="返済日を変更する",
                            data="債権管理システム_操作_変更_一部変更_一部変更その他_一部変更返済日"
                        ),
                        PostbackAction(
                            label="借入利率を変更する",
                            data="債権管理システム_操作_変更_一部変更_一部変更その他_一部変更借入利率"
                        )
                    ]
                )
            )) 

        elif len(postback_datum) == 6:
            cur.execute("select content from 債権管理一覧 where title = %s", (postback_datum[5],))
            res = cur.fetchone()
            reply_message.append(TextSendMessage(text=res[0]))


    cur.close()
    conn.close()

    try:
        return reply_message
    except UnboundLocalError:
        return None
