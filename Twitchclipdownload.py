from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.twitch.tv/jerma985/clip/EnticingBoringLarkNotATK?filter=clips&range=7d&sort=time") #특정 클립 링크

time.sleep(3)

#video 태그 확인
url_element = driver.find_element_by_tag_name('video')
vid_url = url_element.get_attribute('src')
print(vid_url)