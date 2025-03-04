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
# 点击登陆
denglu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[2]/form/button")))
denglu.click()
# 输入账号密码
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div/div[2]/div/div[1]/form/div[1]/div/input[1]").send_keys(id_number)
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div/div[2]/div/div[1]/form/div[2]/div/input").send_keys(password)
# 登录
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/div/div[2]/div/div[1]/form/div[4]/div[1]").click()
# 点击学术活动
xueshuhuodong = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/aside/div/div[1]/ul/li[2]/div/span/div")))
xueshuhuodong.click()

# 点击活动列表
huodongliebiao = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/aside/div/div[1]/ul/li[2]/ul/li[1]/span/a")))
huodongliebiao.click()

# 获取最新的讲座时间
element_huodongshijain = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/main/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[4]")))
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
    element_baoming = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/main/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[8]/div/button/span")))
    element_baoming.click()
    
    # 等待并点击确定按钮
    element_sure = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='dialog']//button[contains(., '确定')]")
        )
    )
    element_sure.click()
    print("成功...")
except Exception as e:
    print("失败:", str(e))