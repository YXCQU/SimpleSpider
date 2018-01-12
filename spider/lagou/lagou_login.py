from selenium import webdriver

"""
拉勾网模拟登录
"""


def get_lagaou_cookie():
    browser = webdriver.Chrome(executable_path="D:/mylibs/chromedriver/chromedriver.exe")
    browser.get("https://passport.lagou.com/login/login.html")
    browser.find_element_by_xpath("/html/body/section/div[1]/div[2]/form/div[1]/input").send_keys("18875299597")
    browser.find_element_by_xpath("/html/body/section/div[1]/div[2]/form/div[2]/input").send_keys("5201314xf")
    browser.find_element_by_xpath("/html/body/section/div[1]/div[2]/form/div[5]/input").click()
    browser.get("https://www.lagou.com")
    print(browser.get_cookies())
    browser.close()


if __name__ == '__main__':
    s = get_lagaou_cookie()
    print(s)
#
# import requests
# import hashlib
# from bs4 import BeautifulSoup
#
# s = requests.Session()
# username = '18875299597'
# password = '5201314xf'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "DNT": "1",
#     "Host": "passport.lagou.com",
#     "Origin": "https://passport.lagou.com",
#     "Referer": "https://passport.lagou.com/login/login.html",
# }
#
#
# def lagou_encrypt(password):
#     c = "veenike"
#     password = hashlib.md5(password.encode('utf-8')).hexdigest()
#     password = hashlib.md5((c + password + c).encode('utf-8')).hexdigest()
#     return password
#
#
# """
# X-Anit-Forge-Code : 13630219
# X-Anit-Forge-Token : faba0d17-eeba-4d04-82ff-a13bc8e809e0
# """
#
#
# def set_token():
#     r = requests.get('https://passport.lagou.com/login/login.html', headers=headers)
#     soup = BeautifulSoup(r.text, 'lxml')
#     tokens = soup.select("script")[1].text.strip()
#     X_Anti_Forge_Token = ''
#     X_Anti_Forge_Code = ''
#
#
# set_token()
# print(password)
