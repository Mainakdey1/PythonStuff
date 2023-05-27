import time
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


#interactive terminal commands
print("Welcome to valorant profile finder.")
print("Please choose your region(1/2/3/4)")
print("1.APAC\n2.Europe\n3.North America \n4.something")
choice=int(input())
username=str(input("Please enter the username of the player you wish to find. This field is case sensitive"))
tag=str(input("Please enter the tag of this player. Case sensitive as afore mentioned"))

if choice==1:
    region="ap"
elif choice==2:
    region="eu"
elif choice==3:
    region="na"
else:
    print(ValueError.add_note("please enter the correct value(numerical values)"))


#driver initiation
options=Options()
options.add_experimental_option("detach",True)
options.add_argument("--headless=new")
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://docs.henrikdev.xyz/valorant.html")
select_element=driver.find_element(By.ID,"SelectMMR")
select=Select(select_element)

#fetch elements from the API
select.select_by_visible_text(region)
driver.find_element(By.ID,"MMRName").send_keys(username)
driver.find_element(By.ID,"MMRTag").send_keys(tag)
driver.find_element(By.ID,"buttonmmr").click()

time.sleep(3)
text=driver.find_element(By.ID,"mmrresponse").text

print(text)

driver.quit()





