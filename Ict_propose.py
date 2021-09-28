import mysql.connector

from linebot.models import(
TextSendMessage,TemplateSendMessage,PostbackAction,ButtonsTemplate
)

class Ict_propose:
  @classmethod
  def ict_propose_handle(self,receive_message):
    
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


    if receive_message[0] == "ICT提案システム起動":
        reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label="経営にICTを導入する意味",
                        data="ICT提案システム_意味"
                    ),
                    PostbackAction(
                        label="ICTの提案を受ける",
                        data="ICT提案システム_受ける"
                    ),
                    PostbackAction(
                        label="ICTの一覧を確認",
                        data="ICT提案システム_ICT一覧確認"
                    )
                ]
            )
        ))

    elif ("ICT提案一覧" in receive_message[0]) == True:
        try:
            receive_message = receive_message[0].split(":")    
            title = receive_message[1]
            cur.execute("SELECT content FROM ICTサービス一覧 WHERE title = %s ",(title,))
            row= cur.fetchone()
            if row == None:
                cur.execute("SELECT content FROM ICT機器一覧 WHERE title = %s ",(title,))
                row= cur.fetchone()            
            ict = (f"「{title}」\n\n{row[0]}")
            reply_message.append(TextSendMessage(text=ict))
        except:
            reply_message.append(TextSendMessage(text="入力頂いたメッセージに間違いがあるため処理できません。\n「()」「:」文字が半角になっているか、余分な余白が入っているか、入力した内容が登録されているか等の確認をお願いします。"))

    try:
        return reply_message
    except UnboundLocalError:
        return None



  @classmethod
  def ict_propose_postback(self,postback_data):
    
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

    if postback_datum[0] == "ICT提案システム":
      if postback_datum[1] == "意味":
        cur.execute("select content from 経営用語辞典 where id = %s",(9,))
        res = cur.fetchone()
        reply_message.append(TextSendMessage(text=res[0]))


      
      elif postback_datum[1] == "受ける":
        if len(postback_datum) == 2:
          cur.execute("select content from ICT提案システム where id = %s",(1,))
          res = cur.fetchone()
          reply_message.append(TextSendMessage(text=res[0]))
          reply_message.append(TemplateSendMessage(
              alt_text='Buttons template',
              template=ButtonsTemplate(
                  text='業種を選択してください',
                  actions=[
                      PostbackAction(
                          label="飲食",
                          data="ICT提案システム_受ける_飲食"
                      ),
                      PostbackAction(
                          label="理容・美容",
                          data="ICT提案システム_受ける_理容美容"
                      ),
                      PostbackAction(
                          label="小売",
                          data="ICT提案システム_受ける_小売"
                      ),
                      PostbackAction(
                          label="情報通信",
                          data="ICT提案システム_受ける_情報通信"
                      )
                  
                  ]
              )
          ))

          reply_message.append(TemplateSendMessage(
              alt_text='Buttons template',
              template=ButtonsTemplate(
                  text='業種を選択してください',
                  actions=[
                      PostbackAction(
                          label="宿泊",
                          data="ICT提案システム_受ける_宿泊"
                      ),
                      PostbackAction(
                          label="不動産",
                          data="ICT提案システム_受ける_不動産"
                      ),
                      PostbackAction(
                          label="金融・保険",
                          data="ICT提案システム_受ける_金融保険"
                      ),
                      PostbackAction(
                          label="医療・福祉",
                          data="ICT提案システム_受ける_医療福祉"
                      )
                  
                  ]
              )
          ))

          reply_message.append(TemplateSendMessage(
              alt_text='Buttons template',
              template=ButtonsTemplate(
                  text='業種を選択してください',
                  actions=[
                      PostbackAction(
                          label="教育",
                          data="ICT提案システム_受ける_教育"
                      ),
                      PostbackAction(
                          label="建設",
                          data="ICT提案システム_受ける_建設"
                      ),
                      PostbackAction(
                          label="運輸",
                          data="ICT提案システム_受ける_運輸"
                      )
                  
                  ]
              )
          ))
        elif len(postback_datum) == 3:

          search_word = postback_datum[2]
          cur.execute("select content from ICT提案システム一覧 where title = %s",(search_word,))
          res = cur.fetchone()

          reply_message.append(TemplateSendMessage(
              alt_text='Buttons template',
              template=ButtonsTemplate(
                  text='あなた以外に従業員はいますか？',
                  actions=[
                      PostbackAction(
                          label="はい",
                          data=(f"ICT提案システム_受ける_{search_word}_従業員有り_{res[0]}")
                      ),
                      PostbackAction(
                          label="いいえ",
                          data=(f"ICT提案システム_受ける_{search_word}_従業員無し_{res[0]}")
                      )
                  ]
              )
          ))

        elif len(postback_datum) == 5:

          a = postback_datum[2]
          search_word = postback_datum[3]
          ict = postback_datum[4]

          if postback_datum[3] == "従業員有り":
            cur.execute("select content from ICT提案システム一覧 where title = %s",(search_word,))
            res = cur.fetchone()
            res_addition = f"{ict}/{res[0]}"

          elif postback_datum[3] == "従業員無し":
            res_addition = ict


          reply_message.append(TemplateSendMessage(
              alt_text='Buttons template',
              template=ButtonsTemplate(
                  text='テレワークを導入しますか？',
                  actions=[
                      PostbackAction(
                          label="はい",
                          data=(f"ICT提案システム_受ける_{a}_{search_word}_テレワーク有り_{res_addition}")
                      ),
                      PostbackAction(
                          label="いいえ",
                          data=(f"ICT提案システム_受ける_{a}_{search_word}_テレワーク無し_{res_addition}")
                      )
                  ]
              )
          ))
      
        elif len(postback_datum) == 6:

          a = postback_datum[2]
          b = postback_datum[3]
          search_word = postback_datum[4]
          ict = postback_datum[5]


          if postback_datum[4] == "テレワーク有り":
            cur.execute("select content from ICT提案システム一覧 where title = %s",(search_word,))
            res = cur.fetchone()
            res_addition = f"{ict}/{res[0]}"

          elif postback_datum[4] == "テレワーク無し":
            res_addition = ict

          reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='販売する商品はありますか？',
                actions=[
                    PostbackAction(
                        label="はい",
                        data=(f"ICT提案システム_受ける_{a}_{b}_{search_word}_商品有り_{res_addition}")
                    ),
                    PostbackAction(
                        label="いいえ",
                        data=(f"ICT提案システム_受ける_{a}_{b}_{search_word}_商品無し_{res_addition}")
                    )
                ]
            )
        ))
        

      
        elif len(postback_datum) == 7:

          a = postback_datum[2]
          b = postback_datum[3]
          c = postback_datum[4]
          search_word = postback_datum[5]
          ict = postback_datum[6]
          

          if postback_datum[5] == "商品有り":
            cur.execute("select content from ICT提案システム一覧 where title = %s",(search_word,))
            res = cur.fetchone()
            res_addition = f"{ict}/{res[0]}"

          elif postback_datum[5] == "商品無し":
            res_addition = ict

          reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='店舗で商品を販売しますか？',
                    actions=[
                        PostbackAction(
                            label="はい",
                            data=(f"ICT提案システム_受ける_{a}_{b}_{c}_{search_word}_店舗販売有り_{res_addition}")
                        ),
                        PostbackAction(
                            label="いいえ",
                            data=(f"ICT提案システム_受ける_{a}_{b}_{c}_{search_word}_店舗販売無し_{res_addition}")
                        )
                    ]
                )
            ))
      
        elif len(postback_datum) == 8:

          search_word = postback_datum[6]
          ict = postback_datum[7]

          if postback_datum[6] == "店舗販売有り":
            cur.execute("select content from ICT提案システム一覧 where title = %s",(search_word,))
            res = cur.fetchone()
            res_addition = f"{ict}/{res[0]}"

          elif postback_datum[6] == "店舗販売無し":
            res_addition = ict

          cur.execute("select content from ICT提案システム一覧 where title = %s",("全業種",))
          res = cur.fetchone()
          ict = (f"{res[0]}/{res_addition}")

          ds = []
          es = []
          ds_ict_systems = []
          es_ict_devices = []
          a = ict
          bs = a.split("/")
          for b in bs:
              if "\n\n" in b:
                  c = b.split("\n\n")
                  ds.append(c[0])
                  es.append(c[1])
                
              else:
                  ds.append(b)
          for d in ds:
              ds_ict_systems.append(d.split("\n"))
          for e in es:
              es_ict_devices.append(e.split("\n"))

          ict_system_detail = "~ICTシステム~\n\n"
          for ds_ict_system in ds_ict_systems:
              for ict_system in ds_ict_system:
                  if not(ict_system == ""):
                      c = (f"・{ict_system}\n")
                      ict_system_detail += c
                    
          ict_device_detail = "\n~ICT機器~\n\n"
          for es_ict_device in es_ict_devices:
              for ict_device in es_ict_device:
                  if not(ict_device == ""):
                      c = (f"・{ict_device}\n")
                      ict_device_detail += c
                    
          ict_system_detail += ict_device_detail

          reply_message.append(TextSendMessage(text=f"{ict_system_detail}\nこちらがあなたの条件にあったICTの一覧です。"))

          
          reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='提案したICTの詳細を確認しますか？',
                    actions=[
                        PostbackAction(
                            label="はい",
                            data=(f"ICT提案システム_詳細の説明を受ける_{ict}")
                        ),
                        PostbackAction(
                            label="いいえ",
                            data=(f"ありがとう")
                        )
                    ]
                )
            ))
        



      elif postback_datum[1] == "詳細の説明を受ける":
          ds = []
          es = []
          ds_ict_systems = []
          es_ict_devices = []
          a = postback_datum[2]
          bs = a.split("/")
          for b in bs:
              if "\n\n" in b:
                  c = b.split("\n\n")
                  ds.append(c[0])
                  es.append(c[1])
                
              else:
                  ds.append(b)
          for d in ds:
              ds_ict_systems.append(d.split("\n"))
          for e in es:
              es_ict_devices.append(e.split("\n"))

          ict_system_detail = "~ICTシステム~\n\n"

          for ds_ict_system in ds_ict_systems:
              for ict_system in ds_ict_system:
                  if not(ict_system == ""):
                      cur.execute("select content from ICTサービス一覧 where title = %s",(ict_system,))
                      b = cur.fetchone()
                      c = (f"・{ict_system}\n\n{b[0]}\n\n")
                      ict_system_detail += c

          ict_device_detail = "\n~ICT機器~\n\n"
          for es_ict_device in es_ict_devices:
              for ict_device in es_ict_device:
                  if not(ict_device == ""):
                      cur.execute("select content from ICT機器一覧 where title = %s",(ict_device,))
                      b = cur.fetchone()
                      c = (f"・{ict_device}\n\n{b[0]}\n\n")
                      ict_device_detail += c
            
          ict_detail = ict_system_detail + ict_device_detail

          if len(ict_detail) <= 5000:
             reply_message.append(TextSendMessage(text=f"{ict_detail}こちらがあなたの条件にあったICTの詳細です。"))
        
          elif len(ict_detail) >= 5001:
              reply_message.append(TextSendMessage(text=f"{ict_system_detail}こちらがあなたの条件にあったICTサービスです。"))
              reply_message.append(TextSendMessage(text=f"{ict_device_detail}こちらがあなたの条件にあったICT機器です。"))
              

      


      elif postback_datum[1] == "ICT一覧確認":
        if len(postback_datum) == 2:
            reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="業種別のICTを確認",
                            data="ICT提案システム_ICT一覧確認_業種別ICT確認"
                        ),
                        PostbackAction(
                            label="お悩み別のICTを確認",
                            data="ICT提案システム_ICT一覧確認_お悩み別ICT確認"
                        ),
                        PostbackAction(
                            label="ICTの一覧表を確認",
                            data="ICT提案システム_ICT一覧確認_ICT一覧表確認"
                        )
                    ]
                )
            ))

        elif postback_datum[2] == "業種別ICT確認":
            if len(postback_datum) == 3:
                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='選択肢をタップしてください',
                    actions=[
                        PostbackAction(
                            label="飲食",
                            data="ICT提案システム_ICT一覧確認_業種別ICT確認_飲食"
                        ),
                        PostbackAction(
                            label="理容美容",
                            data="ICT提案システム_ICT一覧確認_業種別ICT確認_理容美容"
                        ),
                        PostbackAction(
                            label="小売",
                            data="ICT提案システム_ICT一覧確認_業種別ICT確認_小売"
                        ),
                        PostbackAction(
                            label="情報通信",
                            data="ICT提案システム_ICT一覧確認_業種別ICT確認_情報通信"
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
                            label="宿泊",
                            data="ICT提案システム_ICT一覧確認_業種別ICT確認_宿泊"
                        ),
                        PostbackAction(
                            label="理容美容",
                            data="ICT提案システム_ICT一覧確認_業種別ICT確認_不動産"
                        ),
                        PostbackAction(
                            label="金融保険",
                            data="ICT提案システム_ICT一覧確認_業種別ICT確認_金融保険"
                        ),
                        PostbackAction(
                            label="医療福祉",
                            data="ICT提案システム_ICT一覧確認_業種別ICT確認_医療福祉"
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
                            label="教育",
                            data="ICT提案システム_ICT一覧確認_業種別ICT確認_教育"
                        ),
                        PostbackAction(
                            label="建設",
                            data="ICT提案システム_ICT一覧確認_業種別ICT確認_建設"
                        ),
                        PostbackAction(
                            label="運輸",
                            data="ICT提案システム_ICT一覧確認_業種別ICT確認_運輸"
                        ),
                        PostbackAction(
                            label="全業種",
                            data="ICT提案システム_ICT一覧確認_業種別ICT確認_全業種"
                        )
                    ]
                )
            ))

            elif len(postback_datum) == 4:
                ds = []
                es = []
                ict_systems = "特にありません。\n"
                ict_devices = "特にありません。\n"
                search_word = postback_datum[3]
                cur.execute("select content from ICT提案システム一覧 where title = %s",(search_word,))
                res = cur.fetchone()
                bs = res[0]
                if "\n\n" in bs:
                    c = bs.split("\n\n")
                    ds.append(c[0])
                    es.append(c[1])
                    for e in es:
                        ict_devices = e.split("\n")      
                else:
                    ict_systems = bs.split("\n")

                for d in ds:
                    ict_systems = d.split("\n")

                ict_system_detail = "~ICTシステム~\n\n"
                for ict_system in ict_systems:
                    if not (ict_system == ""):
                        c = (f"・{ict_system}\n")
                        ict_system_detail += c
                    ict_device_detail = "\n~ICT機器~\n\n"

                if (ict_devices == "特にありません。\n"):
                    ict_device_detail += ict_devices
                else:
                    for ict_device in ict_devices:
                        if not (ict_device == ""):
                            c = (f"・{ict_device}\n")
                            ict_device_detail += c

                if postback_datum[3] == "全業種":
                    ict_device_detail += (f"\n全業種共通で上記を準備されることをおすすめします。")
                    ict_system_detail += ict_device_detail
               
                else:
                    ict_device_detail += (f"\n{postback_datum[3]}業を経営される方は上記を準備されることをおすすめします。")
                    ict_system_detail += ict_device_detail
                
                reply_message.append(TextSendMessage(text=ict_system_detail))

                reply_message.append(TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    text='それぞれのICTの詳細を確認しますか？',
                    actions=[
                        PostbackAction(
                            label="はい",
                            data=(f"ICT提案システム_詳細の説明を受ける_{bs}")
                        ),
                        PostbackAction(
                            label="いいえ",
                            data=(f"ありがとう")
                        )
                    ]
                )
            ))

        elif postback_datum[2] == "お悩み別ICT確認":
            if len(postback_datum) == 3:
                reply_message.append(TemplateSendMessage(
                        alt_text='Buttons template',
                        template=ButtonsTemplate(
                            text='選択肢をタップしてください',
                            actions=[
                                PostbackAction(
                                    label="慣れない従業員管理が大変",
                                    data="ICT提案システム_ICT一覧確認_お悩み別ICT確認_慣れない従業員管理ができない"
                                ),
                                PostbackAction(
                                    label="多忙で商品管理ができない",
                                    data="ICT提案システム_ICT一覧確認_お悩み別ICT確認_多忙で商品管理ができない"
                                ),
                                PostbackAction(
                                    label="商品の販売先が少ない",
                                    data="ICT提案システム_ICT一覧確認_お悩み別ICT確認_商品の販売先が少ない"
                                ),
                                PostbackAction(
                                    label="店舗運営を効率化したい",
                                    data="ICT提案システム_ICT一覧確認_お悩み別ICT確認_店舗運営を効率化したい"
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
                                    label="早急にコロナ対応をしたい",
                                    data="ICT提案システム_ICT一覧確認_お悩み別ICT確認_早急にコロナ対応をしたい"
                                ),

                                PostbackAction(
                                    label="必要なICTがわからない",
                                    data="ICT提案システム_ICT一覧確認_お悩み別ICT確認_必要なICTがわからない"
                                )
                            ]
                        )
                    ))
            
            elif len(postback_datum) == 4:
                search_word = postback_datum[3]
                cur.execute("select content from ICT提案システム一覧 where title = %s", (search_word,))
                res = cur.fetchone()
                ict = res[0]
                bs = ict.split("/")            
                ds = []
                es = []
                ds_ict_systems = []
                es_ict_devices = []                
                for b in bs:
                    if "\n\n" in b:
                        c = b.split("\n\n")
                        ds.append(c[0])
                        es.append(c[1])
                        
                    else:
                        ds.append(b)
                for d in ds:
                    ds_ict_systems.append(d.split("\n"))
                for e in es:
                    es_ict_devices.append(e.split("\n"))

                ict_system_detail = "~ICTシステム~\n\n"

                for ds_ict_system in ds_ict_systems:
                    for ict_system in ds_ict_system:
                        if not(ict_system == ""):
                            cur.execute("select content from ICTサービス一覧 where title = %s",(ict_system,))
                            b = cur.fetchone()
                            c = (f"・{ict_system}\n\n{b[0]}\n\n")
                            ict_system_detail += c

                ict_device_detail = "\n~ICT機器~\n\n"
                if (es_ict_devices == []):
                    c = "ICT機器は特にありません。\n\n"
                    ict_device_detail += c
                else:
                    for es_ict_device in es_ict_devices:
                        for ict_device in es_ict_device:
                            if not(ict_device == ""):
                                cur.execute("select content from ICT機器一覧 where title = %s",(ict_device,))
                                b = cur.fetchone()
                                c = (f"・{ict_device}\n\n{b[0]}\n\n")
                                ict_device_detail += c
                    
                ict_detail = ict_system_detail + ict_device_detail

                if len(ict_detail) <= 5000:
                    reply_message.append(TextSendMessage(text=f"{ict_detail}「{search_word}」悩みを抱えた企業が導入するべきICTです。"))
                
                elif len(ict_detail) >= 5001:
                    reply_message.append(TextSendMessage(text=f"{ict_detail}「{search_word}」悩みを抱えた企業が導入するべきICTサービスです。"))
                    reply_message.append(TextSendMessage(text=f"{ict_detail}「{search_word}」悩みを抱えた企業が導入するべきICT機器です。"))
    

            
        elif postback_datum[2] == "ICT一覧表確認":
            ict_system_detail = "~ICTシステム一覧~\n\n"
            cur.execute("select title from ICTサービス一覧")
            ict_systems = cur.fetchall()
            for ict_system in ict_systems:
                c = (f"・{ict_system[0]}\n")
                ict_system_detail += c

            ict_device_detail = "\n~ICT機器一覧~\n\n"
            cur.execute("select title from ICT機器一覧")
            ict_devices = cur.fetchall()
            for ict_device in ict_devices:
                c = (f"・{ict_device[0]}\n")
                ict_device_detail += c
            ict_system_detail += ict_device_detail

            reply_message.append(TextSendMessage(text=ict_system_detail))
            reply_message.append(TextSendMessage(text=(f"各サービスや機器を詳しく知りたい方は\nICT提案一覧:サービス名or機器名\n上記の形式で入力してください。")))

  


    try:
      return reply_message 
    except UnboundLocalError:
      return None
