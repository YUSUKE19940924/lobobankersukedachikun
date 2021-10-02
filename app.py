import os,mysql.connector

from First_Choice import First_Choice
from Morphological_analysis import Morphological_analysis
from First_time_use import First_time_use
from Credit_management import Credit_management
from Openingcost_management import Openingcost_management
from Entrepreneurship_flowchart import Entrepreneurship_flowchart
from Ict_propose import Ict_propose
from Founding_plan import Founding_plan
from Instruction_manual import Instruction_manual

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,PostbackEvent
)

from linebot.models import*





app = Flask(__name__)

line_bot_api = LineBotApi('チャネルアクセストークン')
handler = WebhookHandler('チャネルシークレット')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    receive_message = []
    reply_message = []

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

    receive_message.append(event.message.text)
    search_word = Morphological_analysis.morphological_analysis(receive_message[0])

    profile = line_bot_api.get_profile(event.source.user_id)
    user_id = profile.user_id
    user_name = profile.display_name

    receive_message.append(user_id)
    receive_message.append(user_name)
    
    
    cur.execute("select user_id from ユーザーID管理簿 where user_id = %s",(user_id,))
    res = cur.fetchone()
    if res == None:
        reply_message = (First_time_use.first_time_use_handle(receive_message))
    

    elif ("債権管理" in receive_message[0] or "借入"in receive_message[0]) == True:
        reply_message = (Credit_management.credit_management_handle(receive_message))

    elif ("開業費" in receive_message[0]) == True: 
        reply_message = (Openingcost_management.openingcost_management_handle(receive_message))
    

    elif ("起業フローチャート" in receive_message[0]) == True:
        reply_message = (Entrepreneurship_flowchart.entrepreneurship_flowchart_handle(receive_message))
    
    elif ("ICT提案" in receive_message[0]) == True:
        reply_message = (Ict_propose.ict_propose_handle(receive_message))

    elif ("創業計画書" in receive_message[0]) == True:
        reply_message = (Founding_plan.founding_plan_handle(receive_message))

    elif ("取扱説明書" in receive_message[0]) == True:
        reply_message = (Instruction_manual.instruction_manual_handle(receive_message))


    else:
        if len(reply_message) == 0:
            cur.execute("select content from 経営用語辞典 where word = %s",(search_word,))
            res = cur.fetchone()
            if res == None:
                cur.execute("select content from 経営用語辞典1 where word = %s",(search_word,))
                res = cur.fetchone()
                if res == None:
                    cur.execute("select content from 経営用語辞典2 where word = %s",(search_word,))
                    res = cur.fetchone()
                    if res == None:
                        res = ["私にはわかりません。別の質問なら何とか答えられるかもしれません。"]
            
            reply_message.append(TextSendMessage(text=res[0]))
            try:
                cur.execute(f"select title,content from {search_word}")
                res = cur.fetchall()
                reply_message.append(First_Choice.first_choice(res))
            except mysql.connector.errors.ProgrammingError:
                pass

    if len(reply_message) == 1:
        line_bot_api.reply_message(
        event.reply_token,
        [reply_message[0]])
    elif len(reply_message) == 2:
        line_bot_api.reply_message(
        event.reply_token,
        [reply_message[0],reply_message[1]])
    else:
        try:
            line_bot_api.reply_message(
            event.reply_token,
            [reply_message[0]])
        except:
            line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text="エラーです。\n恐れ入りますが、入力頂いたメッセージ欄を確認してください。")])


    cur.close()
    conn.close()




#Post========================================================================================
    @handler.add(PostbackEvent)
    def on_postback(event): 
       
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
        
        postback_data = []

        postback_data.append(event.postback.data)

        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = profile.user_id
        postback_data.append(user_id)

        postback_datum = postback_data[0].split("::")
        reply_message_postback = []
        reply_senario_postback = None
        print(postback_datum)

        if len(postback_datum) == 1:
            if ("債権管理システム" in postback_data[0]) == True:
                reply_message_postback = (Credit_management.credit_management_postback(postback_data))

            elif ("開業費管理システム" in postback_data[0]) == True:
                reply_message_postback = (Openingcost_management.openingcost_management_postback(postback_data))
                
            elif ("起業フローチャート" in postback_data[0]) == True:
                reply_message_postback = (Entrepreneurship_flowchart.entrepreneurship_flowchart_postback(postback_data))

            elif ("ICT提案システム" in postback_data[0])  == True:
                reply_message_postback = (Ict_propose.ict_propose_postback(postback_data))

            elif ("創業計画書サポート" in postback_data[0])  == True:
                reply_message_postback = (Founding_plan.founding_plan_postback(postback_data))

            elif ("取扱説明書" in postback_data[0])  == True:
                reply_message_postback = (Instruction_manual.instruction_manual_postback(postback_data))

            else:
                reply_message_postback.append(TextSendMessage(text=postback_data))
       
       
        else:
            if ("創業計画書サポート" in postback_datum[0])  == True:
                reply_message_postback = (Founding_plan.founding_plan_handle(postback_datum))
            
            elif ("ICT提案システム" in postback_datum[0])  == True:
                reply_message_postback = (Ict_propose.ict_propose_handle(postback_datum))


            else:
                reply_message_postback.append(TextSendMessage(text=postback_datum[0]))

                
                try:
                    search_word = postback_datum[1]
                    
                except IndexError:
                    reply_message_postback.append(TextSendMessage(
                    text="答えがわかりません"))


                cur.execute("select title,content from {0}".format(search_word))
                b = cur.fetchall()
                reply_senario_postback = First_Choice.first_choice(b)

        if len(reply_message_postback) == 1 and reply_senario_postback == None:
            line_bot_api.reply_message(
            event.reply_token,
            [reply_message_postback[0]])   

        elif len(reply_message_postback) == 2 and reply_senario_postback == None:
            line_bot_api.reply_message(
            event.reply_token,
            [reply_message_postback[0],reply_message_postback[1]])

        elif len(reply_message_postback) == 3 and reply_senario_postback == None:
            line_bot_api.reply_message(
            event.reply_token,
            [reply_message_postback[0],reply_message_postback[1],reply_message_postback[2]])     

        elif len(reply_message_postback) == 4 and reply_senario_postback == None:
            line_bot_api.reply_message(
            event.reply_token,
            [reply_message_postback[0],reply_message_postback[1],reply_message_postback[2],reply_message_postback[3]])

        elif len(reply_message_postback) == 5 and reply_senario_postback == None:
            line_bot_api.reply_message(
            event.reply_token,
            [reply_message_postback[0],reply_message_postback[1],reply_message_postback[2],reply_message_postback[3],reply_message_postback[4]])      

        elif len(reply_message_postback) == 6 and reply_senario_postback == None:
            line_bot_api.reply_message(
            event.reply_token,
            [reply_message_postback[0],reply_message_postback[1],reply_message_postback[2],reply_message_postback[3],reply_message_postback[4],reply_message_postback[5]])      

        elif len(reply_message_postback) == 7 and reply_senario_postback == None:
            line_bot_api.reply_message(
            event.reply_token,
            [reply_message_postback[0],reply_message_postback[1],reply_message_postback[2],reply_message_postback[3],reply_message_postback[4],reply_message_postback[5]],reply_message_postback[6])      

        elif len(reply_message_postback) == 8 and reply_senario_postback == None:
            line_bot_api.reply_message(
            event.reply_token,
            [reply_message_postback[0],reply_message_postback[1],reply_message_postback[2],reply_message_postback[3],reply_message_postback[4],reply_message_postback[5],reply_message_postback[6],reply_message_postback[7]])      

        elif len(reply_message_postback) == 9 and reply_senario_postback == None:
            line_bot_api.reply_message(
            event.reply_token,
            [reply_message_postback[0],reply_message_postback[1],reply_message_postback[2],reply_message_postback[3],reply_message_postback[4],reply_message_postback[5],reply_message_postback[6],reply_message_postback[7],reply_message_postback[8]])      

        elif len(reply_message_postback) == 0 and reply_senario_postback is not None: 
            line_bot_api.reply_message(
            event.reply_token,
            [reply_senario_postback])    
        else:
            line_bot_api.reply_message(
            event.reply_token,
            [reply_message_postback[0],reply_senario_postback])       

        cur.close()
        conn.close()    

if __name__ == '__main__':
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port, debug=True)


