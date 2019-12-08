from random import randint
import json
from linebot.models import TextSendMessage,QuickReply, QuickReplyButton,PostbackAction

def san_save(user_id,san):
    with open('cb/ability.json','r') as f:
        bb = json.load(f)
        with open('cb/ability.json','w') as d:
            bb[user_id]['san'] = san
            json.dump(bb,d)

def lowsan(san_check,san_check_list):
    if 5 >= san_check > 0:
        low = [TextSendMessage(text= "SAN值快沒了....")]
        san_check_list.append(low)
        return san_check_list
    # 如果san值歸零，提示玩家遊戲結束，是否重新開始遊玩 
    elif san_check <= 0:
        con_QRB = QuickReply(items=[
                QuickReplyButton(
                action=PostbackAction(
                    label="game over",
                    data="text=template"
                    )
                )
            ]
        )
        gameover_list = [TextSendMessage(text= "SAN值歸零了....。"),
        TextSendMessage(text="你的精神開始錯亂、失控，你無法相信這一切，於是一頭撞向電梯的各個角落...最終失血過多而身亡",quick_reply=con_QRB)
        ]
        san_check_list.append(gameover_list)
        return san_check_list
        # 之後要加上gameover的東西
    else:
        return san_check_list

def dice_(user_id,dice_number):
    dice_roll_num = randint(1,100)
    f = open('cb/ability.json','r')
    a = json.load(f)
    san = a[user_id]['san']
    f.close()
    san_check_list = [
        TextSendMessage(text="骰出來的SAN值檢定為{}".format(dice_roll_num)),
        TextSendMessage(text="您的SAN值為{}".format(san))
    ]
    F = {"D0_12": randint(1,2),
        "D13_241": randint(1,4)+randint(1,4)+1,
        "D16_120": randint(1,20),
        "D1_161": randint(1,6)+1
        }
    G = {"D0_12": "text=check_over_01",
        "D13_241": "text=check_over_02",
        "D16_120": "text=check_over_03",
        "D1_161": "text=check_over_04"
        }
    continue_ = QuickReply(items=[
                QuickReplyButton(
                action=PostbackAction(
                    label="繼續",
                    data=G[dice_number]
                    )
                )
            ]
        )
    if dice_roll_num > san:
        
        p = san - F[dice_number]
        san_save(user_id,p)
        
        san_check_list.append(TextSendMessage(text="您被扣除了{}點SAN值，剩餘SAN值為{}".format(F[dice_number],p),quick_reply=continue_))
        
        return lowsan(p,san_check_list)
        
    
    elif dice_roll_num <= san:
        p = san - F[dice_number]
        san_save(user_id,p)
        san_check_list.append(TextSendMessage(text="您被扣除了{}點SAN值，剩餘SAN值為{}".format(F[dice_number],p),quick_reply=continue_))


        return lowsan(p,san_check_list)


    