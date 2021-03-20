class PlayerCommandInterpreter():
    def __init__(self, player, verb, noun):
        self.player = player
        self.verb = verb
        self.noun = noun
        self.mapping = {
            "go": self.go_handling,
            "drop": self.drop_handling,
            "attack": self.attack_handling,
            "open": self.open_handling,
            "talk": self.talk_handling,
            "equip": self.equip_handling,
            "list": self.list_handling,
            "eat": self.eat_handling,
            "drink": self.drink_handling,
            "sleep": self.sleep_handling,
            "use": self.use_handling,
            "search": self.search_handling,
            "look": self.look_handling,
            "dismiss": self.dismiss_handling
        }

        # NOTE(mateusz): each handle returns None on success and a string when an error
        # occured. That string describes the error
        
        def go_handling(self, noun):
            return "Not yet implemented"
        
        def drop_handling(self, noun):
            return "Not yet implemented"
        
        def attack_handling(self, noun):
            return "Not yet implemented"
        
        def open_handling(self, noun):
            return "Not yet implemented"
        
        def talk_handling(self, noun):
            return "Not yet implemented"
        
        def equip_handling(self, noun):
            return "Not yet implemented"
        
        def list_handling(self, noun):
            return "Not yet implemented"
        
        def eat_handling(self, noun):
            return "Not yet implemented"
        
        def drink_handling(self, noun):
            return "Not yet implemented"
        
        def sleep_handling(self, noun):
            return "Not yet implemented"
        
        def use_handling(self, noun):
            return "Not yet implemented"
        
        def search_handling(self, noun):
            return "Not yet implemented"
        
        def look_handling(self, noun):
            return "Not yet implemented"
        
        def dismiss_handling(self, noun):
            if noun == 'tutorial':
                self.player.seen_tutorial = True
                return None
            else:
                # TODO(mateusz): Maybe each handler can know in an array what things is expects and
                # upon error will tell what it can take as an argument
                
                return "Cannot _dismiss_ " + noun + " possible options are (tutorial)"
