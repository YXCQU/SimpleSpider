from io import BytesIO

from qqai.vision.ocr import GeneralOCR


# 验证码识别

def get_capture(content):
    robot = GeneralOCR(2111250258, '9fbpc02zxLdKjOIy')
    # base64 转为 文件格式
    file_like = BytesIO(content)
    result = robot.run(file_like)
    code = ''
    confidence = 0
    length = 0
    for i in result['data']['item_list'][0]['words']:
        # 只保留字母和数字
        if i['character'].isalnum():
            code += i['character']
            confidence += i['confidence']
            length += 1
    return {"ret": 0, "msg": "ok", "code": code, "confidence": round(confidence / length, 6)}

