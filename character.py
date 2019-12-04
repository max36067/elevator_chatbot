'''

創建腳色選單
隨機能力值?
固定能力值?

'''
import json
from json_ import detect_json
from linebot.models import TextSendMessage,MessageEvent,TemplateSendMessage
from random import randint
import time
import main_rich_menu as mrm
import os



def character(user_id):
    san = (randint(1,6)+randint(1,6)+randint(1,6))*5
    with open('cb/ability.json','r') as f:
        dic = json.load(f)
        with open('cb/ability.json','w') as d:
            dic[user_id] = {'san':san}
            json.dump(dic,d)



# sancheck模組，主要用來偵測san值是否歸零
def lowsan(user_id):
    f = open('cb/ability.json','r')
    a = json.load(f)
    sancheck = a[user_id]['san']
    restart_place = "script/gameover.json"
    # 如果san值過低，提醒玩家
    if 5 >= sancheck > 0:
        low = [TextSendMessage(text= "SAN值快沒了....")]
        return low
    # 如果san值歸零，提示玩家遊戲結束，是否重新開始遊玩 
    elif sancheck <= 0:
        gameover_list = [TextSendMessage(text= "SAN值歸零了....。"),
        detect_json(restart_place)
        ]
        return gameover_list
    f.close()

'''
如何做出1D2，1D3等等差別?
讓值傳入函數?
'''





def count(count_times):
    # 四
    if count_times == 7:
        pass
    # 二
    elif count_times == 11:
        pass
    # 六
    elif count_times == 15:
        pass
    # 二
    elif count_times == 19:
        pass
    # 十
    elif count_times == 23:
        pass
    # 五
    elif count_times == 27:
        pass
    # 一
    elif count_times == 31:
        pass
    # 十
    elif count_times == 35:
        pass