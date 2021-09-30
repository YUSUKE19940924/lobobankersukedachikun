import mysql.connector
from linebot.models import(
  TextSendMessage, ButtonsTemplate, TemplateSendMessage,PostbackAction,ImageSendMessage
)

class Instruction_manual:
  def function_explanation_branch():
    reply_message = []
    reply_message.append(TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            text='選択肢をタップしてください',
            actions=[
                PostbackAction(
                    label="債権管理機能",
                    data="取扱説明書_機能_債権管理"
                ),
                PostbackAction(
                    label="開業費管理機能",
                    data="取扱説明書_機能_開業費管理"
                ),
                PostbackAction(
                    label="起業フローチャート機能",
                    data="取扱説明書_機能_起業フローチャート"
                ),
                PostbackAction(
                    label="創業計画書サポート機能",
                    data="取扱説明書_機能_創業計画書サポート"
                )
            ]
        )
    ))

    reply_message.append(TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            text='選択肢をタップしてください',
            actions=[
                PostbackAction(
                    label="ICT提案機能",
                    data="取扱説明書_機能_ICT提案"
                )
            ]
        )
    ))

    return reply_message


  @classmethod
  def instruction_manual_handle(self,receive_message):

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

    if receive_message[0] == "取扱説明書起動":
        reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label="助太刀くんでできること",
                        data="取扱説明書_助太刀くん"
                    ),
                    PostbackAction(
                        label="基本の使い方",
                        data="取扱説明書_基本の使い方"
                    ),
                    PostbackAction(
                        label="5つの機能の使い方",
                        data="取扱説明書_機能"
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
  def instruction_manual_postback(self,postback_data):
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

    postback_datum = postback_data[0].split("_")

    if postback_datum[0] == "取扱説明書":
        if postback_datum[1] == "助太刀くん":
            search_word = postback_datum[1]
            cur.execute("select content from 取扱説明書 where title = %s",(search_word,))
            res_text = cur.fetchone()
            reply_message.append(TextSendMessage(text=res_text[0]))

        elif postback_datum[1] == "基本の使い方":
            search_word = postback_datum[1]
            cur.execute("select content from 取扱説明書画像 where title = %s",(search_word,))
            res_image = cur.fetchone()
            cur.execute("select content from 取扱説明書 where title = %s",(search_word,))
            res_text = cur.fetchone()
            reply_message.append(ImageSendMessage(
            original_content_url= res_image[0],
            preview_image_url= res_image[0]
            ))
            reply_message.append(TextSendMessage(text=res_text[0]))
            reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text="機能についての説明も確認されますか？",
                    actions=[
                        PostbackAction(
                            label="はい",
                            data="取扱説明書_機能"
                        ),
                        PostbackAction(
                            label="いいえ",
                            data="何もしない"
                        )
                    ]
                )
            ))


        elif postback_datum[1] == "機能":
          if len(postback_datum) == 2:
            cur.execute("select content from 取扱説明書 where title = %s",("5つの機能の説明",))
            res_text = cur.fetchone()
            reply_message.append(TextSendMessage(text=res_text[0]))
            reply_message = Instruction_manual.function_explanation_branch()

          elif len(postback_datum) == 3:
            if postback_datum[2] == "債権管理":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="借入内容の確認",
                            data="取扱説明書_機能_債権管理_借入内容の確認"
                        ),
                        PostbackAction(
                            label="借入内容の計算",
                            data="取扱説明書_機能_債権管理_借入内容の計算"
                        ),
                        PostbackAction(
                            label="借入内容の操作",
                            data="取扱説明書_機能_債権管理_借入内容の操作"
                        ),
                        PostbackAction(
                            label="説明一覧",
                            data="取扱説明書_機能_債権管理_債権管理機能の説明一覧"
                        )
                    ]
                )
                ))
            elif postback_datum[2] == "開業費管理":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="開業費の確認",
                            data="取扱説明書_機能_開業費管理_開業費の確認"
                        ),
                        PostbackAction(
                            label="開業費の計算",
                            data="取扱説明書_機能_開業費管理_開業費の計算"
                        ),
                        PostbackAction(
                            label="開業費の操作",
                            data="取扱説明書_機能_開業費管理_開業費の操作"
                        ),
                        PostbackAction(
                            label="説明一覧",
                            data="取扱説明書_機能_開業費管理_開業費管理機能の説明一覧"
                        )
                    ]
                )
                ))
            elif postback_datum[2] == "起業フローチャート":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="起業フローチャートを確認",
                            data="取扱説明書_機能_起業フローチャート_起業フローチャート確認"
                        ),
                        PostbackAction(
                            label="起業フローチャートを登録",
                            data="取扱説明書_機能_起業フローチャート_起業フローチャート登録"
                        ),
                        PostbackAction(
                            label="起業フローを詳しく学ぶ",
                            data="取扱説明書_機能_起業フローチャート_起業フローチャートを詳しく学ぶ"
                        ),
                        PostbackAction(
                            label="説明一覧",
                            data="取扱説明書_機能_起業フローチャート_起業フローチャート機能の説明一覧"
                        )
                    ]
                )
                ))
            elif postback_datum[2] == "創業計画書サポート":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="創業計画書の解説",
                            data="取扱説明書_機能_創業計画書サポート_創業計画書の解説"
                        ),
                        PostbackAction(
                            label="創業計画書の具体例",
                            data="取扱説明書_機能_創業計画書サポート_創業計画書の具体例"
                        ),
                        PostbackAction(
                            label="創業計画書の提案を受ける",
                            data="取扱説明書_機能_創業計画書サポート_創業計画書の提案"
                        ),
                        PostbackAction(
                            label="創業計画書の提出前確認",
                            data="取扱説明書_機能_創業計画書サポート_創業計画書の確認"
                        )
                    ]
                )
                ))
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="説明一覧",
                            data="取扱説明書_機能_創業計画書サポート_創業計画書サポート機能の説明一覧"
                        )
                    ]
                )
                ))

            elif postback_datum[2] == "ICT提案":
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="ICTの提案を受ける",
                            data="取扱説明書_機能_ICT提案_ICTの提案"
                        ),
                        PostbackAction(
                            label="ICTの一覧を確認",
                            data="取扱説明書_機能_ICT提案_ICTの一覧確認"
                        ),
                        PostbackAction(
                            label="説明一覧",
                            data="取扱説明書_機能_債権管理_ICT提案機能の説明一覧"
                        )
                    ]
                )
                ))

          elif len(postback_datum) == 4:
            if ("説明一覧" in  postback_datum[3]) == True:
                search_word = postback_datum[3]
                cur.execute("select content from 取扱説明書 where title = %s",(search_word,))
                res_text = cur.fetchone()
                reply_message.append(TextSendMessage(text=res_text[0]))
                def_reply_messages = Instruction_manual.function_explanation_branch()
                reply_message.append(def_reply_messages[0])
            else:
                search_word = postback_datum[3]
                cur.execute("select content from 取扱説明書画像 where title = %s",(search_word,))
                res_image = cur.fetchone()
                cur.execute("select content from 取扱説明書 where title = %s",(search_word,))
                res_text = cur.fetchone()
                reply_message.append(ImageSendMessage(
                original_content_url= res_image[0],
                preview_image_url= res_image[0]
                ))
                reply_message.append(TextSendMessage(text=res_text[0]))
                def_reply_messages = Instruction_manual.function_explanation_branch()
                reply_message.append(def_reply_messages[0])




    cur.close()
    conn.close()

    try:
      return reply_message
    except UnboundLocalError:
      return None