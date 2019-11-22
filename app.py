# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
'''
啟動伺服器樣板
'''
from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
import json

secret_file = json.load(open('line_bot_secret_key.json','r'))
server_url = secret_file.get('server_url')
app = Flask(__name__,static_url_path='/image_trpg_elevator',static_folder='../image_trpg_elevator/')

line_bot_api = LineBotApi(secret_file.get("channel_access_token"))
handler = WebhookHandler(secret_file.get('secret_key'))

@app.route('/',methods = ['POST'])
def callback():
    signature = request.headers['X-Link-Signature']
    body = request.get_data(as_text=True)
    app.logger.info('Request body:' + body)

    try:
        handler.handle(body,signature)
    except:
        abort(400)
    return "OK"


# %%
from linebot.models import TextSendMessage,ImageSendMessage,MessageEvent,TextMessage
# 消息製作
reply_message_list = [
ImageSendMessage(original_content_url='https://{}/warning.png'.format(server_url)),
    TextSendMessage(text='本遊戲含有恐怖及克蘇魯神話成分，請斟酌遊玩')
]


# %%
from linebot.models.events import FollowEvent
import requests

# 這裡是在做發消息及取個資的動作

@handler.add(FollowEvent)
def reply_user_and_get_user_id(event):
    user_profile = line_bot_api.get_profile(event.source.user_id)
    with open('../users_profile.txt','a') as us_file:
        us_file.write(json.dumps(vars(user_profile),sort_keys=True))
        us_file.write('\r\n')

    # 綁定圖文選單
    LineRichMenuMainID = secret_file.get('rich_menu_id')
    linkResult = line_bot_api.link_rich_menu_to_user(secret_file["self_user_id"],LineRichMenuMainID)

    # 關注回應
    line_bot_api.reply_message(
        event.reply_token,
        reply_message_list
    )


# %%
if __name__ =='__main__':
    app.run(host='0.0.0.0')

