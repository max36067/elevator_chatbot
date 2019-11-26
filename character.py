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


def character():
    san = (randint(1,6)+randint(1,6)+randint(1,6))*5
    a = {'san':san}
    b = json.dumps(a)
    with open('cb/ability.json','w') as f:
        f.write(b)

# sancheck模組，主要用來偵測san值是否歸零
def lowsan():
    f = open('cb/ability.json','r')
    a = json.load(f)
    sancheck = a.get('san')
    restart_place = "script/gameover.json"
    # 如果san值過低，提醒玩家
    if 5 >= sancheck > 0:
        low = [TextSendMessage(text= "SAN值快沒了....")]
        return low
    # 如果san值歸零，提示玩家遊戲結束，是否重新開始遊玩 
    elif sancheck <= 0:
        gameover_list = [TextSendMessage(text= "SAN值歸零....遊戲結束。"),
        TemplateSendMessage(detect_json(restart_place))
        ]
        return gameover_list
    f.close()

def start_script():
    start_game = "script/start_script.json"
    start_check_json = detect_json(start_game)
    for i in start_check_json:
        time.sleep(2)