import random
from common.config import Config

def get_rarity():
    chances = Config.get_by_key("rarity")
    probab = sorted([int(i) for i in chances.keys()])
    roll = random.random() * 100
    for chance in probab:
        if(roll < chance):
            return chances[str(chance)]
        
