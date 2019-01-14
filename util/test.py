import requests
from io import BytesIO
from qqai.vision.ocr import GeneralOCR

r = requests.get('https://proxy.mimvp.com/common/ygrcode.php')

robot = GeneralOCR(2111250258, '9fbpc02zxLdKjOIy')

# base64 转为 文件格式
file_like = BytesIO(r.content)

result = robot.run(file_like)
print(result)
