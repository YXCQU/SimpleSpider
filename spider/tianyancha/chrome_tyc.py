from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome import options
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import time
import random


class ReuseChrome(Remote):

    def __init__(self, command_executor, session_id):
        self.r_session_id = session_id
        Remote.__init__(self, command_executor=command_executor, desired_capabilities={})

    def start_session(self, capabilities, browser_profile=None):
        """
        重写start_session方法
        """
        if not isinstance(capabilities, dict):
            raise InvalidArgumentException("Capabilities must be a dictionary")
        if browser_profile:
            if "moz:firefoxOptions" in capabilities:
                capabilities["moz:firefoxOptions"]["profile"] = browser_profile.encoded
            else:
                capabilities.update({'firefox_profile': browser_profile.encoded})

        self.capabilities = options.Options().to_capabilities()
        self.session_id = self.r_session_id
        self.w3c = False


#  第一次使用Chrome() 新建浏览器会话
driver = webdriver.Chrome()

# 记录 executor_url 和 session_id 以便复用session
executor_url = driver.command_executor._url
session_id = driver.session_id
# 访问百度
driver.get("https://www.baidu.com")

print(session_id)
print(executor_url)

# 假如driver对象不存在，但浏览器未关闭
# del driver

# 使用ReuseChrome()复用上次的session
driver2 = ReuseChrome(command_executor=executor_url, session_id=session_id)

# 打印current_url为百度的地址，说明复用成功
print(driver2.current_url)

file_name = 'excel1.txt'
with open(file_name, 'r') as f:
    for line in f.readlines():
        res = ' '
        try:
            # time.sleep(random.randint(1, 3))
            time.sleep(1.25)
            driver2.get("https://www.tianyancha.com/search?key={}".format(line))
            try:
                element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "search-item"))
                )
            except:
                res = ' '
            r = driver2.page_source
            html = etree.HTML(r)
            result = \
                html.xpath('//*[@id="web-content"]/div/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/span/text()')[0]
            print(result)
            res = result
            if not res:
                res = ' '
        except:
            res = ' '
        finally:
            with open('res_' + file_name, 'a') as f1:
                f1.write(res)
                f1.write('\n')

time.sleep(10)
driver2.close()
