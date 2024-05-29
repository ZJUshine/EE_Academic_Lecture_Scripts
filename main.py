from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 这里填入你的浙大通行证账号和密码
id_number = ""
password = ""

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# 讲座网站
link1 = "http://ee.app.zju.edu.cn/sztz/"
driver.get(link1)

# 选择浙大通行证登录
driver.find_element(By.XPATH, "/html/body/div/div/form/div[2]").click()
# 输入账号密码
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div/div[2]/div/div[1]/form/div[1]/div/input[1]").send_keys(id_number)
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div/div[2]/div/div[1]/form/div[2]/div/input").send_keys(password)
# 登录
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div/div[2]/div/div[1]/form/div[4]/div[1]").click()
# 进入讲座列表
element_huodongliebiao = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div[1]/div/ul/div[1]/li/ul/a[3]")))
element_huodongliebiao.click()
# 按时间先后顺序排序
element_paixu = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/section/div/div[3]/div[2]/table/thead/tr/th[4]/div/span/i[2]")))
element_paixu.click()
# 获取最新的讲座时间
element_huodongshijain = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[4]")))
time_start = element_huodongshijain.text
time_start = time_start + ":00"
print("报名时间：",time_start)

while True:
    # 获取当前时间
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(time_now,time_start)
    if time_now == time_start:
        break


try:
    element_baoming = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[8]/div/button")))
    element_baoming.click()
    element_sure = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[3]/button[2]")))
    element_sure.click()
    print("成功...")
except:
    print("失败...")
    pass