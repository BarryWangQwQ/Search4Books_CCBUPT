from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time

# 无UI模式
def Console():
   print("SYSETM: Running With Console ...\n")
   global driver
   chrome_options = Options()
   chrome_options.add_argument('--no-sandbox')                                                                                                    # 解决DevToolsActivePort文件不存在的报错
   chrome_options.add_argument('--headless')
   chrome_options.add_argument('--disable-gpu')
   chrome_options.add_argument('blink-settings=imagesEnabled=false')                                                                   # 不加载图片，提升运行速度
   chrome_options.binary_location = r"C:\Users\SchoolWebLogin\ChromeCore\App\Chrome-bin\chrome.exe"                                             # 指定使用的浏览器位置
   driver = webdriver.Chrome(executable_path=r"C:\Users\SchoolWebLogin\ChromeCore\Driver\win32\chromedriver.exe",chrome_options=chrome_options) # 导入 Driver路径 与 相关启动配置参数
 
# 有UI模式
def GUI():
    print("SYSETM: Running With GUI ...\n")
    global driver
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')                                                                                                    # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('blink-settings=imagesEnabled=false')                                                                   # 不加载图片，提升运行速度
    chrome_options.binary_location = r"C:\Users\SchoolWebLogin\ChromeCore\App\Chrome-bin\chrome.exe"                                             # 指定使用的浏览器位置
    driver = webdriver.Chrome(executable_path=r"C:\Users\SchoolWebLogin\ChromeCore\Driver\win32\chromedriver.exe",chrome_options=chrome_options) # 导入 Driver路径 与 相关启动配置参数

ISBN = "9787121342387"                             # 需要检索书籍的ISBN号
#ISBN = "12312345678987"                           # 错误的检索空书籍的ISBN号



# 选择是否能看到有可视化的操作：Console(控制台模式) 或 GUI(图形化操作界面)

if __name__ == '__main__':
    Console()
    #GUI()

driver.maximize_window()                                                            # 最大化浏览器
driver.get("http://lib.ccbupt.cn/")                                                   # 通过get()方法，打开一个url站点
driver.implicitly_wait(5)                                                           # 设置隐式等待最长时间5s
#driver.refresh()
#driver.implicitly_wait(5)                                                           # 设置隐式等待最长时间5s

try:
    driver.find_element_by_id('NewBaseScarch_TxtKay').send_keys(ISBN)
    driver.implicitly_wait(5)                                                           # 设置隐式等待最长时间5s
    driver.find_element_by_xpath('//*[@id="NewBaseScarch_CbbSacrchKay"]/tbody/tr/td[5]/label').click()
    driver.implicitly_wait(5)                                                           # 设置隐式等待最长时间5s
    driver.find_element_by_xpath('//*[@id="NewBaseScarch_BtnSarch"]').click()
    driver.implicitly_wait(1)                                                           # 设置隐式等待最长时间1s
    text = driver.find_element_by_xpath('//*[@id="scarchlist"]/div/h4').text
    print ("\n返回消息：",text)
    driver.quit()
except:
    text = driver.find_element_by_xpath('//*[@id="GoldTableView1"]/tbody/tr[2]/td[2]/a').text
    print ("\n已检索到此书：",text)
    driver.quit()

