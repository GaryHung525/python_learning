import inspect
import json
from dacite import from_dict

class BaseObj:

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        for k, v in inspect.signature(cls.__init__).parameters.items():
            if k != "self" and not json_dict.__contains__(k):
                if v.annotation == list[str]:
                    json_dict[k] = []
                else:
                    json_dict[k] = None
        return from_dict(data_class=cls,data=json_dict)

    def to_json(self):
        return json.dumps(self.__dict__)
