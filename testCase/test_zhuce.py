import time
import random

import pytest

from Common.baseui import baseUI

class TestUI():
    def test_zhuce(self,driver):
        base = baseUI(driver)
        driver.get("http://10.10.10.149:8081")  # 货主承运
        base.click('注册新账号',"//span[contains(text(),'注册新账号')]")
        base.click('点击"知道了"注册须知',"//*[@id='app']/div/div[2]/div/div/button/span")
        base.send_keys('输入手机号','//input[@class="el-input__inner"]',"18201972309")
        base.click('获取验证码',"//span[contains(text(),'获取验证码')]")
        base.send_keys('输入验证码','(//input[@class="el-input__inner"])[2]',"    ")# ------------------
        base.click('勾选服务条款协议','//span[@class="el-checkbox__inner"]')
        base.click('下一步',"//span[contains(text(),'下一步')]")
        base.send_keys('上传营业执照','//i[@class="el-icon-plus avatar-uploader-icon"]',
                       "C:\\Users\\DELL\\Desktop\\认证图片\\营业执照(1)\\营业执照\\南京聚力医药.jpg")
        base.send_keys('社会统一信用代码','(//input[@class="el-input__inner"])[1]','913201067331649774')
        base.send_keys('企业名称','(//input[@class="el-input__inner"])[2]','南京聚力医药科技有限公司')
        base.click('点击下一步',"//span[contains(text(),'下一步')]")
        base.send_keys('上传身份证正面','(//i[@class="el-icon-plus avatar-uploader-icon-horizontal"])[1]',
                       "C:\\Users\DELL\\Desktop\\认证图片\\身份证(1)\\身份证\\杨文丽0.png")
        base.send_keys('上传身份证反面','(//i[@class="el-icon-plus avatar-uploader-icon-horizontal"])[2]',
                       "C:\\Users\DELL\\Desktop\\认证图片\\身份证(1)\\身份证\\杨文丽1.png")
        base.send_keys('身份证号','(//input[@class="el-input__inner"])[1]','340321199408020820')
        base.click('下一步',"//span[contains(text(),'下一步')]")
        base.send_keys('上传道路运输经营许可证','(//i[@class="el-icon-plus avatar-uploader-icon-horizontal"])[1]',
                       "C:\\Users\\DELL\\Desktop\\认证图片\\道路运输许可证\\道路运输许可证.jpg")
        base.click('跳过',"(//span[contains(text(),'跳过')])[2]")
        base.send_keys('用户名','(//input[@class="el-input__inner"])[1]','oppo1234')
        base.send_keys('姓名','(//input[@class="el-input__inner"])[2]','亮晶晶')
        base.send_keys('密码','(//input[@class="el-input__inner"])[3]','q111111')
        base.send_keys('确认密码','(//input[@class="el-input__inner"])[4]','q111111')
        base.click('点击完成',"//span[contains(text(),'完成')]")
        # 拦截页_编辑基本信息
        base.send_keys('税号','(//input[@class="el-input__inner"])[4]','91310115MA1H9HJY9F')
        base.send_keys('单位地址','(//input[@class="el-input__inner"])[5]', '上海欣雅供应链管理有限公司')
        base.send_keys('开户银行','(//input[@class="el-input__inner"])[6]', '上海银行浦东支行')
        base.send_keys('银行账号','(//input[@class="el-input__inner"])[7]', '6221882900055141205')
        base.send_keys('企业邮箱','(//input[@class="el-input__inner"])[8]', '18201972309@163.com')
        base.send_keys('联系人','(//input[@class="el-input__inner"])[9]', '亮晶晶')
        base.send_keys('电话','(//input[@class="el-input__inner"])[10]', '18201972309')
        # 营业执照内容编辑
        base.send_keys('上传营业执照','(//i[@class="el-icon-plus avatar-uploader-icon"])[2]',
                       "C:\\Users\\DELL\\Desktop\\认证图片\\营业执照(1)\\营业执照\\南京聚力医药.jpg")
        base.send_keys('企业名称','(//input[@class="el-input__inner"])[11]','测试一')
        base.send_keys('社会统一信用代码','(//input[@class="el-input__inner"])[12]','91440300772741121F')
        # 上传法人身份证信息
        base.send_keys('身份证号','(//input[@class="el-input__inner"])[13]',110000199001011112)
        base.send_keys('姓名','(//input[@class="el-input__inner"])[14]','测试一')
        #  道路运输经营许可证
        base.click('许可代码下拉框','(//input[@class="el-input__inner"])[15]')
        base.click('选择省份','//span[contains(text(),"沪")]')
        base.send_keys('字','(//input[@class="el-input__inner"])[16]','上海')
        base.send_keys('号','(//input[@class="el-input__inner"])[17]','310115021765')
        base.send_keys('业户名称','(//input[@class="el-input__inner"])[18]','上海欣雅供应链管理有限公司')
        # 危险化学品经营许可证
        base.send_keys('上传危化经营许可证','(//i[@class="el-icon-plus avatar-uploader-icon"])[1]',
                       'C:\\Users\\DELL\\Desktop\\认证图片\\危化品运输\\危化1.jpg')
        base.send_keys('整数编号','(//input[@class="el-input__inner"])[19]','D31083')
        base.send_keys('单位名称','(//input[@class="el-input__inner"])[20]','测试一')
        base.click('提交','//span[contains(text(),"提交")]')
        base.click('确认提交','//span[contains(text(),"确认提交")]')
        base.click('确认','//span[contains(text(),"确认")]')
        base.click('建材','//li[contains(text(),"建材")]')
        base.click('百货','//li[contains(text(),"百货")]')
        base.click('保存','//span[contains(text(),"保存")]')

        base.click('基础信息','//span[contains(text(),"基础信息")]')
        base.click('单位信息','//span[contains(text(),"单位信息")]')
        base.send_keys('下拉单位名称','(//input[@class="el-input__inner"])[3]','测试一')
        base.click('下拉创建来源','(//input[@class="el-input__inner"])[4]')
        base.click('选择注册','//span[contains(text(),"注册")]')
        base.click('下拉企业类型','(//input[@class="el-input__inner"])[5]')
        base.click('选择货主','//span[contains(text(),"货主")]')
        base.click('下拉审核状态','(//input[@class="el-input__inner"])[6]')
        base.click('选择待审核','//span[contains(text(),"待审核")]')
        base.click('查询','//span[contains(text(),"查询")]')
        base.click('查看','//span[contains(text(),"查看")]')




        # 合同管理
        base.click('合同管理','//span[contains(text(),"合同管理")]')
        base.click('签名管理','//span[contains(text(),"签名管理")]')

        base.click('合同模板','//span[contains(text(),"合同模板")]')

        base.click('签约管理','//span[contains(text(),"签约管理")]')

        time.sleep(2)