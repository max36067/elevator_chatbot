'''

創建腳色選單
隨機能力值?
固定能力值?

'''
import json
from random import randint


def character():
    san = (randint(1,6)+randint(1,6)+randint(1,6))*5
    a = {'san':san}
    b = json.dumps(a)
    with open('cb/ability.json','w') as f:
        f.write(b)

    

character()