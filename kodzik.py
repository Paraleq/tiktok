from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def zaloguj_do_tiktok(username, password):
    opcje = webdriver.ChromeOptions()
    opcje.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opcje)

    driver.get('https://www.tiktok.com/login')

    time.sleep(3)

    pole_username = driver.find_element(By.NAME, 'username')
    pole_password = driver.find_element(By.NAME, 'password')

    pole_username.send_keys(username)
    pole_password.send_keys(password)
    pole_password.send_keys(Keys.RETURN)

    return driver

def polub_i_skomentuj(driver, video_url, komentarz):
    driver.get(video_url)

    time.sleep(3)

    przycisk_like = driver.find_element(By.XPATH, '//span[@data-e2e="like-icon"]')
    przycisk_like.click()

    time.sleep(1)

    pole_komentarza = driver.find_element(By.XPATH, '//textarea[@placeholder="Add a comment..."]')
    pole_komentarza.send_keys(komentarz)
    pole_komentarza.send_keys(Keys.RETURN)

    time.sleep(2)

def sprawdz_nowe_posty(driver, url_profilu, komentarz):
    driver.get(url_profilu)

    time.sleep(5)

    elementy_video = driver.find_elements(By.XPATH, '//a[contains(@href, "/video/")]')
    linki_video = [element.get_attribute('href') for element in elementy_video]

    for video_url in linki_video:
        polub_i_skomentuj(driver, video_url, komentarz)

def main():
    username = 'TIKTOK_USERNAME'
    password = 'TIKTOK_PASSWORD'
    url_profilu = 'https://www.tiktok.com/@NAZWA_PROFILU'
    komentarz = 'Super filmik!'

    driver = zaloguj_do_tiktok(username, password)

    sprawdz_nowe_posty(driver, url_profilu, komentarz)

    driver.quit()

if __name__ == '__main__':
    main()
