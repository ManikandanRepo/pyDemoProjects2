import sys
import time

import selenium
from selenium import webdriver


def test_lambdatest_todo_app():
    try:
        Chrome_driver = webdriver.Chrome(r"D:\User\masrinivasan\Downloads\chromedriver.exe")
        Chrome_driver.get("https://lambdatest.github.io/sample-todo-app/")
        Chrome_driver.maximize_window()
        Chrome_driver.find_element('name', 'li1').click()
        time.sleep(2)
        Chrome_driver.find_element('name', 'li2').click()
        time.sleep(2)
        title = "Sample page - lambdatest.com"
        assert title == Chrome_driver.title
        sample_text = "Happy Testing!"
        email_text_field = Chrome_driver.find_element('id', 'sampletodotext')
        email_text_field.send_keys(sample_text)
        time.sleep(2)
        Chrome_driver.find_element('id', 'addbutton').click()
        time.sleep(5)
        new_label = Chrome_driver.find_element('name', 'li6').text
        print('new label is:' + new_label)
        sys.stderr.write(new_label)
        #assert sample_text == str(new_label)
    finally:
        Chrome_driver.quit()
