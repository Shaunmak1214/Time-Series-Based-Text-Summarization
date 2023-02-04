from ctypes import POINTER
from exceptiongroup import catch
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time
import requests
import json 
import undetected_chromedriver as uc

def get_data(link, postIdx):
    print('Getting data for post: ', postIdx, ' with link: ', link)
    driver.get(link)
    time.sleep(5)
    
    try:
      all_comments = []
      
      post_idx = link.split('/')[4]
      post_title = driver.find_element(By.CSS_SELECTOR, "#question-header > h1 > .question-hyperlink").text
      post_body = driver.find_element(By.CSS_SELECTOR, ".question .post-layout--right > .s-prose.js-post-body").get_attribute('innerHTML')
      post_date = driver.find_element(By.CSS_SELECTOR, '.d-flex.fw-wrap.pb8.mb16.bb.bc-black-075 > .flex--item.ws-nowrap.mr16.mb8').get_attribute('title'),
      post_votecounts = driver.find_element(By.CSS_SELECTOR, '.question .post-layout--left .js-vote-count').text,
      
      ''' SAVING THE POST ITSELF '''
      post_dict = {
        'post_idx': post_idx,
        'post_link': link,
        'post_title': post_title,
        'post_body': post_body,
        'post_date': post_date,
        'post_votecounts': post_votecounts,
        
        'comment_idx': '',
        'comment_score': '',
        'comment_username': '',
        'comment_text': '',
        'comment_date_time': '',
        
        'answer_idx': '',
        'answer_text': '',
        'answer_body': '',
        'answer_date_time': '',
        'answer_votecounts': '',
        
        'answer_cmt_idx': '',
        'answer_cmt_text': '',
        'answer_cmt_body': '',
        'answer_cmt_date_time': '',
        'answer_cmt_votecounts': '',  
        
        'type': 'post'
      }
      all_comments.append(post_dict)
      
      ''' SAVING ALL THE POST COMMENTS '''
      comment_list = driver.find_element(By.CSS_SELECTOR, '.question .post-layout--right > .comments > ul')
      comments = comment_list.find_elements(By.TAG_NAME, "li")
      for comment in comments:
        # find the username
        data = comment.find_element(By.CSS_SELECTOR, '.js-comment-text-and-form > .comment-body')
        comment_score  = comment.find_element(By.CSS_SELECTOR, ".comment-score").text
        comment_text = data.find_element(By.CSS_SELECTOR, ".comment-copy").text
        comment_body = data.find_element(By.CSS_SELECTOR, ".comment-copy").get_attribute('innerHTML')
        comment_username = data.find_element(By.CSS_SELECTOR, ".comment-user").text
        comment_date_time = data.find_element(By.CSS_SELECTOR, ".comment-date > .comment-link > span").get_attribute('title')
        
        # construct a dictionary
        comment_dict = {
            'post_idx': post_idx,
            'post_link': link,
            'post_title': post_title,
            'post_body': post_body,
            'post_date': post_date,
            'post_votecounts': post_votecounts,
            
            'comment_idx': comment.get_attribute('id'),
            'comment_score':comment_score,
            'comment_username': comment_username,
            'comment_text': comment_body,
            'comment_date_time': comment_date_time,
            
            'answer_idx': '',
            'answer_text': '',
            'answer_body': '',
            'answer_date_time': '',
            'answer_votecounts': '',
            
            'answer_cmt_idx': '',
            'answer_cmt_text': '',
            'answer_cmt_body': '',
            'answer_cmt_date_time': '',
            'answer_cmt_votecounts': '',
            
            'type': 'post_comment'
        }
        all_comments.append(comment_dict)

      try:
        answers_dirty = driver.find_elements(By.CSS_SELECTOR, '.answer.js-answer')
        print("{} of answers found".format(len(answers_dirty)))
        for answer in answers_dirty:
          answer_text = answer.find_element(By.CSS_SELECTOR, '.s-prose.js-post-body').text
          answer_date_time = answer.find_element(By.CSS_SELECTOR, ".comment-date > .comment-link > span").get_attribute('title')
          answer_body = answer.find_element(By.CSS_SELECTOR, '.s-prose.js-post-body').get_attribute('innerHTML'),
          answer_votecounts  = answer.find_element(By.CSS_SELECTOR, '.post-layout--left .js-vote-count').text,
          
          ''' SAVE THE ANSWER '''
          comment_dict = {
            'post_idx':post_idx,
            'post_link': link,
            'post_title': post_title,
            'post_body': post_body,
            'post_date': post_date,
            'post_votecounts': post_votecounts,
            
            'comment_idx': '',
            'comment_score': '',
            'comment_username': '',
            'comment_text': '',
            'comment_date_time': '',
            
            'answer_idx': answer.get_attribute('id').split('-')[1],
            'answer_text': answer_text,
            'answer_body': answer_body, 
            'answer_date_time': answer_date_time,
            'answer_votecounts': answer_votecounts,
            
            'answer_cmt_idx': '',
            'answer_cmt_text': '',
            'answer_cmt_body': '',
            'answer_cmt_date_time': '',
            'answer_cmt_votecounts': '',
            
            'type': 'answer'
          }
          all_comments.append(comment_dict)
          
          
          ''' SAVE THE ANSWER COMMENTS '''
          answer_comments = answer.find_elements(By.CSS_SELECTOR, '.post-layout--right .comments > ul > li')
          for comment in answer_comments:
            
            answer_cmt_idx = comment.get_attribute('id').split('-')[1],
            answer_cmt_data = comment.find_element(By.CSS_SELECTOR, '.js-comment-text-and-form > .comment-body')
            answer_cmt_text = answer_cmt_data.find_element(By.CSS_SELECTOR, ".comment-copy").text
            answer_cmt_date_time = answer_cmt_data.find_element(By.CSS_SELECTOR, ".comment-date > .comment-link > span").text
            answer_cmt_body  = comment.find_element(By.CSS_SELECTOR, '.js-comment-text-and-form > .comment-body').get_attribute('innerHTML'),
            answer_cmt_votecounts = comment.find_element(By.CSS_SELECTOR, '.js-comment-actions.comment-actions > .comment-score').text,
            
            comment_dict = {
                'post_idx': post_idx,
                'post_link': link,
                'post_title': post_title,
                'post_body': post_body,
                'post_date': post_date,
                'post_votecounts': post_votecounts,
                
                'comment_idx': '',
                'comment_score': '',
                'comment_username': '',
                'comment_text': '',
                'comment_date_time': '',
                
                'answer_idx': answer.get_attribute('id').split('-')[1],
                'answer_text': answer_text,
                'answer_body': answer_body, 
                'answer_date_time': answer_date_time,
                'answer_votecounts': answer_votecounts,
                
                'answer_cmt_idx': answer_cmt_idx,
                'answer_cmt_text': answer_cmt_text,
                'answer_cmt_body': answer_cmt_body,
                'answer_cmt_date_time': answer_cmt_date_time,
                'answer_cmt_votecounts': answer_cmt_votecounts,
                
                'type': 'answer_comment'
            }
            all_comments.append(comment_dict)

      except Exception as e:
        print('Error in handling answers: ', e)
        pass

      print(len(all_comments))
      df = pd.DataFrame.from_records(all_comments)
      df.to_csv('./archive/react-useeffect-final.csv', mode="a", index=False, header=False)

      print("{} comments saved to csv for index {} and link {} ".format(len(all_comments), postIdx, link))

    except Exception as e:
      print(e)
      print("Rate limited")

if __name__ == '__main__': 
  op = webdriver.ChromeOptions()
  op.add_argument('--disable-popup-blocking') 
  op.add_argument('--headless')
  op.add_argument('--incognito')
  path = '/usr/local/bin/chromedriver' # write the path here
  driver = uc.Chrome(executable_path=path, options=op, version_main=108)
  
  for i in range(1, 10):
    print("Scrapping page number: ", i)
    api_link = 'https://api.stackexchange.com/2.3/search?order=desc&sort=activity&site=stackoverflow&key=MkldPoI*EBSwcLnfwW3iQw((&intitle=react%20useeffect&page={page}&pagesize=100';
    # https://api.stackexchange.com/2.3/search?order=desc&sort=activity&site=stackoverflow&key=MkldPoI*EBSwcLnfwW3iQw((&intitle=centering%20a%20div&page=3&pagesize=100
    api_link = api_link.format(page=i)
    res = requests.get(api_link)
    response = json.loads(res.text)
    links = [i['link'] for i in response['items']]
    
    for idx, link in enumerate(links):
      get_data(link, idx)
      print("Scrapping page number: ", i)

  driver.quit();