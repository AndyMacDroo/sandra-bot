import os


class Config(object):

    def __init__(self):
        self.wit_ai_api_key = os.getenv("WIT_AI_API_KEY")

    def get_wit_ai_api_key(self):
        return self.wit_ai_api_key