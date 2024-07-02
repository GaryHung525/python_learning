import json
from dataclasses import dataclass
from dacite import from_dict

from test.BaseObj import BaseObj


@dataclass
class Test222(BaseObj):
    xx: str
    yy: str
    zz: int

@dataclass
class Test111(BaseObj):
    aa: Test222
    bb: str
    keysToUpdate: list[str]
    def test(self):
        has_value_keys = []
        attrs = [attr for attr in dir(self) if not attr.startswith('__') and not callable(getattr(self, attr))]
        for attr in attrs:
            if attr == 'keysToUpdate':
                continue
            tmp_val = getattr(self, attr)
            if tmp_val is not None and tmp_val != "":
                has_value_keys.append(attr)
        setattr(self, 'keysToUpdate', has_value_keys)

str_tmp = '{"aa":{"xx":"11","yy":"aa","zz":33},"bb":"bbbb"}'

j = json.loads(str_tmp)

test111 = Test111.from_json(str_tmp)
test111.test()
print(test111)