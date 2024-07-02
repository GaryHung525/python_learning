import base64


class base64Util:
    @staticmethod
    def base64_encode(data):
        return base64.b64encode(bytes('{}'.format(data),'utf-8'))


    @staticmethod
    def base64_decode(data):
        return base64.b64decode(data).decode('utf-8')
