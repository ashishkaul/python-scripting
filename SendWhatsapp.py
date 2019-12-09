#!/usr/bin/env python3
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

recipients = input('Enter comma separated names of user: ').split(',')
message = input('Enter message: ')

input('Press enter after scanning QR code')


for recipient in recipients:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(recipient.strip()))
    user.click()
    message_box = driver.find_element_by_xpath('//footer//div/div[2]/div')
    message_box.send_keys(message)
    send_button = driver.find_element_by_xpath('//span[@data-icon = "send"]')
    send_button.click()