from common.dbhandler import DatabaseHandler
from common.utils import get_rarity
import random

class Crawler:
    
    def __init__(self, player_id):
        self.player_id = player_id 
        self.current_region = 0#GET PLAYER_CURRENT_REGION
        self.directions_from =  ["north","east","south","west"]
                
    def walk(self, direction):
        in_battle = False #IF_MONSTERS_IN_REGION_CANT_ESCAPE
        bot_response = ""
        if not in_battle:
            is_explored = False #QUERY, CHECKS IS OF DIRECTION FROM THAT REGION
            if is_explored:
                biome = "mountains" #QUERY, GET BIOME NAME FROM REGION
                description = "land of beers"
                bot_response = f"Travelling to {biome}, {description}"
                monsters_spawned = 0 #QUERY, get amount of monsters
                loot_spawned = 0
                if monsters_spawned == 0:
                    self.generate_entities(biome,monster=True)
                if loot_spawned == 0:
                    self.generate_entities(biome,item=True)
                self.move_player(1) 
            else:
                bot_response = self.generate_region(direction)
        else:
            bot_response = "Can't run away from battle"
        return bot_response
    
    def move_player(self,region_id):
        self.current_region = region_id    
        return #QUERY WHICH WILL SET PLAYER TO SELECTED ID
    
    def generate_region(self,direction):
        back_index = (self.directions_from.index(direction)+2)%3
        direction_back = self.directions_from[back_index] # SET DIRECTION BACK
        biome_rarity = get_rarity()
        biome_list = ["tundra","jungle","temple"] #QUERY, BIOMES WITH biome_rarity
        biome = random.choice(biome_list)
        description = "full of tres, trees, and treees"
        reg_id = 420 #CREATE ROW, WITH ID, RETURN THIS ID, SET DIRECTION FROM DRIECTION BACK FROM current_region
        self.generate_enemies(biome,monster=True)
        self.generate_entities(biome,item=True)
        return f"Exploring {biome}, {description}"
        
    def generate_entities(self,biome,monster=False,item=False):
        if (not item and not monster) or (item and monster):
            return []
        entities = []
        entity_count = 5 #QUERY, GET MONSTER_COUNT
        for i in range(0,random.randint(1,entity_count)):
            how_rare = get_rarity()
            entity_list = ["waldek","wilczur","big chunugs"] #QUERY, ALL MONSTERS WHERE BIOME = ID AND RARITY = how_rare
            name = random.choice(entity_list)
            entity_dict={}
            if monster:
                entity_dict = {"name":name,"hp":100,"attack":100,"defense":100} #QUERY, get monster stats
            elif item:
                entity_dict = {"name":"Banknot Wenezuelski","value":10000000,"type":"GOLD"}
            entities.append(entity_dict)
        #QUERY UPDATE REGION WITH CURRENT MONSTERS
        return entities
