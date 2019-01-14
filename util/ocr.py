from qqai.vision.ocr import GeneralOCR


def get_capture(url=None):
    url = 'https://proxy.mimvp.com/common/ygrcode.php'
    robot = GeneralOCR(2111250258, '9fbpc02zxLdKjOIy')
    result = robot.run(url)
    code = ''
    confidence = 0
    length = 0
    for i in result['data']['item_list'][0]['words']:
        # 只保留字母和数字
        if i['character'].isalnum():
            code += i['character']
            confidence += i['confidence']
            length += 1
    return {"ret": 0, "msg": "ok", "code": code, "confidence": round(confidence/length, 6)}


print(get_capture())
