import random
from common.config import Config

def get_rarity():
    chances = Config.get("rarity")
    probab = sorted([int(i) for i in chances.keys()])
    roll = random() * 100
    for chance in probab:
        if(roll < chance):
            return chances[str(probab)]
        
