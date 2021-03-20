from game.crawl import Crawler

class CommandInterpreter():
    mapping = {
            "go": lambda player, noun: Crawler(player).walk(noun),
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

    @staticmethod
    def interact(player,verb,noun):
        action = CommandInterpreter.mapping(verb)
        action(player,noun)
        # NOTE(mateusz): each handle returns None on success and a string when an error
        # occured. That string describes the error
        