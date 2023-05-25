from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=Options()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://web.whatsapp.com/")




