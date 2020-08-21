import json

class JsonUtils(object):

    @staticmethod
    def loadList(path: str) -> list:
        with open(path, mode='r') as f:
            return json.load(f)

    @staticmethod
    def saveList(l: list, path: str) -> None:
        with open(path, mode='w') as f:
            json.dump(l, f)
