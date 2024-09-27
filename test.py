import json

_INSTANCE = None

# https://pastebin.com/vw7RczKZ

class AClass:
    def __init__(self, a, b):
        self.a = a
        self.__b = b

    def get_b(self):
        return self.__b

    @staticmethod
    def get_instance():
        global _INSTANCE
        if _INSTANCE is None:
            _INSTANCE = AClass(1, 2)
        return _INSTANCE

    @staticmethod
    def from_json_dict(obj):
        return AClass(obj["a"], obj["b"])

    def __repr__(self):
        return "This instance of AClass contains" + str({"a": self.a, "b": self.__b})

json_str = """
{
    "a": 3,
    "b": 4
}
"""

from_json_str = json.loads(json_str)
print(AClass.from_json_dict(from_json_str))
