from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)

#btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
#print(len(btns)) 총 버튼의 갯수

#print(btns[0].text) 첫번째 버튼 text 프린트

#전역변수
#현재 찾아야될 숫자
num = 1
def clickBtn():
    global num  #전역변수
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

    for btn in btns:
        if btn.text==str(num):
            btn.click()
            print(True)
            num+=1
            return

##메인코드
while num<=50:
    clickBtn()