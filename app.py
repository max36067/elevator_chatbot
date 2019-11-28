
'''
啟動伺服器樣板
'''
from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
import json
import os 
import main_rich_menu as mrm
import time
from json_ import detect_json

f = os.getcwd()
d = open("{}/{}".format(f, 'line_bot_secret_key.json'), 'r', encoding="big5")
secret_file = json.load(d)
server_url = secret_file.get('server_url')
app = Flask(__name__,static_url_path='/image_trpg_elevator',static_folder='../image_trpg_elevator/')

line_bot_api = LineBotApi(secret_file.get("channel_access_token"))
handler = WebhookHandler(secret_file.get('secret_key'))
count = 0

@app.route('/',methods = ['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info('Request body:' + body)

    try:
        handler.handle(body,signature)
    except:
        abort(400)
    return "OK"



from linebot.models import (
    TextSendMessage,ImageSendMessage,
    MessageEvent,TextMessage,
    QuickReply, QuickReplyButton,
    PostbackAction,PostbackEvent
)
# 消息製作
image = 'https://imgur.com/HsqGhhT.jpg'
reply_message_list = [
ImageSendMessage(original_content_url=image,preview_image_url=image),
    TextSendMessage(text='本遊戲含有恐怖及克蘇魯神話成分，請斟酌遊玩。請點擊下方圖片以開始遊戲')
]


from linebot.models.events import FollowEvent
import requests

# 這裡是在做發消息及取個資的動作

@handler.add(FollowEvent)
def reply_user_and_get_user_id(event):
    user_profile = line_bot_api.get_profile(event.source.user_id)
    with open('users_profile.txt','a') as us_file:
        us_file.write(json.dumps(vars(user_profile),sort_keys=True))
        us_file.write('\r\n')

    # 綁定圖文選單

    linkRichMenuId = open("image_trpg_elevator/rich_menu/rich_menu_main/rich_menu_id", 'r').read()
    line_bot_api.link_rich_menu_to_user(event.source.user_id,linkRichMenuId)

    # 關注回應
    line_bot_api.reply_message(
        event.reply_token,
        reply_message_list
    )

'''
san值小於0要gameover
'''


import character

# 幫玩家設定SAN值
@handler.add(MessageEvent,message = TextMessage)
def handler_message(event):
    global count
    if event.message.text == 'gamestart':
        character.character()
        ca = open('cb/ability.json','r')
        cb = json.load(ca)
        sanA = cb.get('san')
        con_QRB = QuickReply(items=[
                QuickReplyButton(
                action=PostbackAction(
                    label="了解了!",
                    data="text=capital_1"
                    )
                )
            ]
        )
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text="您的SAN值為{}，請努力不要讓SAN值歸零喔!".format(sanA)),
            TextSendMessage(text="遊戲開始..."),
            TextSendMessage(text="友情提示:本遊戲中有許多以骰子作檢定的動作\nSAN值都是以100面骰作檢定，若大於自身SAN值則做扣除SAN值判定，若小於自身SAN值則視情況做判定。",
            quick_reply=con_QRB)
            ]
        )
        line_bot_api.unlink_rich_menu_from_user(event.source.user_id)
        # 之後再把這行打開


        # TODO: 完成擲骰子的動作，順便考慮如何讓1D20之類的參數傳回去


    else:
        # TODO: 完成電梯內各種操作，考慮一下要使用圖文選單還是quickreply
        # 若是要做圖文選單可以做到下面
        count += 1
        character.count(count)
        pass



from urllib.parse import parse_qs

@handler.add(PostbackEvent)
def process_postback_event(event):
    query_postback_dict = parse_qs(event.postback.data)
    global count
    if 'menu' in query_postback_dict:
        # 在main_rich_menu裡面做出幾個圖文選單並綁定
        menu_message_local = query_postback_dict.get('menu')[0]
        linkRichMenuId = open("image_trpg_elevator/rich_menu/{}/rich_menu_id".format(menu_message_local), 'r').read()
        line_bot_api.link_rich_menu_to_user(event.source.user_id,linkRichMenuId)
        count += 1
        character.count(count)


    elif 'text' in query_postback_dict:
        text_message_local = "script/{}.json".format(query_postback_dict.get('text')[0])
        text_message_array = detect_json(text_message_local)
        line_bot_api.reply_message(
            event.reply_token,
            text_message_array
        )
        count += 1
        character.count(count)
    

    elif 'sign' in query_postback_dict:
        sign_name = {'sign_name':'true'}
        sign_in = json.load(open('cb/item.json'))
        if type(sign_in) is dict:
            sign_in = [sign_in]
        sign_in.append(sign_name)
        with open('cb/item.json','w') as sign_in_name:
            json.dump(sign_in,sign_in_name)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="在廣告上寫下了名字...")
        )
        count += 1
        character.count(count)
        

    elif 'unlink' in query_postback_dict:
        line_bot_api.unlink_rich_menu_from_user(event.source.user_id)
        unlink_message_local = "script/{}.json".format(query_postback_dict.get('unlink')[0])
        unlink_message_array = detect_json(unlink_message_local)
        line_bot_api.reply_message(
            event.reply_token,
            unlink_message_array
        )

    # elif 'dice' in query_postback_dict:
    #     unlink_message_local = "script/{}.json".format(query_postback_dict.get('unlink')[0])
        


        

if __name__ =='__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port)