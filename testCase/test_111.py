import time

from Common.baseui import baseUI


class TestUI():

    def test_111(self,driver):
        base = baseUI(driver)
        driver.get("http://192.168.0.101")
        #  打开网页浏览器   ( http://api.xsungroup.com:8080 测试环境)  ( http://10.10.10.171:8080 开发环境的 )


        #  输入用户名    '输入用户名','//input[@name="username"] ','admin'
        base.send_keys('输入用户名','//input[@name="username"] ','admin')

        #  输入密码     '输入密码','//input[@name="password"] ',111111
        base.send_keys('输入密码','//input[@name="password"] ','111111')

        #  点击登录     '点击登录','//span[contains(text(),'登录')]'
        base.click('点击登录',"//span[contains(text(),'登录')]")
        #  ------------------------------------------------------------------------------------------------------

        #  点击首页       '点击首页','//*[@id="app"]/div/div[2]/div[1]/div[1]/svg'
        # base.click('点击首页',"(//div[@id='app']/div/div[2]//*[name()='svg'])[1]")
        # base.click('点击首页','//div[@id="toggelTEST"]')

        #  点击运输相关配置  '点击运输相关配置',"//span[contains(text(),'运输相关配置')]"
        base.click('点击运输相关配置',"//span[contains(text(),'运输相关配置')]")
        #  点击运输类型     '点击运输相关配置','//span[contains(text(),'运输类型')]'
        base.click('点击运输相关配置',"//span[contains(text(),'运输类型')]")
        #  ------------------------------------------------------------------------------------------------------

        #  点击新增    '点击新增','//span[contains(text(),'新增')]'

        #  输入代码    '输入代码','(//div[@class="el-input el-input--medium"])[1]','X007'

        #  输入名称   '输入名称','(//div[@class="el-input el-input--medium"])[2]','面包车运输'

        #  点击失效日期框   '点击失效日期框','//div[@class="el-date-editor el-input el-input--medium el-input--prefix el-input--suffix el-date-editor--date"]'

        #  点击日期   '点击日期','(//span[contains(text(),28)])[2]'

        #  点击确定   '点击确定','//span[contains(text(),'确 定')]'

        #  ------------------------------------------------------------------------------------------------------

        #  点击编辑   '点击编辑','//span[contains(text(),'编辑')]'

        #  输入代码(输入框需要做个清空)     '输入代码','(//div[@class="el-input el-input--medium"])[3]','X100'

        #  输入名称     '输入名称','(//div[@class="el-input el-input--medium"])[4]','集装箱运输'

        #  点击日期   '点击日期','(//span[contains(text(),30)])[2]'

        #  点击确定   '点击确定','//span[contains(text(),'确 定')]'

        #  -------------------------------------------------------------------------------------------------------


        # 切换点击运输方式  '点击运输方式','(//span[contains(text(),'运输方式')])[1]'

        #  输入代码    '输入代码','(//div[@class="el-input el-input--medium"])[1]','X101'

        #  输入名称    '输入名称','(//div[@class="el-input el-input--medium"])[2]','门到站'

        #  点击查询     '点击查询','//span[contains(text(),'查询')]'



        #  点击删除     '点击删除','//span[contains(text(),'删除')]'

        # 点击确定      '点击确定','(//span[contains(text(),'确定')])[2]'






