import json
from linebot.models import RichMenu
import requests
from linebot import LineBotApi,WebhookHandler


def run():
    secretfile = json.load(open('line_bot_secret_key.json','r',encoding='utf-8'))
    
    line_bot_api = LineBotApi(secretfile.get('channel_access_token'))

    rich_menu_array = ['rich_menu_main','rich_menu_1','rich_menu_7']

    for rich_menu_name in rich_menu_array:
        lineRichMenuId = line_bot_api.create_rich_menu(rich_menu=RichMenu.new_from_json_dict(json.load(open('image_trpg_elevator/rich_menu/{}/{}.json'.format(rich_menu_name,rich_menu_name),'r',encoding='utf-8'))))
        print('設定上傳結果')
        print(lineRichMenuId)
        
        f = open('image_trpg_elevator/rich_menu/{}/rich_menu_id'.format(rich_menu_name),'w',encoding='utf-8')
        f.write(lineRichMenuId)
        f.close()
    
        with open('image_trpg_elevator/rich_menu/{}/{}.jpg'.format(rich_menu_name,rich_menu_name),'rb') as f:
            set_image_response = line_bot_api.set_rich_menu_image(lineRichMenuId,'image/jpeg',f)
        print('圖片上傳結果')
        print(set_image_response)
        
    # menujson = json.load(open('cb/rich_menu_main.json','r',encoding='utf-8'))
    
    # lineRichmenu = line_bot_api.create_rich_menu(rich_menu=RichMenu.new_from_json_dict(menujson))
    
    # uploadImageFile = open('image_trpg_elevator/cosulu.png','rb')
    
    # line_bot_api.set_rich_menu_image(lineRichmenu,'image/png',uploadImageFile)
    
    # line_bot_api.link_rich_menu_to_user(secretfile['self_user_id'],lineRichmenu)



# def any_rich_menu(filename):
#     secretfile = json.load(open('line_bot_secret_key.json','r',encoding='utf-8'))
    
#     line_bot_api = LineBotApi(secretfile.get('channel_access_token'))
    
#     menujson = json.load(open('cb/{}.json'.format(filename),'r',encoding='utf-8'))
    
#     lineRichmenu = line_bot_api.create_rich_menu(rich_menu=RichMenu.new_from_json_dict(menujson))
    
#     uploadImageFile = open('image_trpg_elevator/rich_menu/{}.jpg'.format(filename),'rb')
    
#     line_bot_api.set_rich_menu_image(lineRichmenu,'image/jpeg',uploadImageFile)
    
#     line_bot_api.link_rich_menu_to_user(secretfile['self_user_id'],lineRichmenu)