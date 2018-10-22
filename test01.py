#-*- coding: utf-8 -*-
from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os



def test01(driver, url):
    driver.get(url)
    assert url == driver.current_url , "fail"


