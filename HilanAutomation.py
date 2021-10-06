import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import datetime
from PIL import Image

if __name__ == '__main__':
    PATH = "C:\\Program Files (x86)\\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
# insert the login url of the site
    driver.get("hilan login url")
    time.sleep(2)
# (HILAN-ID = your user id) & (HILAN-PASSWORD = your password)
    driver.find_element_by_id("user_nm").send_keys("HILAN-ID")
    driver.find_element_by_id("password_nm").send_keys("HILAN-PASSWORD")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div/div/div[5]/button").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/form/div[3]/div[2]/div[2]/div[2]/ul/li[4]/a").click()
    driver.find_element_by_xpath("/html/body/form/div[3]/div[4]/div/div[3]/div/div/div/div/table/tbody/tr[2]/td[5]/span").click()

    time.sleep(2)
    datetime = datetime.datetime.now()
    print(datetime)
    month = str(datetime.month - 1)
    lest_month = month + "-" + str(datetime.year)
    print(lest_month)
    driver.switch_to.window(driver.window_handles[1])
    driver.fullscreen_window()

    # saveing the hours and converting it to pdf
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('HoursAnalysisInfo_' + lest_month + ".png")
    img_png = 'HoursAnalysisInfo_' + lest_month + ".png"
    img_pdf = 'HoursAnalysisInfo_' + lest_month + ".pdf"
    time.sleep(5)
    driver.quit()

    im = Image.open(img_png)

    # crop the png file
    def crop_center(pil_img, crop_width, crop_height):
        img_width, img_height = pil_img.size
        return pil_img.crop(((img_width - crop_width) // 2,
                             (img_height - crop_height) // 2,
                             (img_width + crop_width) // 2,
                             (img_height + crop_height) // 2))


    im_new = crop_center(im, 1300, 800)
    im_new.save(img_png, quality=95)

    # save as pdf
    im1 = im_new.convert('RGB')
    im1.save(img_pdf)

    driver = webdriver.Chrome(PATH)
    driver.get("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
    time.sleep(5)

    search = driver.find_element_by_name("identifier")
    search.send_keys("USERNAME")  # your Gmail username
    search.send_keys(Keys.RETURN)
    driver.implicitly_wait(4)
    search = driver.find_element_by_name("password")
    search.send_keys("GMAIL-PASSWORD")  # your Gmail password
    time.sleep(3)
    search.send_keys(Keys.RETURN)
    time.sleep(5)

    driver.maximize_window()

    driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div").click()
    time.sleep(3)
    open = driver.find_element_by_name("to")
    open.send_keys("DESTENATION-EMAIL")  # insert Destenation email address
    open = driver.find_element_by_name("subjectbox") 
    open.send_keys("Hours Analysis") 
    time.sleep(1)
    open.send_keys(Keys.TAB)
    time.sleep(1)
    time.sleep(1)

    pyautogui.write("YOUR MESSAGE")     # inser your massage
    time.sleep(1)

    pyautogui.click(310, 1084)
    time.sleep(3)
    pyautogui.write(os.getcwd() + "\\" + img_pdf)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)

    # press send
    pyautogui.click(204, 1088)
    driver.quit()
    
