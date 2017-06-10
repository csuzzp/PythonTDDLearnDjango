#coding = utf-8

from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://localhost:8000')

assert 'Welcome' in browser.title, "Browser title was " + browser.title

#assert 'Django' in browser.tittle

browser.quit()