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
  def first_choice(self,choices):
    reply_message = []
    if len(choices) == 1:
        reply_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=choices[0][0],
                        data=choices[0][1]
                    ),

                ]
            )
        )

    elif len(choices) == 2 :
        reply_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=choices[0][0],
                        data=choices[0][1]
                    ),
                    PostbackAction(
                        label=choices[1][0],
                        data=choices[1][1]
                    ),

                ]
            )
        )

    elif len(choices) == 3 :
        reply_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=choices[0][0],
                        data=choices[0][1]
                    ),
                    PostbackAction(
                        label=choices[1][0],
                        data=choices[1][1]
                    ),
                    PostbackAction(
                        label=choices[2][0],
                        data=choices[2][1]
                    ),

                ]
            )
        )

    elif len(choices) == 4 :
        reply_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=choices[0][0],
                        data=choices[0][1]
                    ),
                    PostbackAction(
                        label=choices[1][0],
                        data=choices[1][1]
                    ),
                    PostbackAction(
                        label=choices[2][0],
                        data=choices[2][1]
                    ),
                    PostbackAction(
                        label=choices[3][0],
                        data=choices[3][1]
                    )
                ]
            )
        )
    elif len(choices) == 5:
        reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=choices[0][0],
                        data=choices[0][1]
                    ),
                    PostbackAction(
                        label=choices[1][0],
                        data=choices[1][1]
                    ),
                    PostbackAction(
                        label=choices[2][0],
                        data=choices[2][1]
                    ),
                    PostbackAction(
                        label=choices[3][0],
                        data=choices[3][1]
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
                    label=choices[4][0],
                    data=choices[4][1]
                )
             ]
        )
        ))


    elif len(choices) == 6:
        reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=choices[0][0],
                        data=choices[0][1]
                    ),
                    PostbackAction(
                        label=choices[1][0],
                        data=choices[1][1]
                    ),
                    PostbackAction(
                        label=choices[2][0],
                        data=choices[2][1]
                    ),
                    PostbackAction(
                        label=choices[3][0],
                        data=choices[3][1]
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
                    label=choices[4][0],
                    data=choices[4][1]
                ),
                PostbackAction(
                    label=choices[5][0],
                    data=choices[4][1]
                )
             ]
        )
        ))

    elif len(choices) == 7 :
        reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=choices[0][0],
                        data=choices[0][1]
                    ),
                    PostbackAction(
                        label=choices[1][0],
                        data=choices[1][1]
                    ),
                    PostbackAction(
                        label=choices[2][0],
                        data=choices[2][1]
                    ),
                    PostbackAction(
                        label=choices[3][0],
                        data=choices[3][1]
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
                    label=choices[4][0],
                    data=choices[4][1]
                ),
                PostbackAction(
                    label=choices[5][0],
                    data=choices[5][1]
                ),
                PostbackAction(
                    label=choices[6][0],
                    data=choices[6][1]
                )
             ]
        )
        ))

    elif len(choices) == 8:
        reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=choices[0][0],
                        data=choices[0][1]
                    ),
                    PostbackAction(
                        label=choices[1][0],
                        data=choices[1][1]
                    ),
                    PostbackAction(
                        label=choices[2][0],
                        data=choices[2][1]
                    ),
                    PostbackAction(
                        label=choices[3][0],
                        data=choices[3][1]
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
                    label=choices[4][0],
                    data=choices[4][1]
                ),
                PostbackAction(
                    label=choices[5][0],
                    data=choices[5][1]
                ),
                PostbackAction(
                    label=choices[6][0],
                    data=choices[6][1]
                ),
                PostbackAction(
                    label=choices[7][0],
                    data=choices[7][1]
                )
             ]
        )
        ))
    elif len(choices) == 9:
        reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=choices[0][0],
                        data=choices[0][1]
                    ),
                    PostbackAction(
                        label=choices[1][0],
                        data=choices[1][1]
                    ),
                    PostbackAction(
                        label=choices[2][0],
                        data=choices[2][1]
                    ),
                    PostbackAction(
                        label=choices[3][0],
                        data=choices[3][1]
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
                    label=choices[4][0],
                    data=choices[4][1]
                ),
                PostbackAction(
                    label=choices[5][0],
                    data=choices[5][1]
                ),
                PostbackAction(
                    label=choices[6][0],
                    data=choices[6][1]
                ),
                PostbackAction(
                    label=choices[7][0],
                    data=choices[7][1]
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
                        label=choices[8][0],
                        data=choices[8][1]
                    )
                ]
            )
        ))

    elif len(choices) == 10:
        reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=choices[0][0],
                        data=choices[0][1]
                    ),
                    PostbackAction(
                        label=choices[1][0],
                        data=choices[1][1]
                    ),
                    PostbackAction(
                        label=choices[2][0],
                        data=choices[2][1]
                    ),
                    PostbackAction(
                        label=choices[3][0],
                        data=choices[3][1]
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
                    label=choices[4][0],
                    data=choices[4][1]
                ),
                PostbackAction(
                    label=choices[5][0],
                    data=choices[5][1]
                ),
                PostbackAction(
                    label=choices[6][0],
                    data=choices[6][1]
                ),
                PostbackAction(
                    label=choices[7][0],
                    data=choices[7][1]
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
                        label=choices[8][0],
                        data=choices[8][1]
                    ),
                    PostbackAction(
                        label=choices[9][0],
                        data=choices[9][1]
                    )
                ]
            )
        ))
    elif len(choices) == 11:
        reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=choices[0][0],
                        data=choices[0][1]
                    ),
                    PostbackAction(
                        label=choices[1][0],
                        data=choices[1][1]
                    ),
                    PostbackAction(
                        label=choices[2][0],
                        data=choices[2][1]
                    ),
                    PostbackAction(
                        label=choices[3][0],
                        data=choices[3][1]
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
                    label=choices[4][0],
                    data=choices[4][1]
                ),
                PostbackAction(
                    label=choices[5][0],
                    data=choices[5][1]
                ),
                PostbackAction(
                    label=choices[6][0],
                    data=choices[6][1]
                ),
                PostbackAction(
                    label=choices[7][0],
                    data=choices[7][1]
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
                        label=choices[8][0],
                        data=choices[8][1]
                    ),
                    PostbackAction(
                        label=choices[9][0],
                        data=choices[9][1]
                    ),
                    PostbackAction(
                        label=choices[10][0],
                        data=choices[10][1]
                    )
                ]
            )
        ))

    elif len(choices) == 12:
        reply_message.append(TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                text='選択肢をタップしてください',
                actions=[
                    PostbackAction(
                        label=choices[0][0],
                        data=choices[0][1]
                    ),
                    PostbackAction(
                        label=choices[1][0],
                        data=choices[1][1]
                    ),
                    PostbackAction(
                        label=choices[2][0],
                        data=choices[2][1]
                    ),
                    PostbackAction(
                        label=choices[3][0],
                        data=choices[3][1]
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
                    label=choices[4][0],
                    data=choices[4][1]
                ),
                PostbackAction(
                    label=choices[5][0],
                    data=choices[5][1]
                ),
                PostbackAction(
                    label=choices[6][0],
                    data=choices[6][1]
                ),
                PostbackAction(
                    label=choices[7][0],
                    data=choices[7][1]
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
                        label=choices[8][0],
                        data=choices[8][1]
                    ),
                    PostbackAction(
                        label=choices[9][0],
                        data=choices[9][1]
                    ),
                    PostbackAction(
                        label=choices[10][0],
                        data=choices[10][1]
                    ),
                    PostbackAction(
                        label=choices[11][0],
                        data=choices[11][1]
                    )
                ]
            )
        ))


    try:
        return reply_message 
    except UnboundLocalError:
        return None 