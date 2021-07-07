import random,glob

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
class First_Choice:
  @classmethod
  def first_choice(self,b):
    if len(b) == 4 :
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=b[0][0],
                        data=b[0][1]
                    ),
                    PostbackAction(
                        label=b[1][0],
                        data=b[1][1]
                    ),
                    PostbackAction(
                        label=b[2][0],
                        data=b[2][1]
                    ),
                    PostbackAction(
                        label=b[3][0],
                        data=b[3][1]
                    )
                ]
            )
        )

    elif len(b) == 3 :
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=b[0][0],
                        data=b[0][1]
                    ),
                    PostbackAction(
                        label=b[1][0],
                        data=b[1][1]
                    ),
                    PostbackAction(
                        label=b[2][0],
                        data=b[2][1]
                    ),

                ]
            )
        )

    elif len(b) == 2 :
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=b[0][0],
                        data=b[0][1]
                    ),
                    PostbackAction(
                        label=b[1][0],
                        data=b[1][1]
                    ),

                ]
            )
        )

    else:
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=b[0][0],
                        data=b[0][1]
                    ),

                ]
            )
        )
    return buttons_template_message

