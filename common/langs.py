import json

class Langs:
    _lang_texts = None

    @staticmethod
    def load_json(config_file):
        with open(config_file,"r") as f:
            config = json.load(f)
        Langs._lang_texts = config

    @staticmethod
    def get_text(text_id):
        return Langs._lang_texts[text_id]
