import json
import time
import csv
import pandas 
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

#driver initiation


options=Options()
options.add_experimental_option("detach",True)
options.add_argument("--headless=new")
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)





#interactive terminal commands

file=open("valhistory1.json",'a+')
print("Welcome to valorant profile finder.")
print()
print("\n\n")
print("Please choose your region(1/2/3/4) or retrieve player data from file")

print("\n\n")
print("1.APAC\n2.Europe\n3.North America \n4.Retrieve the last player's data")

#csv file writer and opener modules
def csvwrite(listobj):
    with open('valhistory1.json', 'w') as file:
        json.dump(listobj,file,indent=2)
        

def csvread(listobj):
    
    with open('valhistory1.json','r') as file:
        listobj=json.load(file)
    
    return listobj
       
#browser driver definition here


def valdriver(usern,usert,reg):

    driver.get("https://docs.henrikdev.xyz/valorant.html")
    select_element=driver.find_element(By.ID,"SelectMMR")
    select=Select(select_element)

    #fetch elements from the API
    select.select_by_visible_text(reg)
    driver.find_element(By.ID,"MMRName").send_keys(usern)
    driver.find_element(By.ID,"MMRTag").send_keys(usert)
    driver.find_element(By.ID,"buttonmmr").click()

    time.sleep(3)
    text=driver.find_element(By.ID,"mmrresponse").text

    return text



### after-API interactive terminal definition


def datasave():
    print("Player data can be stored so that it does not have to be searched repeatedly")
    print("Do you want to save this players data?  Y/N")


    response=str(input())
    if response=="Y":
        csvwrite([username,usertag,region])
   

    else:
        print("Invalid response")
      





#terminal interaction definition


choice=int(input())
if choice==1:
    region="ap"
    username=str(input("Enter the username of the player. (the part of the id that comes before the # eg SillyGooose  in SillyGooose#4078): "))
    usertag=str(input("Please enter the tag of the player( the part of the id that comes after # eg: SillyGooose#4078)"))
    text=valdriver(username,usertag,region)
   
    print(text)
    datasave()

elif choice==2:
    region="eu"
    username=str(input("Enter the username of the player. (the part of the id that comes before the # eg SillyGooose  in SillyGooose#4078): "))
    usertag=str(input("Please enter the tag of the player( the part of the id that comes after # eg: SillyGooose#4078)"))
    text=(valdriver(username,usertag,region))
    print(text)
    datasave()

elif choice==3:
    region="na"
    username=str(input("Enter the username of the player(the part of the id that comes before the # eg SillyGooose  in SillyGooose#4078): "))
    usertag=str(input("Please enter the tag of the player( the part of the id that comes after # eg: SillyGooose#4078)"))
    text=valdriver(username,usertag,region)
    print(text)
    datasave()

elif choice==4:
    newlist=[]
    newlist=csvread(newlist)
    print(valdriver(newlist[0],newlist[1],newlist[2]))
   

else:
    raise(ValueError("Please enter the correct value type."))
  
