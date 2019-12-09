'''

創建腳色選單
隨機能力值?
固定能力值?

'''
import json
from json_ import detect_json
from linebot.models import TextSendMessage,MessageEvent,TemplateSendMessage,QuickReply, QuickReplyButton,PostbackAction,ImageSendMessage,VideoSendMessage
from linebot import LineBotApi
from random import randint
import time
import main_rich_menu as mrm
import os

f = os.getcwd()
d = open("{}/{}".format(f, 'line_bot_secret_key.json'), 'r', encoding="big5")
secret_file = json.load(d)
line_bot_api = LineBotApi(secret_file.get("channel_access_token"))


def character(user_id):
    san = (randint(1,6)+randint(1,6)+randint(1,6))*5
    with open('cb/ability.json','r') as f:
        dic = json.load(f)
        with open('cb/ability.json','w') as d:
            dic[user_id] = {'san':san}
            json.dump(dic,d)





def count(user_id,count_times):
    # 四
    if 18 > count_times >= 0:
        linkRichMenuId = open("image_trpg_elevator/rich_menu/rich_menu_2/rich_menu_id", 'r').read()
        line_bot_api.link_rich_menu_to_user(user_id,linkRichMenuId)
    #二
    elif 26 > count_times >= 18:
        linkRichMenuId = open("image_trpg_elevator/rich_menu/rich_menu_3/rich_menu_id", 'r').read()
        line_bot_api.link_rich_menu_to_user(user_id,linkRichMenuId)
        
    # 六
    elif 34 > count_times >= 26:
        linkRichMenuId = open("image_trpg_elevator/rich_menu/rich_menu_2/rich_menu_id", 'r').read()
        line_bot_api.link_rich_menu_to_user(user_id,linkRichMenuId)
        
    # 二
    elif 42 > count_times >= 34:
        linkRichMenuId = open("image_trpg_elevator/rich_menu/rich_menu_5/rich_menu_id", 'r').read()
        line_bot_api.link_rich_menu_to_user(user_id,linkRichMenuId)
        
    # 十
    elif 50 > count_times >= 42:
        linkRichMenuId = open("image_trpg_elevator/rich_menu/rich_menu_4/rich_menu_id", 'r').read()
        line_bot_api.link_rich_menu_to_user(user_id,linkRichMenuId)
        
    # 五
    elif 58 > count_times >= 50:
        linkRichMenuId = open("image_trpg_elevator/rich_menu/rich_menu_6/rich_menu_id", 'r').read()
        line_bot_api.link_rich_menu_to_user(user_id,linkRichMenuId)
        
    # 一
    elif count_times >= 58:
        linkRichMenuId = open("image_trpg_elevator/rich_menu/rich_menu_10/rich_menu_id", 'r').read()
        line_bot_api.link_rich_menu_to_user(user_id,linkRichMenuId)



def floor_move(user_id,count_number):
    if count_number == 15:
        line_bot_api.push_message( user_id, TextSendMessage(text="電梯開始移動了..貌似是向下移動。"))
    elif count_number == 23:
        line_bot_api.push_message( user_id, TextSendMessage(text="電梯開始移動了..貌似是向上移動。"))
    elif count_number == 31:
        line_bot_api.push_message( user_id, TextSendMessage(text="電梯開始移動了..貌似是向下移動。"))
    elif count_number == 39:
        line_bot_api.push_message( user_id, TextSendMessage(text="電梯開始移動了..貌似是向上移動。"))
    elif count_number == 47:
        line_bot_api.push_message( user_id, TextSendMessage(text="電梯開始移動了..貌似是向下移動。"))
    elif count_number == 55:
        line_bot_api.push_message( user_id, TextSendMessage(text="電梯開始移動了..貌似是向下移動。"))
    elif count_number == 63:
        line_bot_api.push_message( user_id, 
        TextSendMessage(text="電梯開始移動了..貌似是向上移動。")
        )
        line_bot_api.unlink_rich_menu_from_user(user_id)
        con_QRB = QuickReply(items=[
                    QuickReplyButton(
                    action=PostbackAction(
                        label="game over",
                        data="text=template"
                        )
                    )
                ]
            )
        with open('cb/sign.json','r') as f:
            sign_check = json.load(f)
            if sign_check[user_id]['sign'] == "true":
                line_bot_api.push_message( user_id,
                TextSendMessage(text="電梯停在了十樓，電梯門輕巧的打開，在你眼前的，是不曾在現實中看過、無盡的黑暗\n無關你自己的意志、你就這樣走出了電梯...\n這之後會發生什麼，就無法得知了...",quick_reply=con_QRB)
                )
            else:
                time.sleep(3)
                line_bot_api.push_message( user_id,
                TextSendMessage(text="但是電梯沒在十樓停下，電梯再度往上移動....\n接著，「空－」的一聲，樓層顯示中的「地獄」、「天堂」的樓層燈亮起來了\n瞬間，探索者(你)感覺身體似乎浮了起來\n接著，探索者(你)沒了知覺....")
                )
                linkRichMenuId = open("image_trpg_elevator/rich_menu/rich_menu_12/rich_menu_id", 'r').read()
                line_bot_api.link_rich_menu_to_user(user_id,linkRichMenuId)
                line_bot_api.push_message(
                    user_id,
                    VideoSendMessage(original_content_url="https://imgur.com/oxBHMzG.mp4",
                    preview_image_url="https://memeprod.s3.ap-northeast-1.amazonaws.com/user-wtf/1573911645133.jpg")
                )
                time.sleep(5)
                line_bot_api.unlink_rich_menu_from_user(user_id)
                line_bot_api.push_message( user_id,
                TextSendMessage(text="當天晚上，新聞播報了電梯墜落事故，死者數名的消息.....",quick_reply=con_QRB))
        
    elif count_number == 18:
        line_bot_api.push_message( user_id, TextSendMessage(text="電梯停下了，面板上六樓的燈亮了起來"))
    elif count_number == 26:
        line_bot_api.push_message( user_id, TextSendMessage(text="電梯停下了，面板上二樓的燈亮了起來"))
    elif count_number == 34:
        line_bot_api.push_message( user_id, TextSendMessage(text="電梯停下了，面板上十樓的燈亮了起來"))
    elif count_number == 42:
        ghost_come = QuickReply(items=[
                QuickReplyButton(
                action=PostbackAction(
                    label="...",
                    data="text=ghost_1"
                    )
                )
            ]
        )
        line_bot_api.unlink_rich_menu_from_user(user_id)
        line_bot_api.push_message( user_id, TextSendMessage(text="電梯停下了，面板上五樓的燈亮了起來",quick_reply=ghost_come))
    elif count_number == 50:
        line_bot_api.push_message( user_id, TextSendMessage(text="電梯停下了，面板上一樓的燈亮了起來"))
    elif count_number == 58:
        line_bot_api.push_message( user_id, TextSendMessage(text="電梯停下了，面板上十樓的燈亮了起來"))