import inspect
import json

class BaseObj:
    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        for n, p in inspect.signature(cls.__init__).parameters.items():
            if n != "self" and not json_dict.__contains__(n):
                json_dict[n] = None
        return cls(**json_dict)

    def to_json(self):
        return json.dumps(self.__dict__)
