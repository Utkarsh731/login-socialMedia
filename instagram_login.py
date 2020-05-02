from selenium import webdriver
from time import sleep
def bot(username,password):
    driver=webdriver.Chrome("driverPath")
    driver.get("https://www.instagram.com/")
    # driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[2]/p/a").click()
    sleep(10)
    #driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
    sleep(2)
    driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
    driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(4)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    sleep(2)
bot("username","password")
