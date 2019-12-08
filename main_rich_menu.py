import json
from linebot.models import RichMenu
import requests
from linebot import LineBotApi,WebhookHandler
secretfile = json.load(open('line_bot_secret_key.json','r',encoding='utf-8'))
line_bot_api = LineBotApi(secretfile.get('channel_access_token'))
def run():
    rich_menu_array = ['rich_menu_main','rich_menu_button_1','rich_menu_button_2','rich_menu_control','rich_menu_control_1']
    for i in range(1,13):
        c = 'rich_menu_{}'.format(i)
        rich_menu_array.append(c)

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

# run()

# rich_menu_list = line_bot_api.get_rich_menu_list()
# for rich_menu in rich_menu_list:
#     line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)