class PlayerCommandInterpreter():
    def __init__(self, player, verb, noun):
        self.player = player
        self.verb = verb
        self.noun = noun
        self.mapping = {
            "go": self.walk,
            "drop": lambda noun: "Not yet implemented",
            "attack": lambda noun: "Not yet implemented",
            "open": lambda noun: "Not yet implemented",
            "talk": lambda noun: "Not yet implemented",
            "equip": lambda noun: "Not yet implemented",
            "list": lambda noun: "Not yet implemented",
            "eat": lambda noun: "Not yet implemented",
            "drink": lambda noun: "Not yet implemented",
            "sleep": lambda noun: "Not yet implemented",
            "use": lambda noun: "Not yet implemented",
            "search": lambda noun: "Not yet implemented",
            "look": lambda noun: "Not yet implemented",
            "dismiss": lambda noun: "Not yet implemented"
        }

        # NOTE(mateusz): each handle returns None on success and a string when an error
        # occured. That string describes the error
        