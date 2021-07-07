import math

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,TemplateSendMessage,ConfirmTemplate, PostbackAction,MessageAction,ButtonsTemplate
)

app = Flask(__name__)

line_bot_api = LineBotApi('2PxQlKQk9a7CypAYhi5kE5rlYaA09rjzOlMaWP1oHE2//uhfzpuWEuMeDl/Zfgm38quDlinjvxu1Q5Pl0VIHdVzDPgKNPGY5bMlWyUecO9M1X0Xu1zuypY698nRHChfudvD6LmzsnmmIyD5EoGZQOQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('dc66c011c03f32db0610150c1614b99f')


class Credit_management:
  @classmethod
  def credit_management(self,rows,event):
    if len(rows) == 1:
        message0 = TextSendMessage(
        text=(f"借入ID:{rows[0][0]}\n登録日時:{rows[0][1]}\n金融機関名:{rows[0][2]}\n借入金額:{math.floor(rows[0][3]/10000)}万円\n借入残額:{math.floor(rows[0][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[0][5])}円\n借入日:{rows[0][6]}\n借入期間:{rows[0][7]}年{rows[0][8]}ヶ月\n残存期間:{rows[0][9]}年{rows[0][10]}月\n返済日:{rows[0][11]}\n借入利率:{rows[0][12]}%") )
        
        line_bot_api.reply_message(
        event.reply_token,
        [message0])
    
    if len(rows) == 2:
        message0 = TextSendMessage(
        text=(f"借入ID:{rows[0][0]}\n登録日時:{rows[0][1]}\n金融機関名:{rows[0][2]}\n借入金額:{math.floor(rows[0][3]/10000)}万円\n借入残額:{math.floor(rows[0][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[0][5])}円\n借入日:{rows[0][6]}\n借入期間:{rows[0][7]}年{rows[0][8]}ヶ月\n残存期間:{rows[0][9]}年{rows[0][10]}月\n返済日:{rows[0][11]}\n借入利率:{rows[0][12]}%") )
        message1 = TextSendMessage(
        text=(f"借入ID:{rows[1][0]}\n登録日時:{rows[1][1]}\n金融機関名:{rows[1][2]}\n借入金額:{math.floor(rows[1][3]/10000)}万円\n借入残額:{math.floor(rows[1][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[1][5])}円\n借入日:{rows[1][6]}\n借入期間:{rows[1][7]}年{rows[1][8]}ヶ月\n残存期間:{rows[1][9]}年{rows[1][10]}月\n返済日:{rows[1][11]}\n借入利率:{rows[1][12]}%") )
        
        line_bot_api.reply_message(
        event.reply_token,
        [message0,message1])

    if len(rows) == 3:
        message0 = TextSendMessage(
        text=(f"借入ID:{rows[0][0]}\n登録日時:{rows[0][1]}\n金融機関名:{rows[0][2]}\n借入金額:{math.floor(rows[0][3]/10000)}万円\n借入残額:{math.floor(rows[0][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[0][5])}円\n借入日:{rows[0][6]}\n借入期間:{rows[0][7]}年{rows[0][8]}ヶ月\n残存期間:{rows[0][9]}年{rows[0][10]}月\n返済日:{rows[0][11]}\n借入利率:{rows[0][12]}%") )
        message1 = TextSendMessage(
        text=(f"借入ID:{rows[1][0]}\n登録日時:{rows[1][1]}\n金融機関名:{rows[1][2]}\n借入金額:{math.floor(rows[1][3]/10000)}万円\n借入残額:{math.floor(rows[1][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[1][5])}円\n借入日:{rows[1][6]}\n借入期間:{rows[1][7]}年{rows[1][8]}ヶ月\n残存期間:{rows[1][9]}年{rows[1][10]}月\n返済日:{rows[1][11]}\n借入利率:{rows[1][12]}%") )
        message2 = TextSendMessage(
        text=(f"借入ID:{rows[2][0]}\n登録日時:{rows[2][1]}\n金融機関名:{rows[2][2]}\n借入金額:{math.floor(rows[2][3]/10000)}万円\n借入残額:{math.floor(rows[2][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[2][5])}円\n借入日:{rows[2][6]}\n借入期間:{rows[2][7]}年{rows[2][8]}ヶ月\n残存期間:{rows[2][9]}年{rows[2][10]}月\n返済日:{rows[2][11]}\n借入利率:{rows[2][12]}%") )
        
        line_bot_api.reply_message(
        event.reply_token,
        [message0,message1,message2])

    if len(rows) == 4:
        message0 = TextSendMessage(
        text=(f"借入ID:{rows[0][0]}\n登録日時:{rows[0][1]}\n金融機関名:{rows[0][2]}\n借入金額:{math.floor(rows[0][3]/10000)}万円\n借入残額:{math.floor(rows[0][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[0][5])}円\n借入日:{rows[0][6]}\n借入期間:{rows[0][7]}年{rows[0][8]}ヶ月\n残存期間:{rows[0][9]}年{rows[0][10]}月\n返済日:{rows[0][11]}\n借入利率:{rows[0][12]}%") )
        message1 = TextSendMessage(
        text=(f"借入ID:{rows[1][0]}\n登録日時:{rows[1][1]}\n金融機関名:{rows[1][2]}\n借入金額:{math.floor(rows[1][3]/10000)}万円\n借入残額:{math.floor(rows[1][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[1][5])}円\n借入日:{rows[1][6]}\n借入期間:{rows[1][7]}年{rows[1][8]}ヶ月\n残存期間:{rows[1][9]}年{rows[1][10]}月\n返済日:{rows[1][11]}\n借入利率:{rows[1][12]}%") )
        message2 = TextSendMessage(
        text=(f"借入ID:{rows[2][0]}\n登録日時:{rows[2][1]}\n金融機関名:{rows[2][2]}\n借入金額:{math.floor(rows[2][3]/10000)}万円\n借入残額:{math.floor(rows[2][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[2][5])}円\n借入日:{rows[2][6]}\n借入期間:{rows[2][7]}年{rows[2][8]}ヶ月\n残存期間:{rows[2][9]}年{rows[2][10]}月\n返済日:{rows[2][11]}\n借入利率:{rows[2][12]}%") )
        message3 = TextSendMessage(
        text=(f"借入ID:{rows[3][0]}\n登録日時:{rows[3][1]}\n金融機関名:{rows[3][2]}\n借入金額:{math.floor(rows[3][3]/10000)}万円\n借入残額:{math.floor(rows[3][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[3][5])}円\n借入日:{rows[3][6]}\n借入期間:{rows[3][7]}年{rows[3][8]}ヶ月\n残存期間:{rows[3][9]}年{rows[3][10]}月\n返済日:{rows[3][11]}\n借入利率:{rows[3][12]}%") )
        
        line_bot_api.reply_message(
        event.reply_token,
        [message0,message1,message2,message3])

    if len(rows) == 5:
        message0 = TextSendMessage(
        text=(f"借入ID:{rows[0][0]}\n登録日時:{rows[0][1]}\n金融機関名:{rows[0][2]}\n借入金額:{math.floor(rows[0][3]/10000)}万円\n借入残額:{math.floor(rows[0][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[0][5])}円\n借入日:{rows[0][6]}\n借入期間:{rows[0][7]}年{rows[0][8]}ヶ月\n残存期間:{rows[0][9]}年{rows[0][10]}月\n返済日:{rows[0][11]}\n借入利率:{rows[0][12]}%") )
        message1 = TextSendMessage(
        text=(f"借入ID:{rows[1][0]}\n登録日時:{rows[1][1]}\n金融機関名:{rows[1][2]}\n借入金額:{math.floor(rows[1][3]/10000)}万円\n借入残額:{math.floor(rows[1][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[1][5])}円\n借入日:{rows[1][6]}\n借入期間:{rows[1][7]}年{rows[1][8]}ヶ月\n残存期間:{rows[1][9]}年{rows[1][10]}月\n返済日:{rows[1][11]}\n借入利率:{rows[1][12]}%") )
        message2 = TextSendMessage(
        text=(f"借入ID:{rows[2][0]}\n登録日時:{rows[2][1]}\n金融機関名:{rows[2][2]}\n借入金額:{math.floor(rows[2][3]/10000)}万円\n借入残額:{math.floor(rows[2][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[2][5])}円\n借入日:{rows[2][6]}\n借入期間:{rows[2][7]}年{rows[2][8]}ヶ月\n残存期間:{rows[2][9]}年{rows[2][10]}月\n返済日:{rows[2][11]}\n借入利率:{rows[2][12]}%") )
        message3 = TextSendMessage(
        text=(f"借入ID:{rows[3][0]}\n登録日時:{rows[3][1]}\n金融機関名:{rows[3][2]}\n借入金額:{math.floor(rows[3][3]/10000)}万円\n借入残額:{math.floor(rows[3][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[3][5])}円\n借入日:{rows[3][6]}\n借入期間:{rows[3][7]}年{rows[3][8]}ヶ月\n残存期間:{rows[3][9]}年{rows[3][10]}月\n返済日:{rows[3][11]}\n借入利率:{rows[3][12]}%") )
        message4 = TextSendMessage(
        text=(f"借入ID:{rows[4][0]}\n登録日時:{rows[4][1]}\n金融機関名:{rows[4][2]}\n借入金額:{math.floor(rows[4][3]/10000)}万円\n借入残額:{math.floor(rows[4][4]/10000)}万円 \n毎月の返済額:{math.floor(rows[4][5])}円\n借入日:{rows[4][6]}\n借入期間:{rows[4][7]}年{rows[4][8]}ヶ月\n残存期間:{rows[4][9]}年{rows[4][10]}月\n返済日:{rows[4][11]}\n借入利率:{rows[4][12]}%") )
        
        line_bot_api.reply_message(
        event.reply_token,
        [message0,message1,message2,message3,message4])