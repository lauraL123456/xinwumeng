import os
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    driver_path = os.path.join(os.path.dirname(__file__), "../ChromDriver/chromedriver.exe")
    # 打开浏览器
    dr = webdriver.Chrome(driver_path)
    dr.maximize_window()  # 最大化浏览器
    dr.set_page_load_timeout(10)#网页加载超时为10s
    dr.set_script_timeout(10)#js脚本运行超时10s
    dr.implicitly_wait(10)#元素查找超时时间10s
    yield dr
    dr.quit()
