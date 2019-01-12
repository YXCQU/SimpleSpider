from qqai.vision.ocr import GeneralOCR


def get_capture():
    robot = GeneralOCR(2111250258, '9fbpc02zxLdKjOIy')
    result = robot.run('https://proxy.mimvp.com/common/ygrcode.php?rcode=123456')
    # 打开本地图片识别
    # with open('pic.png', 'rb') as image_file:
    #     result = robot.run(image_file)
    code = ''
    for i in result['data']['item_list'][0]['words']:
        # 只保留字母和数字
        if i['character'].isalnum():
            code += i['character']
    return code


print(get_capture())
