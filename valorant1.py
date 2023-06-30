import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)



driver.get("https://docs.henrikdev.xyz/valorant.html")
select_element=driver.find_element(By.ID,"SelectMMR")
select=Select(select_element)
select.select_by_visible_text("ap")
driver.find_element(By.ID,"MMRName").send_keys("KHANA")
driver.find_element(By.ID,"MMRTag").send_keys("PYAR")
driver.find_element(By.ID,"buttonmmr").click()

time.sleep(3)
text=driver.find_element(By.ID,"mmrresponse").text
print(text)





