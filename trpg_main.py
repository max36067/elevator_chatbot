'''
執行程式主要檔案


'''
import json,requests
from linebot import LineBotApi,WebhookHandler
from linebot.models import RichMenu

# 開啟secretkey準備與line做連結
secret_file = json.load(open('line_bot_secret_key.json','r',encoding='utf-8'))

print(secret_file.get("channel_access_token"))
print(secret_file.get("secret_key"))
print(secret_file.get("self_user_id"))

line_bot_api = LineBotApi(secret_file.get("channel_access_token"))

# 請line_bot_api上傳圖文選單給line
MainMenu = json.load(open('rich_menu_main.json','rb'))
LineRichMenuMainID = line_bot_api.create_rich_menu(rich_menu=RichMenu.new_from_json_dict(MainMenu))
print(LineRichMenuMainID)

# 用line_bot_api載入照片
upload_RM_main = open("image_trpg_elevator\\cosulu.jpg",'rb')

setImage_RM_main = line_bot_api.set_rich_menu_image(LineRichMenuMainID,"image/png",upload_RM_main)
print(setImage_RM_main)

