import requests
import re
import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
import codecs
import json

def print_Reviews(url):
    pass



product_url= "http://www.flipkart.com/moto-g-2nd-generation/p/itme7ybangawqzzx?q=Moto+G+%282nd+Generation%29&as=on&as-show=on&otracker=start&as-pos=p_1_moto+g&pid=MOBDYGZ6SHNB7RFC"
driver = webdriver.Chrome()
driver.get(product_url)


#<input name="username" type="text" />
#"//input[@name='username']")
#<span itemprop="reviewCount">8,593</span>
reviews_count = driver.find_element_by_xpath("//span[@itemprop='reviewCount']")

print "Total reviews are %s" % reviews_count.text

outputFile = codecs.open("reviewsFile.txt",'w','utf-8')
#outputFile.write("Total reviews are %s" % reviews_count.text + "\n")

element = driver.find_element_by_link_text("Show ALL")

review_url = element.get_attribute("href")
driver.get(review_url)

print review_url
count = 1
condn = True
data={}
data["reviews"]=[]

while condn:
    if count > 1000:
        condn = False
    review_texts = driver.find_elements_by_class_name("review-text")
    for review_text in review_texts:
        print "####Review %s" % count
        print review_text.text
        review={}
        review["count"]=count
        review["desc"]=review_text.text
        #outputFile.write("\n\nReview %s" %count + "\n" + review_text.text + "\n\n")
        data["reviews"].append(review)
        count = count + 1
    prev_next_pages = driver.find_elements_by_class_name("nav_bar_next_prev")

    for page in prev_next_pages:
        text = page.text.encode("ascii",errors="ignore")
        if "Next" in text:
            nextpage_url = page.get_attribute("href")

    driver.get(nextpage_url)
    print "\n\n\n"+ nextpage_url + "\n\n\n"
outputFile.write(json.dumps(data,indent=4))
print "%s reviews printed" % count
outputFile.close()
