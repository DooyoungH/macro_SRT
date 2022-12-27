# -*- coding: utf-8 -*-

import os
import sys
import datetime
from time import sleep
from random import randint
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import pygame
pygame.init()

pygame.mixer.music.load("21*.MP3")


dpt_locs = {'동탄' :3 ,'동대구':9 , '울산':11, '수서':2, '천안아산':5, '부산':12, '대전': 7}
avl_locs = {'동탄':21, '동대구':27, '수서':20, '울산':29, '부산':30, '천안아산':23}
time_table = {'6시': 40, '16시': 180000}

def open_browser():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome("/Users/ryumei/Downloads/chromedriver", chrome_options=options)
    return driver

def run():
    driver = open_browser()
    driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')
    driver.implicitly_wait(15)
    driver.find_element_by_id('srchDvNm01').send_keys("2287793934")
    driver.find_element_by_id('hmpgPwdCphd01').send_keys("DiendS2Listen!")
    driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()
    driver.implicitly_wait(4)
    sleep(0.4)
    #driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/div[1]/a').click()
    #driver.implicitly_wait(1)
    #driver.find_element_by_id("ui-id-{}".format(dpt_locs[dpt])).click()
    #sleep(0.4)
    #driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/div[2]/a').click()
    #driver.implicitly_wait(1)
    #driver.find_element_by_id("ui-id-{}".format(avl_locs[avl])).click()
    date_ele = driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/div[3]/div/input[1]')
    driver.execute_script("arguments[0].setAttribute('value','{}')".format(dpt_date), date_ele)
    #driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/div[4]/a').click()
    #driver.find_element_by_id("ui-id-{}".format(time_table[when])).click()
    #sleep(0.4)
    driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/a').click()
    driver.implicitly_wait(4)
    sleep(0.4)

    counter = 1
    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        trlist = soup.select('#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr')  # [tr,tr,tr,....]
        
        index=0
        done=False

        for tdl in trlist:
            if done == False:
                index += 1
                for train_no in train_nums:  
                    if tdl.select('.trnNo')[0].text.strip() == str(train_no):    
                        if '예약하기' in tdl.select("td")[6].find_all(text='예약하기'):
                            t = "#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child("+str(index)+") > td:nth-child(7) > a"
                            driver.find_element_by_css_selector(t).click()
                            print("예약완료------------------------------------------------------------")
                            
                            while(True):
                                pygame.mixer.music.play()
                                sleep(5)
                                
                            done=True
                            break
                        else:
                            sleep(0.1)
            else:
                break


        print("loop done. counter : {}".format(counter))
        sleep(randint(5,10))
        
        if done == False:        
            elm = driver.find_element_by_xpath('//*[@id="search_top_tag"]/input')
            driver.execute_script("arguments[0].click();", elm)
            driver.implicitly_wait(2)    
            counter += 1
        else:
            driver.quit()
            break    

        if counter > 9999:
            bot.sendMessage(chat_id=chat_id, text="9999바퀴 돌았습니다. 자동 종료")
            driver.quit()
            break

if __name__ == "__main__":
    dpt = input("출발지 입력 (ex 동탄, 울산, 동대구, 수서, 천안아산) : ")
    avl = input("도착지 입력 : ")
    dpt_date = input("날짜 입력. 반드시 2019.12.31 형태 : ")
    when = input("6시 or 16시 둘중 하나 : ")
    train_nums = list(map(int,input("기차 번호 입력 스페이스바로 구분 : ").strip().split()))   
    run()