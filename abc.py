from lxml import html
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv


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
            break
        i+=1
        #break
