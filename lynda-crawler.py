#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib
import time
import json
import csv
import os 

chrome_options = webdriver.ChromeOptions();
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--mute-audio")
# chrome_options.add_argument("--headless")

def validate_filename(filename):
    validate = (':','?','''"''',"|","<",">","!","/");
    for filtering in validate: 
        if(filtering in filename):
            filename = filename.replace(filtering,"");
    return filename;

def download_video(url):
    browser = webdriver.Chrome("./chromedriver.exe",options=chrome_options);
    browser.get("https://www.lynda.com/portal/sip?org=washoecountylibrary.us");
    time.sleep(1);
    username = browser.find_element_by_id("card-number");
    username.send_keys("41235080014175");
    time.sleep(1);
    password = browser.find_element_by_id("card-pin");
    password.send_keys("123456");
    time.sleep(1);
    login = browser.find_element_by_id("library-login-login");
    login.click();
    print("Login");
    time.sleep(1);
    browser.get(url);
    title_element = browser.find_element_by_class_name("default-title");
    folder = title_element.get_attribute("data-course");
    os.mkdir(f"E:/{validate_filename(folder)}");
    course_length = len(browser.find_elements_by_class_name("item-name"));
    print(folder);
    for i in range(0,course_length):
        link = browser.find_elements_by_class_name("item-name")[i];
        video_name = link.get_attribute("innerHTML").strip();
        link.click();
        time.sleep(2);
        video = browser.find_element_by_css_selector(".mejs-mediaelement .player");
        print(video_name);
        video_url = video.get_property("src")
        urllib.request.urlretrieve(video_url, f'E:/{validate_filename(folder)}/{i+1}.{validate_filename(video_name)}.mp4')
        time.sleep(1);
    browser.close();

def download_path(url):
    browser = webdriver.Chrome("./chromedriver.exe",options=chrome_options);
    browser.get("https://www.lynda.com/portal/sip?org=washoecountylibrary.us");
    time.sleep(1);
    username = browser.find_element_by_id("card-number");
    username.send_keys("41235080014175");
    time.sleep(1);
    password = browser.find_element_by_id("card-pin");
    password.send_keys("123456");
    time.sleep(1);
    login = browser.find_element_by_id("library-login-login");
    login.click();
    print("Login");
    time.sleep(1);
    browser.get(url);
    path_length = len(browser.find_elements_by_class_name("card-content"));
    print(f"Path length: {path_length}");
    path_title = browser.find_elements_by_tag_name("h1")[0].get_attribute("innerHTML");
    print(path_title);
    for i in range(0,path_length):
        browser.get(url);
        course = browser.find_elements_by_class_name("card-content")[i];
        course.click();
        time.sleep(2);
        title_element = browser.find_element_by_class_name("default-title");
        folder = title_element.get_attribute("data-course");
        os.mkdir(f"E:/{validate_filename(folder)}");
        course_length = len(browser.find_elements_by_class_name("item-name"));
        print(validate_filename(folder));
        for j in range(0,course_length):
            link = browser.find_elements_by_class_name("item-name")[j];
            video_name = link.get_attribute("innerHTML").strip();
            link.click();
            time.sleep(3);
            video = browser.find_element_by_css_selector(".mejs-mediaelement .player");
            print(video_name);
            video_url = video.get_property("src")
            if(video_url == ""):
                video_url = video.get_attribute("data-src");
                print("Source doesn't load, replace secondary source.")
            urllib.request.urlretrieve(video_url, f'E:/{validate_filename(folder)}/{j+1}.{validate_filename(video_name)}.mp4')
            time.sleep(1);
    browser.close();
    
def download_courses_in_path(url,start,end):
    browser = webdriver.Chrome("./chromedriver.exe",options=chrome_options);
    browser.get("https://www.lynda.com/portal/sip?org=washoecountylibrary.us");
    time.sleep(1);
    username = browser.find_element_by_id("card-number");
    username.send_keys("41235080014175");
    time.sleep(1);
    password = browser.find_element_by_id("card-pin");
    password.send_keys("123456");
    time.sleep(1);
    login = browser.find_element_by_id("library-login-login");
    login.click();
    print("Login");
    time.sleep(1);
    browser.get(url);
    path_length = len(browser.find_elements_by_class_name("card-content"));
    print(f"Path length: {path_length}")
    path_title = browser.find_elements_by_tag_name("h1")[0].get_attribute("innerHTML");
    print(path_title);
    for i in range(start-1,end):
        browser.get(url);
        time.sleep(1);
        course = browser.find_elements_by_class_name("card-content")[i];
        course.click();
        time.sleep(2);
        title_element = browser.find_element_by_class_name("default-title");
        folder = title_element.get_attribute("data-course");
        ## Create course folder
        os.mkdir(f"E:/{validate_filename(folder)}");
        course_length = len(browser.find_elements_by_class_name("item-name"));
        print(validate_filename(folder));
        for j in range(0,course_length):
            link = browser.find_elements_by_class_name("item-name")[j];
            video_name = link.get_attribute("innerHTML").strip();
            link.click();
            time.sleep(2);
            video = browser.find_element_by_css_selector(".mejs-mediaelement .player");
            print(video_name);
            ## Create video file.
            video_url = video.get_property("src");
            if(video_url == ""):
                video_url = video.get_attribute("data-src");
                print("Source doesn't load, replace secondary source.")
            urllib.request.urlretrieve(video_url, f'E:/{validate_filename(folder).strip()}/{j+1}.{validate_filename(video_name).strip()}.mp4')
            time.sleep(1);
    browser.close();

queues = [
    "https://www.lynda.com/learning-paths/Web/become-a-java-ee-7-developer",
    "https://www.lynda.com/learning-paths/Web/become-a-spring-developer",
]
for i in queues:
    download_path(i);
    print("Finish");
download_courses_in_path("https://www.lynda.com/learning-paths/Web/advance-your-spring-developer-skills",1,4);
# 
# download_courses_in_path("https://www.lynda.com/learning-paths/IT/master-sql-for-data-science",3,5);
# print("Finish");
# download_courses_in_path("https://www.lynda.com/learning-paths/IT/become-a-machine-learning-specialist",3,9);
# print("Finish");
# download_courses_in_path("https://www.lynda.com/learning-paths/IT/advance-your-skills-in-deep-learning-and-neural-networks",1,5);
# print("Finish");


# In[5]:


queues = [
    "https://www.lynda.com/course-tutorials/Welcome/503930/569746-4.html",
    "https://www.lynda.com/course-tutorials/Statistics-Fundamentals-Part-3-Advanced/503930-2.html",
    "https://www.lynda.com/Data-Science-tutorials/pandas-Essential-Training/636129-2.html",
    "https://www.lynda.com/NumPy-tutorials/NumPy-Data-Science-Essential-Training/508873-2.html",   
]

for i in queues:
    print(i)

