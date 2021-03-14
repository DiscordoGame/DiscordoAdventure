import random

def get_random(chances_map):
    #{example 70:"common",20:"rare",5:"epic",0.1:"legendary"}
    
    probab = sorted(chances_map.keys())
    roll = random() * 100
    for chance in probab:
        if(roll < chance):
            return chances_map[probab]
        
