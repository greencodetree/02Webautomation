from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
#print(len(btns)) 총 버튼의 갯수

#print(btns[0].text) 첫번째 버튼 text 프린트

for btn in btns:
    if btn.text=="1":
        btn.click()     #btn text가 1일시 클릭