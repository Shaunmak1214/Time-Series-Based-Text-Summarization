from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# Topics: Locate a button, select element within dropdown and extract data from a table

# define the website to scrape and path where the chromediver is located
website = 'https://stackoverflow.com/questions/51861577/python-list-function-or-list-comprehension'
path = '/usr/local/bin/chromedriver' # write the path here

op = webdriver.ChromeOptions()
op.add_argument('headless')
# define 'driver' variable
driver = webdriver.Chrome(path, options=op)
# open Google Chrome with chromedriver
driver.get(website)

# locate a button
all_comments_button = driver.find_element_by_xpath('//*[@id="comments-link-51861577"]/a[2]')
# print(all_comments_button)
# click on a button
# all_comments_button.click()
# time.sleep(2)

comment_list = driver.find_element_by_css_selector('.post-layout--right > .comments > ul')
comments = comment_list.find_elements_by_tag_name("li")

all_comments = []

for comment in comments:
    # find the username
    data = comment.find_element_by_css_selector('.js-comment-text-and-form > .comment-body')
    comment_text = data.find_element_by_css_selector(".comment-copy").text 
    comment_username = data.find_element_by_css_selector(".comment-user").text 
    comment_date_time = data.find_element_by_css_selector(".comment-date > .comment-link > span").text 
    
    # construct a dictionary
    comment_dict = {
        'comment_username': comment_username,
        'comment_text': comment_text,
        'comment_date_time': comment_date_time
    }
    all_comments.append(comment_dict)

# select dropdown and select element inside by visible text
# dropdown = Select(box.find_element_by_id('country'))
# dropdown.select_by_visible_text('Spain')
driver.quit()
df = pd.DataFrame.from_dict(all_comments)
df.to_csv('comments.csv')

print("{} comments saved to csv".format(len(all_comments)))