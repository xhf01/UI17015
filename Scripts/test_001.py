import time

import allure
from selenium import webdriver


class Test:
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")


    @allure.step("第二步")
    def hai(self):
        print("是")

    @allure.step("第一步")
    def xu(self):
        print("我")

    @allure.step("第三步")
    def feng(self):
        print("我")

    @allure.step("开始")
    def test_01(self):
        allure.attach(self.driver.get_screenshot_as_png(), "百度首页", allure.attachment_type.PNG)
        self.xu()
        self.hai()
        self.feng()
        print("\n test_001")
