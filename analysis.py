import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#변수 초기화
id = "sc8556"
pw = "#jaehee0536"
url = "https://bigdata.sbiz.or.kr/?#/hotplace/gisDetail"
address = "서울시 마포구 망원1동"

driver = webdriver.Chrome() #드라이버 객체 정의
driver.get(url) # 웹 페이지 실행
driver.maximize_window() # 창 최대화
driver.implicitly_wait(20) # 암시적인 대기 20초

# 로그인 작업에서 필요한 객체 정의
login_popup_btn = driver.find_element(By.XPATH,"//span[text()='확인']")
# 로그인 팝업창 확인 및 처리 -> 데이터 분석 url로 바로 접근할 경우 '로그인이 필요한 서비스입니다.' 창 발생 -> 확인 클릭 시 로그인화면으로 이동
if login_popup_btn.is_displayed():
    print("'로그인이 필요한 서비스입니다.' 알림창 확인!!")
    login_popup_btn.click()
else:
    print("'로그인이 필요한 서비스입니다.' 알림창 확인 실패로 업무 종료")
    exit


try:
    driver.find_element(By.XPATH,"//input[@title='아이디']").send_keys(id)
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@title='비밀번호']").send_keys(pw)
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[text()='로그인']").click()
    time.sleep(10)
except Exception as e:
    print(f'오류 발생: {e}')
    exit
try:
    driver.switch_to.frame('iframe')
    driver.find_element(By.XPATH, "//input[@id = 'searchAddress']").click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, "//input[@id = 'searchAddress']").send_keys(address)
    time.sleep(1.5)
    driver.find_element(By.XPATH, "//input[@id = 'searchAddress']").send_keys(Keys.ENTER)
    time.sleep(1.5)
    driver.find_element(By.XPATH,"//ul[@id='admListAddress']/li[1]/button").click()
    time.sleep(1.5)
    driver.find_element(By.XPATH,"//i[@class='food']").click()
    time.sleep(1.5)
    driver.find_element(By.XPATH,"//table[@class='childDiv']/tr[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@id='analysisBtn']").click()
    time.sleep(10)
    
except Exception as e:
    print(f'오류 발생: {e}')
    exit