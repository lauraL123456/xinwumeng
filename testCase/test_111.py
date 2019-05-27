import time
import random

import pytest

from Common.baseui import baseUI

class TestUI():
    #重复执行几次,数字就填几
    @pytest.mark.repeat(20)
    def test_login(self,driver):
        base = baseUI(driver)
        driver.get("http://192.168.0.101")
        #  输入用户名  '输入用户名','//input[@name="username"] ','admin'
        base.send_keys('输入用户名', '//input[@name="username"] ', 'wuming')
        #  输入密码  '输入密码','//input[@name="password"] ',111111
        base.send_keys('输入密码', '//input[@name="password"] ', 'a111111')
        #  点击登录  '点击登录',"//span[contains(text(),'登录')]"
        base.click('点击登录', "//span[contains(text(),'登录')]")
        #退出登录



    def test_111(self,driver):
        base = baseUI(driver)
        driver.get("http://192.168.0.101")
        #  输入用户名  '输入用户名','//input[@name="username"] ','admin'
        base.send_keys('输入用户名','//input[@name="username"] ','wuming')
        #  输入密码  '输入密码','//input[@name="password"] ',111111
        base.send_keys('输入密码','//input[@name="password"] ','a111111')
        #  点击登录  '点击登录',"//span[contains(text(),'登录')]"
        base.click('点击登录',"//span[contains(text(),'登录')]")
        #  点击运输相关配置  '点击运输相关配置',"//span[contains(text(),'运输相关配置')]"
        base.click('点击运输相关配置',"//span[contains(text(),'运输相关配置')]")


        #  点击运输类型   '点击运输类型',"//span[contains(text(),'运输类型')]"
        base.click('点击运输类型',"//span[contains(text(),'运输类型')]")
        #  点击新增   '点击新增',"//span[contains(text(),'新增')]"
        base.click('点击新增',"//span[contains(text(),'新增')]")
        #  输入代码  "//div[@aria-label='新增']//label[contains(text(),'代码')]/following-sibling::div//input"
        base.send_keys('输入代码',"//div[@aria-label='新增']//label[contains(text(),'代码')]/following-sibling::div//input",'X%d'%random.randint(100,999))
        #  输入名称  '输入名称','(//div[@class="el-input el-input--medium"])[2]','面包车运输'
        # base.send_keys('输入名称',"(//div[@aria-label='新增']//label[contains(text(),'名称:')]/following-sibling::div//input)[1]",'面包车运输')
        # base.send_keys('输入名称',"(//label[contains(text(),'名称:')]/following-sibling::div//input)[2]",'面包车运输')
        base.send_keys('输入名称',"//div[@aria-label='新增']//label[contains(text(),'名称')]/following-sibling::div//input",'面包车运输%d'%random.randint(100,999))
        #  点击失效日期框   "//div[@aria-label='新增']//label[contains(text(),'失效日期')]/following-sibling::div//input"
        base.click('点击失效日期框',"//div[@aria-label='新增']//label[contains(text(),'失效日期')]/following-sibling::div//input")
        # 点击日期    "//th[text()='日']/parent::*/following-sibling::tr//td[@class='available']//span[contains(text(),'28')]"
        base.click('点击日期', "//th[text()='日']/parent::*/following-sibling::tr//td[@class='available']//span[contains(text(),'28')]")
        #  点击确定   '点击确定','//span[contains(text(),'确 定')]'
        base.click('点击确定',"//span[contains(text(),'确 定')]")
        #  点击编辑   '点击编辑','//span[contains(text(),'编辑')]'
        # base.click('点击编辑',"(//span[contains(text(),'ASDFASFD')])[1]/parent::*/parent::*/following-sibling::td//span[contains(text(),'编辑')]")
        base.click('点击编辑',"//*[@id='app']/div/div[2]/section/div/div[2]/div/div[4]/div[2]/table/tbody/tr[1]/td[4]/div/div/button[1]/span/span")
        #  输入代码(输入框需要做个清空)     '输入代码','(//div[@class="el-input el-input--medium"])[3]','X100'
        base.send_keys('输入代码',"//div[@aria-label='编辑']//label[contains(text(),'代码')]/following-sibling::div//input",'X%d'%random.randint(100,999))
        #  输入名称    '输入名称','(//div[@class="el-input el-input--medium"])[4]','集装箱运输'
        base.send_keys('输入名称',"//div[@aria-label='编辑']//label[contains(text(),'名称')]/following-sibling::div//input",'集装箱运输%d'%random.randint(100,999))
        #  点击日期    '点击日期','(//span[contains(text(),30)])[2]'
        base.click('点击失效日期',"//div[@aria-label='编辑']//label[contains(text(),'失效日期')]/following-sibling::div//input")
        # base.click('点击日期',"//th[text()='日']/parent::*/following-sibling::tr//td[@class='available']//span[contains(text(),'28')]")
        base.click('点击日期','/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[3]/div/span')
        #  点击确定   '点击确定','//span[contains(text(),'确 定')]'
        base.click('点击确定',"//span[contains(text(),'确 定')]")

        # 切换点击运输方式  '点击运输方式','(//span[contains(text(),'运输方式')])[1]'
        base.click('点击运输方式',"(//span[contains(text(),'运输方式')])[1]")
        #  输入代码  '输入代码','(//div[@class="el-input el-input--medium"])[1]','X101'
        base.send_keys('输入代码',"//label[contains(text(),'代码')]/following-sibling::div//input",'X888')
        #  输入名称  '输入名称','(//div[@class="el-input el-input--medium"])[2]','门到站'
        base.send_keys('输入名称',"//label[contains(text(),'名称')]/following-sibling::div//input",'AAA')
        #  点击查询   '点击查询','//span[contains(text(),'查询')]'
        base.click('点击查询',"//span[contains(text(),'查询')]")


        #  点击删除     '点击删除','//span[contains(text(),'删除')]'
        base.click('点击删除',"//span[contains(text(),'删除')]")
        # 点击确定      '点击确定','(//span[contains(text(),'确定')])[2]'
        # base.click('点击确定',"//span[contains(text(),'确定')])[2]")
        base.click('点击确定','/html/body/div[3]/div/div[3]/button[2]/span')
# 切换点击报价类型  //*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/ul/div[6]/a/li/span
        # base.click('点击报价类型','//*[@id="app"]/div/div[2]/div[1]/div/ul/div[3]/li/ul/div[6]/a/li/span')
        base.click('点击重泡类型',"//span[contains(text(),'重泡类型')][1]")
        # 输入代码
        base.send_keys('输入代码','//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[1]/div/div/div/input','100')
        # 输入名称
        base.send_keys('输入名称','//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[2]/div/div/div/input','重货')
        # 点击查询
        base.click('点击查询','//*[@id="app"]/div/div[2]/section/div/div[1]/div/button[1]/span')
        time.sleep(1)
        # 点击清空查询  //span[contains(text(),'清空查询')]
        base.click('点击清空查询',"//span[contains(text(),'清空查询')]")
        time.sleep(1)
        #  点击查询   '点击查询','//span[contains(text(),'查询')]'
        base.click('点击查询',"//span[contains(text(),'查询')]")
        time.sleep(2)
        #  点击新增
        base.click('点击新增',"//span[contains(text(),'新增')]")
        # 输入代码
        base.click('输入代码',"//div[@aria-label='新增']//label[contains(text(),'代码')]/following-sibling::div//input",'ABC')
        # 点击勾选下拉默认值
        base.click('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div/div[2]/form/div[3]/div/label/span')

