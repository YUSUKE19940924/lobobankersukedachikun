import os,mysql.connector
from flask import Flask, request, abort

from First_Choice import First_Choice
from Morphological_analysis import Morphological_analysis

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)



app = Flask(__name__)

line_bot_api = LineBotApi('L9nOYlTdQr2tvB62rOTtakfayJvw99bB9JZh0brzXQvsaZ86pY5Zt4c5VT94x+Tn+1tN86x4hfyCmrm6HYUK0J0a5smndbsnzoOG/Zs/V5EX/N9nQZpWFUuqJsJqFORolekBtR8JaO+l4T2EPP2h+AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('790c279873d8763924c7673463a30a82')


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
    """
    conn = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='P@ssw0rd',
    database='chatbot'
    )   
    """
    conn = mysql.connector.connect(
    host='us-cdbr-east-04.cleardb.com',
    port='3306',
    user='be12bd3f68a8ac',
    password='36cefdb1',
    database='heroku_97e37ed6dee1412'
    )   
    
    conn.ping(reconnect=True)

    received_message = event.message.text
    search_word = Morphological_analysis.morphological_analysis(received_message)
    received_message = received_message.split(":")
    print(received_message)

    cur = conn.cursor()

    
    try:
        cur.execute("select content from 経営用語辞典 where word = %s",(search_word,))
        a = cur.fetchone()
        message = TextSendMessage(
        text=a[0])
    except mysql.connector.errors.ProgrammingError:
        error_message = TextSendMessage(
        text="私にはわかりません。別の質問なら何とか答えられるかもしれません。")
        line_bot_api.reply_message(
        event.reply_token,
        [error_message])

    except mysql.connector.errors.InternalError:
        error_message = TextSendMessage(
        text="私にはわかりません。別の質問なら何とか答えられるかもしれません。")
        line_bot_api.reply_message(
        event.reply_token,
        [error_message])
    except UnboundLocalError:
        error_message = TextSendMessage(
        text="私にはわかりません。別の質問なら何とか答えられるかもしれません。")
        line_bot_api.reply_message(
        event.reply_token,
        [error_message])
    except TypeError:
        error_message = TextSendMessage(
        text="私にはわかりません。別の質問なら何とか答えられるかもしれません。")
        line_bot_api.reply_message(
        event.reply_token,
        [error_message])
    except TypeError:
        error_message = TextSendMessage(
        text="私にはわかりません。別の質問なら何とか答えられるかもしれません。")
        line_bot_api.reply_message(
        event.reply_token,
        [error_message])
        a = cur.fetchone()
        message = TextSendMessage(
        text=a[0])


    try:
        cur.execute("select title,content from {0}".format(search_word))
    except mysql.connector.errors.ProgrammingError:
        error_message = TextSendMessage(
        text="私にはわかりません。別の質問なら何とか答えられるかもしれません。")
        line_bot_api.reply_message(
        event.reply_token,
        [message])
    except mysql.connector.errors.InternalError:
        error_message = TextSendMessage(
        text="私にはわかりません。別の質問なら何とか答えられるかもしれません。")
        line_bot_api.reply_message(
        event.reply_token,
        [message])
    except UnboundLocalError:
        error_message = TextSendMessage(
        text="私にはわかりません。別の質問なら何とか答えられるかもしれません。")
        line_bot_api.reply_message(
        event.reply_token,
        [message])
    except TypeError:
        error_message = TextSendMessage(
        text="私にはわかりません。別の質問なら何とか答えられるかもしれません。")
        line_bot_api.reply_message(
        event.reply_token,
        [message])
    else:
    
        line_bot_api.reply_message(
        event.reply_token,
        [message])

        cur.close()
        conn.close()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)