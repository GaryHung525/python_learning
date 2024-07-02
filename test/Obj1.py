from test.Base64Util import base64Util
from test.BaseObj import BaseObj

class Test2(BaseObj):
    def __init__(self, xxx,yyy):
        self.xxx = xxx
        self.yyy = yyy
class Test(BaseObj):
    def __init__(self,test2:Test2, x, y, z, keysToUpdate):
        self.test2 = Test2.from_json(test2)
        self.x = x
        self.y = y
        self.z = z
        self.keysToUpdate = keysToUpdate

    def test(self):
        has_value_keys = []
        attrs = [attr for attr in dir(self) if not attr.startswith('__') and not callable(getattr(self, attr))]
        for attr in attrs:
            tmp_val = getattr(self, attr)
            if tmp_val is not None and tmp_val != "":
                has_value_keys.append(attr)
        setattr(self, 'keysToUpdate', has_value_keys)

# b64 = "eyAieSI6ICIiLCJ4IjogIjEiLCJ6IjoiIn0=".encode('ascii')
b64 = base64Util.base64_encode('{ "test2":{"xxx":"","yyy":"yyy"},"y": "","x": "1","z":""}')
print(b64)
json = base64Util.base64_decode(b64)
print(json)
test = Test.from_json(json)
test.test()
print(test.to_json())
