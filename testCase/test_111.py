import time
import random

import pytest

from Common.baseui import baseUI

class TestUI():
    # @pytest.markrk.xinyang
    # @pytest.mark.repeat(2)
    # def test_login(self,driver):
    #     base = baseUI(driver)
    #     driver.get("http://192.168.0.101")
    #     #  输入用户名  '输入用户名','//input[@name="username"] ','admin'
    #     base.send_keys('输入用户名', '//input[@name="username"] ', 'wuming')
    #     #  输入密码  '输入密码','//input[@name="password"] ',111111
    #     base.send_keys('输入密码', '//input[@name="password"] ', 'a111111')
    #     #  点击登录  '点击登录',"//span[contains(text(),'登录')]"
    #     base.click('点击登录', "//span[contains(text(),'登录')]")
    #     #退出登录
    #     base.click('点击退出图标','//*[@id="app"]/div/div[2]/div[1]/div[3]/div/div/img')
    #     # 点击退出登录     "//span[contains(text(),'退出登录')]"
    #     base.click('点击退出登录',"//span[contains(text(),'退出登录')]")
    #
    # @pytest.mark.xin
    def test_111(self,driver):
        base = baseUI(driver)
        driver.get("http://10.10.10.149")   # 运营
        base.send_keys('输入用户名','//input[@name="username"] ','admin')
        base.send_keys('输入密码','//input[@name="password"] ','111111')
        base.click('点击登录',"//span[contains(text(),'登录')]")
        base.click('点击运输相关配置',"//span[contains(text(),'运输相关配置')]")
        base.click('点击运输类型',"//span[contains(text(),'运输类型')]")
        base.send_keys('输入代码','(//input[@class="el-input__inner"])[3]','X222')
        # base.send_keys('输入代码','//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div/div[1]/div/div/div/input','X%d'%random.randint(100,999))
        base.send_keys('输入名称','(//input[@class="el-input__inner"])[4]','运输')
        # base.send_keys('输入名称',"//label[contains(text(),'名称')]/following-sibling::div//input",'运输')
        base.click('点击查询',"//span[contains(text(),'查询')]")
        base.click('点击清空',"//span[contains(text(),'清空查询')]")
        base.click('点击查询',"//span[contains(text(),'查询')]")
        #  点击翻页按钮
        # base.click('点击翻页','//*[@id="app"]/div/div[2]/section/div/div[3]/div/button[2]/i')

        #  点击新增   '点击新增',"//span[contains(text(),'新增')]"
        base.click('点击新增',"//span[contains(text(),'新增')]")
        #  输入代码  "//div[@aria-label='新增']//label[contains(text(),'代码')]/following-sibling::div//input"
        base.send_keys('输入代码',"//div[@aria-label='新增']//label[contains(text(),'代码')]/following-sibling::div//input",'X%d'%random.randint(100,999))
        base.send_keys('输入名称',"//div[@aria-label='新增']//label[contains(text(),'名称')]/following-sibling::div//input",'面包车运输%d'%random.randint(100,999))
        #  点击失效日期框   "//div[@aria-label='新增']//label[contains(text(),'失效日期')]/following-sibling::div//input"
        base.click('点击失效日期框',"//div[@aria-label='新增']//label[contains(text(),'失效日期')]/following-sibling::div//input")
        # 点击日期    "//th[text()='日']/parent::*/following-sibling::tr//td[@class='available']//span[contains(text(),'28')]"
        base.click('点击日期', "//th[text()='日']/parent::*/following-sibling::tr//td[@class='available']//span[contains(text(),'11')]")
        # base.click('点击日期','/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[4]/td[4]/div/span')
        base.click('点击确定',"//span[contains(text(),'确 定')]")
        # base.click('点击编辑',"(//span[contains(text(),'ASDFASFD')])[1]/parent::*/parent::*/following-sibling::td//span[contains(text(),'编辑')]")
        base.click('点击编辑第四个',"(//span[contains(text(),'编辑')])[4]")
        base.send_keys('输入代码',"//div[@aria-label='编辑']//label[contains(text(),'代码')]/following-sibling::div//input",'X%d'%random.randint(100,999))
        # base.send_keys('输入代码','(//input[@class="el-input__inner"])[7]','X330')
        base.send_keys('输入名称',"//div[@aria-label='编辑']//label[contains(text(),'名称')]/following-sibling::div//input",'集装箱运输%d'%random.randint(100,999))
        # base.send_keys('输入名称','(//input[@class="el-input__inner"])[8]','半挂车运输4')
        #  点击失效日期
        base.click('点击失效日期',"//div[@aria-label='编辑']//label[contains(text(),'失效日期')]/following-sibling::div//input")
        base.click('点击日期',"//th[text()='日']/parent::*/following-sibling::tr//td[@class='available']//span[contains(text(),'23')]")
        # base.click('选择日期','/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[3]/td[7]/div/span')
        # base.click('点击日期','(//span[contains(text(),"15")])[3]')
        base.click('点击确定',"//span[contains(text(),'确 定')]")
######################################################################################################################
        # 切换点击运输方式
        base.click('点击运输方式',"(//span[contains(text(),'运输方式')])[1]")
        base.send_keys('输入代码',"//label[contains(text(),'代码')]/following-sibling::div//input",'X102')
        # base.send_keys('输入代码','(//input[@class="el-input__inner"])[1]','X102')
        base.send_keys('输入名称',"//label[contains(text(),'名称')]/following-sibling::div//input",'站到站')
        # base.send_keys('输入名称','(//input[@class="el-input__inner"])[2]','站到站')
        base.click('点击查询',"//span[contains(text(),'查询')]")
        base.click('点击新增',"(//span[contains(text(),'新增')])[1]")
        #  输入代码  "//div[@aria-label='新增']//label[contains(text(),'代码')]/following-sibling::div//input"
        base.send_keys('输入代码',"//div[@aria-label='新增']//label[contains(text(),'代码')]/following-sibling::div//input",'X%d'%random.randint(100,999))
        #  输入名称  '输入名称','(//div[@class="el-input el-input--medium"])[2]','面包车运输'
        base.send_keys('输入名称',"//div[@aria-label='新增']//label[contains(text(),'名称')]/following-sibling::div//input",'门到站%d'%random.randint(100,999))
        base.click('点击复选框','//span[@class="el-checkbox__input"]')
        #  点击失效日期    '点击失效日期','(//span[contains(text(),30)])[2]'
        # base.click('点击失效日期',"//div[@aria-label='编辑']//label[contains(text(),'失效日期')]/following-sibling::div//input")
        base.click('点击失效日期','//*[@id="datePickered"]')
        base.click('选择日期',"//th[text()='日']/parent::*/following-sibling::tr//td[@class='available']//span[contains(text(),'28')]")
        base.click('点击确定',"//span[contains(text(),'确 定')]")
        #  输入代码  '输入代码','(//div[@class="el-input el-input--medium"])[1]','X101'
        base.send_keys('输入代码',"//label[contains(text(),'代码')]/following-sibling::div//input",'X27')
        # base.send_keys('输入代码',"//label[contains(text(),'代码')]/following-sibling::div//input",'X%d'%random.randint(100,999))
        base.send_keys('输入名称',"//label[contains(text(),'名称')]/following-sibling::div//input",'门到门')
        base.click('点击查询',"//span[contains(text(),'查询')]")
        base.click('点击清空',"//span[contains(text(),'清空查询')]")
        base.click('点击查询',"(//span[contains(text(),'查询')])[1]")
        base.click('点击编辑',"//span[contains(text(),'编辑')]")
        base.click('点击取消',"//span[contains(text(),'取 消')]")
        #  点击删除     '点击删除','//span[contains(text(),'删除')]'
        base.click('点击删除',"(//span[contains(text(),'删除')])[17]")
        # 点击确定      '点击确定','//span[contains(text(),'确定')]'
        base.click('点击确定',"(//span[contains(text(),'确定')])[1]")
        # # 切换点击重泡类型
        # base.click('点击重泡类型',"//span[contains(text(),'重泡类型')][1]")
        # # 输入代码
        # base.send_keys('输入代码','//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[1]/div/div/div/input','100')
        # # 输入名称
        # base.send_keys('输入名称','//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[2]/div/div/div/input','重货')
        # # 点击查询
        # base.click('点击查询','//*[@id="app"]/div/div[2]/section/div/div[1]/div/button[1]/span')
        # time.sleep(1)
        # # 点击清空查询  //span[contains(text(),'清空查询')]
        # base.click('点击清空查询',"//span[contains(text(),'清空查询')]")
        # time.sleep(1)
        # #  点击查询   '点击查询','//span[contains(text(),'查询')]'
        # base.click('点击查询',"//span[contains(text(),'查询')]")
        # time.sleep(2)
        # #  点击新增
        # base.click('点击新增',"//span[contains(text(),'新增')]")
        # # 输入代码
        # base.click('输入代码',"//div[@aria-label='新增']//label[contains(text(),'代码')]/following-sibling::div//input",'ABC')
        # # 点击勾选下拉默认值
        # base.click('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div/div[2]/form/div[3]/div/label/span')
        # #
