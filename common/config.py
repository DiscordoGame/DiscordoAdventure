import json

class Config:
    cfg = None

    @staticmethod
    def load_from(path):
        if isinstance(path, str):
            content = open(path, 'r').read()
            Config.cfg = json.loads(content)
        else:
            raise TypeError("path must be a string")

    @staticmethod
    def get():
        return Config.cfg
        
    @staticmethod
    def get_by_key(key):
        """
        You're getting your value or None if the key doesn't exists
        """
        
        return Config.cfg[key] if key in Config.cfg else None

    @staticmethod
    def set_by_key(key, value):
        Config.cfg[key] = value

    
