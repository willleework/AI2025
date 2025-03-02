from vanna.ollama import Ollama
from vanna.vannadb import VannaDB_VectorStore

class MyVanna(VannaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        MY_VANNA_MODEL = 'deepseek-r1:7b'# Your model name from https://vanna.ai/account/profile''
        VannaDB_VectorStore.__init__(self, vanna_model=MY_VANNA_MODEL, vanna_api_key=MY_VANNA_API_KEY, config=config)
        Ollama.__init__(self, config=config)

vn = MyVanna(config={'model': 'mistral'})