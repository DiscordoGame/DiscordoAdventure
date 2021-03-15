import re

class CmdParser:
    def __init__(self, user_input):
        self.content = user_input
        self.parsed = None
        
    @property
    def is_command(self):
        if self.parsed == None:
            self.parse()
            
        return self.parsed['is_cmd']

    def parse(self):
        if len(self.content) == 0 or self.content[0] != '!':
            self.parsed = { "is_cmd": False }
            return

        s = self.content[1:].strip()
        parts = re.compile(" +").split(s)

        self.parsed = {
            "is_cmd": True,
            "cmd": parts[0],
            "args": parts[1:]
        }

    def get_command(self):
        if self.parsed == None:
            self.parse()

        return self.parsed['cmd']

    def get_arguments(self):
        if self.parsed == None:
            self.parse()

        return self.parsed['args']
