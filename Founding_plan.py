import mysql.connector

from linebot.models import(
  TextSendMessage,TemplateSendMessage,PostbackAction,ButtonsTemplate,ImageSendMessage
)

class Founding_plan:   
  def founding_plan_suggest():
    reply_message = []
    reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label="創業の動機",
                        data="創業計画書サポート_提案_提案創業動機"
                    ),
                    PostbackAction(
                        label="経営者の略歴等",
                        data="創業計画書サポート_提案_提案経歴"
                    ),
                    PostbackAction(
                        label="取扱商品・サービス",
                        data="創業計画書サポート_提案_提案商品"
                    ),
                    PostbackAction(
                        label="取引先・取引先関係等",
                        data="創業計画書サポート_提案_提案取引先"
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
                    label="従業員",
                    data="創業計画書サポート_提案_提案従業員"
                ),
                PostbackAction(
                    label="お借入の状況",
                    data="創業計画書サポート_提案_提案借入状況"
                ),
                PostbackAction(
                    label="必要な資金と調達方法",
                    data="創業計画書サポート_提案_提案資金内訳"
                ),
                PostbackAction(
                    label="事業の見通し",
                    data="創業計画書サポート_提案_提案事業の見通し"
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
                    label="自由記述欄",
                    data="創業計画書サポート_提案_提案自由記述欄"
                ),
                PostbackAction(
                    label="補足説明資料",
                    data="創業計画書サポート_提案_提案補足説明"
                )
            ]
        )
        ))

    return reply_message
    
  def founding_plan_good_bad(discrimination):
    reply_message = []
    reply_message.append(TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        text='選択肢をタップしてください',
        actions=[
            PostbackAction(
                label="創業の動機",
                data=f"創業計画書サポート_具体例_{discrimination}具体例各項目解説_{discrimination}創業動機"
            ),
            PostbackAction(
                label="経営者の略歴等",
                data=f"創業計画書サポート_具体例_{discrimination}具体例各項目解説_{discrimination}経歴"
            ),
            PostbackAction(
                label="取扱商品・サービス",
                data=f"創業計画書サポート_具体例_{discrimination}具体例各項目解説_{discrimination}商品"
            ),
            PostbackAction(
                label="取引先・取引先関係等",
                data=f"創業計画書サポート_具体例_{discrimination}具体例各項目解説_{discrimination}取引先"
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
                label="従業員",
                data=f"創業計画書サポート_具体例_{discrimination}具体例各項目解説_{discrimination}従業員"
            ),
            PostbackAction(
                label="お借入の状況",
                data=f"創業計画書サポート_具体例_{discrimination}具体例各項目解説_{discrimination}借入状況"
            ),
            PostbackAction(
                label="必要な資金と調達方法",
                data=f"創業計画書サポート_具体例_{discrimination}具体例各項目解説_{discrimination}資金内訳"
            ),
            PostbackAction(
                label="事業の見通し",
                data=f"創業計画書サポート_具体例_{discrimination}具体例各項目解説_{discrimination}事業の見通し"
            )
        ]
    )
))
    if discrimination == "良い":
        reply_message.append(TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            text='選択肢をタップしてください',
            actions=[
                PostbackAction(
                    label="自由記述欄",
                    data=f"創業計画書サポート_具体例_{discrimination}具体例各項目解説_{discrimination}自由記述欄"
                ),
                PostbackAction(
                    label="補足説明書",
                    data=f"創業計画書サポート_具体例_{discrimination}具体例各項目解説_補足説明書"
                )
            ]
        )
    ))

    elif discrimination == "悪い":
        reply_message.append(TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            text='選択肢をタップしてください',
            actions=[
                PostbackAction(
                    label="自由記述欄",
                    data=f"創業計画書サポート_具体例_{discrimination}具体例各項目解説_{discrimination}自由記述欄"
                )
            ]
        )
    ))

    return reply_message

  @classmethod
  def founding_plan_handle(self,receive_message):
 
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

    if receive_message[0] == "創業計画書サポートシステム起動":
        reply_message.append(TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            text='選択肢をタップしてください',
            actions=[
                PostbackAction(
                    label="創業計画書の解説",
                    data="創業計画書サポート_解説"
                ),
                PostbackAction(
                    label="創業計画書の具体例",
                    data="創業計画書サポート_具体例"
                ),
                PostbackAction(
                    label="創業計画書の提案を受ける",
                    data="創業計画書サポート_提案"
                ),
                PostbackAction(
                    label="創業計画書の提出前確認",
                    data="創業計画書サポート_提出前確認"
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
  def founding_plan_postback(self,postback_data):

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

    if postback_datum[0] == "創業計画書サポート":
      if postback_datum[1] == "解説":
       if len(postback_datum) == 2:
        reply_message.append(TemplateSendMessage(
              alt_text='Buttons template',
              template=ButtonsTemplate(
                  text='選択肢をタップしてください',
                  actions=[
                      PostbackAction(
                          label="創業計画書を作成する理由",
                          data="創業計画書サポート_解説_作成理由"
                      ),
                      PostbackAction(
                          label="創業計画書の作成時期",
                          data="創業計画書サポート_解説_作成時期"
                      ),
                      PostbackAction(
                          label="創業計画書の添付書類",
                          data="創業計画書サポート_解説_添付書類"
                      ),
                      PostbackAction(
                          label="事業計画書との違い",
                          data="創業計画書サポート_解説_違い"
                      )
                  ]
              )
          ))

       elif len(postback_datum) == 3:
          cur.execute("select content from 創業計画書サポート where title = %s",(postback_datum[2],))
          res = cur.fetchone()
          reply_message.append(TextSendMessage(text=res[0]))
        

      elif postback_datum[1] == "具体例":
        if len(postback_datum) == 2:
          reply_message.append(TemplateSendMessage(
              alt_text='Buttons template',
              template=ButtonsTemplate(
                  text='選択肢をタップしてください',
                  actions=[
                      PostbackAction(
                          label="具体例の画像と情報を確認",
                          data="創業計画書サポート_具体例_画像と情報確認"
                      ),
                      PostbackAction(
                          label="具体例全体のポイント",
                          data="創業計画書サポート_具体例_具体例全体のポイント"
                      ),
                      PostbackAction(
                          label="良い具体例各項目の解説",
                          data="創業計画書サポート_具体例_良い具体例各項目解説"
                      ),
                      PostbackAction(
                          label="悪い具体例各項目の解説",
                          data="創業計画書サポート_具体例_悪い具体例各項目解説"
                      ),
                  ]
              )
          ))

        elif len(postback_datum) == 3:
          if postback_datum[2] == "画像と情報確認":
            rows = ["良い創業計画書", "良い補足説明",  "悪い創業計画書"]
            for row in rows:
                cur.execute("select content from 創業計画書サポート画像 where title = %s",(row,))
                res = cur.fetchone()
                reply_message.append(ImageSendMessage(
                original_content_url= res[0],
                preview_image_url= res[0]
                ))

            cur.execute("select content from 創業計画書サポート where title = %s",(postback_datum[1],))
            res = cur.fetchone()
            reply_message.append(TextSendMessage(text=res[0]))
            
            reply_message.append(TemplateSendMessage(
              alt_text='Buttons template',
              template=ButtonsTemplate(
                  text='選択肢をタップしてください',
                  actions=[
                      PostbackAction(
                          label="具体例全体のポイント",
                          data="創業計画書サポート_具体例_具体例全体のポイント"
                      ),
                      PostbackAction(
                          label="良い具体例各項目の解説",
                          data="創業計画書サポート_具体例_良い具体例各項目解説"
                      ),
                      PostbackAction(
                          label="悪い具体例各項目の解説",
                          data="創業計画書サポート_具体例_悪い具体例各項目解説"
                      ),
                  ]
              )
          ))
          

          elif postback_datum[2] == "具体例全体のポイント":
            cur.execute("select content from 創業計画書サポート画像 where title = %s",("良い創業計画書",))
            res = cur.fetchone()
            reply_message.append(ImageSendMessage(
            original_content_url= res[0],
            preview_image_url= res[0]
            ))
            
            cur.execute("select content from 創業計画書サポート where title = %s",("全体のポイント",))
            res = cur.fetchone()
            reply_message.append(TextSendMessage(text=res[0]))

            reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="良い具体例各項目の解説",
                            data="創業計画書サポート_具体例_良い具体例各項目解説"
                        ),
                        PostbackAction(
                            label="悪い具体例各項目の解説",
                            data="創業計画書サポート_具体例_悪い具体例各項目解説"
                        ),
                    ]
                )
            ))

          elif postback_datum[2] == "良い具体例各項目解説":
            image_url = "https://egaoknk.com/wp-content/uploads/2021/08/good_founding_plam.png"
            reply_message.append(ImageSendMessage(
            original_content_url= image_url,
            preview_image_url= image_url
            ))
            cur.execute("select content from 創業計画書サポート where title = %s",(postback_datum[2],))
            res = cur.fetchone()
            reply_message.append(TextSendMessage(text=res[0]))
            discrimination = "良い"
            def_reply_messages = Founding_plan.founding_plan_good_bad(discrimination)
            for def_reply_message in def_reply_messages:
                reply_message.append(def_reply_message)
        
          elif postback_datum[2] == "悪い具体例各項目解説":
            image_url = "https://egaoknk.com/wp-content/uploads/2021/08/bad_founding_plan.png"
            reply_message.append(ImageSendMessage(
            original_content_url= image_url,
            preview_image_url= image_url
            ))
            cur.execute("select content from 創業計画書サポート where title = %s",(postback_datum[2],))
            res = cur.fetchone()
            reply_message.append(TextSendMessage(text=res[0])) 
            discrimination = "悪い"      
            def_reply_messages = Founding_plan.founding_plan_good_bad(discrimination)
            for def_reply_message in def_reply_messages:
                reply_message.append(def_reply_message)
          
        elif len(postback_datum) == 4:
            if ("良い" in postback_datum[3]) == True:
                cur.execute("select content from 創業計画書サポート画像 where title = %s",(postback_datum[3],))
                res = cur.fetchone()
                reply_message.append(ImageSendMessage(
                original_content_url= res[0],
                preview_image_url= res[0]
                ))
                cur.execute("select content from 創業計画書サポート where title = %s",(postback_datum[3],))
                res = cur.fetchone()
                reply_message.append(TextSendMessage(text=res[0]))

                discrimination = "良い"
                def_reply_messages = Founding_plan.founding_plan_good_bad(discrimination)
                for def_reply_message in def_reply_messages:
                    reply_message.append(def_reply_message)


            elif ("悪い" in postback_datum[3]) == True:
                cur.execute("select content from 創業計画書サポート画像 where title = %s",(postback_datum[3],))
                res = cur.fetchone()
                reply_message.append(ImageSendMessage(
                original_content_url= res[0],
                preview_image_url= res[0]
                ))
                cur.execute("select content from 創業計画書サポート where title = %s",(postback_datum[3],))
                res = cur.fetchone()
                reply_message.append(TextSendMessage(text=res[0]))
                discrimination = "悪い"      
                def_reply_messages = Founding_plan.founding_plan_good_bad(discrimination)
                for def_reply_message in def_reply_messages:
                    reply_message.append(def_reply_message)

          
      elif postback_datum[1] == "提案":
        if len(postback_datum) == 2:
            reply_message = Founding_plan.founding_plan_suggest()

        elif len(postback_datum) == 3:
            cur.execute("select content from 創業計画書サポート where title = %s",(postback_datum[2],))
            res = cur.fetchone()
            reply_message.append(TextSendMessage(text=res[0]))
            rows = Founding_plan.founding_plan_suggest()
            for row in rows:
                reply_message.append(row)

        
        
      
      elif postback_datum[1] == "提出前確認": 
          if len(postback_datum) == 2:
            reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label="創業計画書全体の確認",
                        data="創業計画書サポート_提出前確認_創業計画書全体の確認"
                    ),
                    PostbackAction(
                        label="創業計画書9項目の確認",
                        data="創業計画書サポート_提出前確認_創業計画書9項目の確認"
                    ),
                    PostbackAction(
                        label="添付書類の確認",
                        data="創業計画書サポート_提出前確認_添付書類の確認"
                    )
                ]
            )
            ))

          elif len(postback_datum) == 3:
            if postback_datum[2] == "創業計画書全体の確認":
                cur.execute("select content from 創業計画書サポート where title = %s",(postback_datum[2],))
                res = cur.fetchone()
                reply_message.append(TextSendMessage(text=res[0]))

                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='創業計画書9項目の確認はされますか？',
                    actions=[
                        PostbackAction(
                            label="はい",
                            data="創業計画書サポート_提出前確認_創業計画書9項目の確認"
                        ),
                        PostbackAction(
                            label="いいえ",
                            data="創業計画書サポート_提出前確認_いいえ"
                        )
                    ]
                )
                ))


            elif postback_datum[2] == "創業計画書9項目の確認":
                cur.execute("select content from 創業計画書サポート where title = %s",(postback_datum[2],))
                res = cur.fetchone()
                reply_message.append(TextSendMessage(text=res[0]))

                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='添付書類の確認はされますか？',
                    actions=[
                        PostbackAction(
                            label="はい",
                            data="創業計画書サポート_提出前確認_添付書類の確認"
                        ),
                        PostbackAction(
                            label="いいえ",
                            data="創業計画書サポート_提出前確認_いいえ"
                        )
                    ]
                )
                ))




            elif postback_datum[2] == "添付書類の確認":
                cur.execute("select content from 創業計画書サポート where title = %s",(postback_datum[2],))
                res = cur.fetchone()
                reply_message.append(TextSendMessage(text=res[0]))
    
            elif postback_datum[2] == "いいえ":
                reply_message.append(TextSendMessage(text="わかりました。何かあれば声を掛けてください。"))

        
    


            

    cur.close()
    conn.close()
    try:
      return reply_message
    except UnboundLocalError:
      return None