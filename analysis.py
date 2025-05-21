import time
import pyautogui
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
    time.sleep(3)
    login_popup_btn.click()
else:
    print("'로그인이 필요한 서비스입니다.' 알림창 확인 실패로 업무 종료")
    exit()

try:
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@title='아이디']").send_keys(id)
    driver.find_element(By.XPATH,"//input[@title='비밀번호']").send_keys(pw)
    driver.find_element(By.XPATH,"//button[text()='로그인']").click()

except Exception as e:
    print(f'오류 발생: {e}')
    exit

try:
    time.sleep(5)
    driver.switch_to.frame('iframe')
    driver.find_element(By.XPATH, "//input[@id = 'searchAddress']").click() #주소 입력창 활성화
    driver.find_element(By.XPATH, "//input[@id = 'searchAddress']").send_keys(address) #주소 입력
    driver.find_element(By.XPATH, "//input[@id = 'searchAddress']").send_keys(Keys.ENTER) #엔터키
    driver.find_element(By.XPATH,"//ul[@id='admListAddress']/li[1]/button").click() #첫 번째 항목 클릭
    driver.find_element(By.XPATH,"//i[@class='food']").click() #음식 클릭
    driver.find_element(By.XPATH,"//table[@class='childDiv']/tr[1]").click() #카페 클릭
    driver.find_element(By.XPATH,"//button[@class='mapFunBtn redrawBtn2 radius show']").click() #반경 클릭
    driver.find_element(By.XPATH,"//button[@value='300']").click() #300M 클릭
    driver.find_element(By.XPATH,"//button[text()='확인']").click() #확인 클릭

    driver.find_element(By.XPATH,"//button[@id='analysisBtn']").click() #분석하기 클릭
    time.sleep(5)

    driver.find_element(By.XPATH,"//button[@class='btn large bg customPoint04 img imgL print']").click() #출력 클릭
    driver.implicitly_wait(300)

    # driver.switch_to.window(driver.window_handles[1]) #새 창 포커스 이동
    # driver.implicitly_wait(300)
    
    # driver.find_element(By.XPATH,"//input[@title='저장']").click() #저장 디스크 이미지 클릭
    time.sleep(3)
    pyautogui.click(x=34, y=156)
    time.sleep(3)
    # driver.find_element(By.XPATH,"//button[text()='확인']").click() #확인 클릭
    # time.sleep(10)
    pyautogui.click(x=1014, y=680)
    time.sleep(10)

    driver.quit()

except Exception as e:
    print(f'오류 발생: {e}')
    exit