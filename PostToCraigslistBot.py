# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:34:53 2020

@author: smadden
"""
# Download chrome web driver

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
import os.path

#function determines if images are found and appends them to a list to upload to craiglist
def find(browser):
    add_images = browser.find_element_by_xpath('//input[@name="file"]')
    if add_images:
        return add_images
    else:
        return False
        
#initiate browser's webdriver (a must for selenium... download the appropriate webbrowser driver from selenium website and save the driver in your project folder)       
browser = webdriver.Chrome('C:\\yourPathToWebdriver\\chromedriver')

#open browser to craigslist
browser.get('https://post.craigslist.org/')

#select location
browser.find_element_by_class_name('ui-selectmenu-text').click()
browser.find_element_by_xpath('//li[@id="ui-id-541"]').click() #this location id is for san diego
browser.find_element_by_xpath('//button[@name="go"]').click()

#select what to sell
browser.find_element_by_xpath('//input[@name="n" and @value="1"]').click()
browser.find_element_by_xpath('//input[@name="id" and @value="fso"]').click() #this is for sale by owner
browser.find_element_by_xpath('//input[@name="id" and @value="93"]').click() #this is for sporting

#describe what your are selling
title_area = browser.find_element_by_xpath('//input[@name="PostingTitle" and @id="PostingTitle"]')
title_area.send_keys('TitleOfWhatYouAreSelling')

price_area = browser.find_element_by_xpath('//input[@name="price"]')
price_area.send_keys('100') #price of what you are selling

geo_area = browser.find_element_by_xpath('//input[@name="geographic_area" and @id="geographic_area"]')
geo_area.send_keys('PB') #neighborhood of where you are selling

postal_code = browser.find_element_by_xpath('//input[@name="postal"]')
postal_code.send_keys(92109) #zip code of where you are selling

description = browser.find_element_by_xpath('//textarea[@name="PostingBody" and @id="PostingBody"]')
description.send_keys("description of what you are selling")
description.send_keys(Keys.ENTER)
description.send_keys(Keys.ENTER)
description.send_keys('If interested contact:')
description.send_keys(Keys.ENTER)
description.send_keys("your telephone number")


dimensions = browser.find_element_by_xpath('//input[@name="sale_size"]')
dimensions.send_keys('dimensions of what you are selling')

email = browser.find_element_by_xpath('//input[@name="FromEMail"]')
email.send_keys('youremail@gmail.com')

browser.find_element_by_xpath('//button[@name="go"]').click()
time.sleep(2)

browser.find_element_by_xpath('//button[@class="continue bigbutton"]').click()

#Upload photos with classic mode
browser.find_element_by_xpath('//a[@id="classic"]').click()
add_images = browser.find_element_by_xpath('//input[@name="file"]')

img = []
path ='C:\\pathToYourItemsPhotos\\Photos\\'
valid_image = ['.jpg', '.tif', '.png']
for i in os.listdir(path):
    print(i)
    img.append(path+i)
    
for f in img:
    add_images.send_keys(f)
    add_images= WebDriverWait(browser, 3).until(find)
    
browser.find_element_by_xpath('//button[@value="Done with Images"]').click()
time.sleep(2)

#submit post
browser.find_element_by_xpath('//button[@value="Continue"]').click()
   
    
    
