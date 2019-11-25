import json
from linebot.models import RichMenu
import requests
from linebot import LineBotApi,WebhookHandler


def run():
    secretfile = json.load(open('line_bot_Trpg\\line_bot_secret_key.json','r',encoding='utf-8'))

    line_bot_api = LineBotApi(secretfile.get('channel_access_token'))

    menujson = json.load(open('line_bot_Trpg\\rich_menu_main.json','r',encoding='utf-8'))

    lineRichmenu = line_bot_api.create_rich_menu(rich_menu=RichMenu.new_from_json_dict(menujson))
    print(lineRichmenu)

    uploadImageFile = open('line_bot_Trpg\\image_trpg_elevator\\cosulu.jpg','rb')
    line_bot_api.set_rich_menu_image(lineRichmenu,'image/jpg',uploadImageFile)

    linkResult = line_bot_api.link_rich_menu_to_user(secretfile['self_user_id'],lineRichmenu)
    print(linkResult)