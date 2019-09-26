from lxml import html
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv
import time


response = webdriver.Chrome()
response.get("http://lucky-coyote.w6.wpsandbox.pro/wp-admin/post-new.php?post_type=product")
username = "arehman622"
password = "arehman622"
user = response.find_elements_by_xpath("//input[@id='user_login']")
passw = response.find_elements_by_xpath("//input[@id='user_pass']")
login = response.find_elements_by_xpath("//input[@id='wp-submit']")
user[0].send_keys(username)
passw[0].send_keys(password)
login[0].click()
with open("Ouput_Username.csv", errors='ignore') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    i=0
    prevTitle = "title"
    for row in readCSV:
        if(i!=0):
            response.get("http://lucky-coyote.w6.wpsandbox.pro/wp-admin/post-new.php?post_type=product")
            title = response.find_elements_by_xpath("//input[@id='title']")
            title[0].send_keys(row[2])
            desc = '{}\n<div style="overflow: auto;">\n<table class="shop_attributes">\n<tbody>\n<tr>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n</tr>\n<tr>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n</tr>\n<tr>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n</tr>\n</tbody>\n</table>\n</div>'.format(row[2],row[18],row[19],row[28],row[29],row[30],row[31],row[20],row[21],row[22],row[23],row[32],row[33],row[26],row[27],row[26],row[27],row[34],row[35])
            description = response.find_elements_by_xpath("//textarea[@id='content']")
            description[0].send_keys(desc)
            vendor = Select(response.find_element_by_xpath("//select[@id='dokan_product_author_override']"))
            vendor.select_by_visible_text(row[136])
            category ="//label[text()[contains(.,'{}')]]".format(row[1])
            response.find_elements_by_xpath(category)[0].click()
            img1 = response.find_elements_by_xpath("//input[@id='knawatfibu_url']")
            img1[0].send_keys(row[36])
            response.find_elements_by_xpath("//a[@id='knawatfibu_preview']")[0].click()
            j=0
            idx = 0
            while(row[37+j] and j<99):
                if(j==1):
                    idx = j+2
                    imgpath = "//input[@id='knawatfibu_url{}']".format(idx)
                else:
                    idx = idx+1
                    imgpath = "//input[@id='knawatfibu_url{}']".format(idx)
                time.sleep(0.6)
                response.find_elements_by_xpath(imgpath)[0].send_keys(row[37+j])
                prevPath = "//a[@id='knawatfibu_preview{}']".format(idx)
                response.find_elements_by_xpath(prevPath)[0].click()
                j+=1
            price = response.find_elements_by_xpath("//input[@id='_regular_price']")
            price[0].send_keys(row[15].lstrip("$€£"))
            break
        i+=1
        #break
