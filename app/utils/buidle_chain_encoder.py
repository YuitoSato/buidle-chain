from json import JSONEncoder


class BuidleChainEncoder(JSONEncoder):
    def default(self, o):
        return JSONEncoder.default(self, o)
