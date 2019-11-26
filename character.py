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

    start_dict = {"0":"今天是禮拜天。\n探索者(你)因為某些理由，來到了一家大百貨公司。\n準備要往上的你，正好一個電梯到來了、你們就順勢靠了過去。\n叮～電梯開門了。\n各位請搭乘^^"
                    "1":"等大家都進了電梯，門便緩緩的關閉。\n你按下了想去的樓層。\n\n順帶一提，總共一到十樓，一到六樓是電器賣場、七到八樓是餐廳、九到十樓是停車場。"
                    "2": "按下了按鈕，電梯就緩緩上升。\n但是，不知道為什麼電梯沒有停在你按下的樓層，而是在四樓亮起的時候停了下來；所有的樓層燈都熄了下去。\n接著，不知道為什麼二樓的樓層燈自己亮了起來。\n沒打算停下、沒打開門、自己點亮的樓層燈。"
                }

start_script()