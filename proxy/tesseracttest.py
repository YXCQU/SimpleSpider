from PIL import Image, ImageFilter, ImageEnhance
import pytesseract

# 二值化
threshold = 125
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)


# 识别验证码
def get_vcode():
    # 打开原始图像
    image = Image.open("C:/Users/YX/Pictures/test15.png")

    # 将图像转为灰度，并另存为
    bimage = image.convert('L')
    bimage.save('g' + "getimgbysig.png")

    # 进行二值化处理，并另存为
    out = bimage.point(table, '1')
    out.save('b' + "getimgbysig.png")

    icode = pytesseract.image_to_string(image)
    bcode = pytesseract.image_to_string(bimage)
    vcode = pytesseract.image_to_string(out)
    print(icode, bcode, vcode)
    # text = pytesseract.image_to_string(Image.open('C:/Users/YX/Pictures/test8.png'))
    # print(text)


if __name__ == '__main__':
    get_vcode()
