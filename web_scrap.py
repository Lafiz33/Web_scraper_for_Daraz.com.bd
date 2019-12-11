# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import time
print("*"*60)
print("WEB_SCRAP_v1.0.3_By__Lafiz33 \nthis is a test program.. \nFirst input is the item you want to search \nSecond input is how many pages you want to traverse")
print("*"*60)

#https://sites.google.com/a/chromium.org/chromedriver/downloads
url= "https://www.daraz.com.bd/"
flag = True
        
        
while(True):
    try:    
        print("1 -- search by item \n2 -- search by link")
        type_of_search=int(input("Enter your choice: \n"))        
        
        if(type_of_search == 1):
            userInput=str(input("Enter Item Name \n\r"))
            flag = True
        
        elif(type_of_search == 2):
            url=str(input("Enter link? \n\r"))
            shop=url.split("/")
            userInput = shop[3]
            print ("seller name : "+userInput)
            flag= False
        else:
            continue
            
        
        
        page_num=int(input("how many pages you want? \n\r"))
        
        print("Opening Web page...")
        
        dir_now=os.path.dirname(os.path.abspath(__file__))
        browser=webdriver.Chrome(executable_path=dir_now+'\\chromedriver.exe')
        
        print("Creating File...")
        if(userInput=="/"):
            filename = "all product.csv"
        else:
            filename = userInput+".csv"
        f = open(filename, "w", encoding="utf-8")
        
        print("Writing Headers...")
        headers= "sku, title, price"
        f.write(headers+ "\n")
        
        for i in range(1,page_num+1) :   
            start_time = time()
            browser.get(url)
            end_time = time()
            print("time took to load : " +str(round(end_time-start_time,5)) +"s")
            
            print("searching for " + str(userInput))
            if (flag):
                elem = browser.find_element_by_name("q")
                elem.send_keys(userInput)
                elem.send_keys(Keys.RETURN)
                flag = False
            print("Page found.. \nmaking soup")
            soup=BeautifulSoup(browser.page_source, "html.parser")
        #    
        #    
        #    #browser.close();
        #    
        #    
            print("finding stuffs that you need...")
            sku_div=soup.findAll("div", class_="c2prKC")
            
            title_div=soup.findAll("div", class_="c16H9d")
            
            price_div=soup.findAll("span", class_="c13VH6")
            
           
        #    
        #    
            print("Found them...")
            
            print("Writing Them for you")
            for j in range (len(sku_div)):
                found_sku = sku_div[j]["data-sku-simple"]
                found_title = title_div[j].a.text
                found_price = price_div[j].text
                
                
            #    print ("sku: "+found_sku+ " title: "+found_title+" price: "+found_price+" \n")
                f.write(found_sku+","+found_title.replace(",","")+","+found_price.replace(",","")+"\n")
            #    .replace(",","_")
            print("Done... ")
            if i!=page_num:
                print("going to next page...")
                nextPage = browser.find_element_by_link_text(str(i+1))
                url=nextPage.get_attribute('href')
                print("found next page")
            
    except:
            print("Something went wrong.. \nSorry.. \nTry again :(")
    finally:
            print("Closing file...")
            f.close()
            print("have fun.. :)")
            if(input("exit? y/n \n")=="y"):
                print("exiting..\nthank you..")
                break
            
            



