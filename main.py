import os
import configparser
import unittest
from selenium import webdriver
from time import sleep

class search_familiar_images(unittest.TestCase):
    def getConfigContent(section, key):
        config = configparser.ConfigParser()
        config.read(path, encoding="utf-8")
        path = os.path.split(os.path.realpath(__file__))[0] + '/config.ini'
        return config.get(section, key)
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://image.baidu.com/"
        self.image_url = os.path.split(os.path.realpath(__file__))[0] + '/img.png'
    def search_image(self):
        # 谷歌我本地访问不了，暂为从百度图库里搜图
        wd = self.driver
        wd.get(self.base_url+"/")
        # 点击图片上传按钮弹出对话框
        wd.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        # 在对话框send图片并确定上传
        wd.find_element_by_xpath('//*[@id="uploadImg"]').send_keys(self.image_url)
        # 直接等待并跳转到结果页并定位相应结果
        wd.implicitly_wait(10)
        VISIT_RESULT_INDEX = getConfig("IMAGE", "VISIT_RESULT")
        wd.find_element_by_xpath("'//*[@id="imgid"]/div[1]/ul/li[" + VISIT_RESULT_INDEX + "]/div/div[3]/img'").click()
        wd.get_screenshot_as_file('screenshot_for_last_page.png')
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()







