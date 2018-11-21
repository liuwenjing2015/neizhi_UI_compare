#encoding:utf-8
import atx
import time
import os
import adb
import datetime
import logzero
from logzero import logger
from atx.ext.report import Report

log_dir = os.path.join(os.path.split(os.path.realpath(__file__))[0],'log')
if not os.path.isdir(log_dir):
    os.makedirs(log_dir)
error_log = os.path.join(log_dir, datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.log')
if not os.path.exists(error_log):
    os.system(r'touch %s' % error_log)
logzero.logfile(error_log)

class UICompaare():
    pic_save = os.path.join(os.path.split(os.path.realpath(__file__))[0],'resource pic')
    log_dir = os.path.join(os.path.split(os.path.realpath(__file__))[0],'log')
    adb = adb.ADB()

    def pic_aim(self,pic_name):
        pic_dir = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'pic')
        aim_pic = os.path.join(pic_dir,pic_name)
        return aim_pic

    def pic_exist(self, d, pic_name):
        pic = self.pic_aim(pic_name)
        if d.exists(pic,threshold= 0.9)!= None:
            logger.info("Pass,内置数据 %s 测试通过" % pic_name)
        else:
            logger.info("Failed,内置数据 %s 异常，请查看截图" % pic_name)

    def PicCom(self):
        os.system('adb shell pm clear com.wuba')
        d = atx.connect()
        d.start_app('com.wuba', 'com.wuba.activity.launch.LaunchActivity')
        time.sleep(1)
        # 三次都点击弹框中的允许
        for i in range(3):
            if d.uiautomator(text=u'允许'):
                d.uiautomator(text=u'允许').click()

        rp = Report(d, save_dir=u'report')
        rp.patch_uiautomator()
        rp.info("Test started", screenshot=d.screenshot())

        #对比城市列表页面
        d.wait(self.pic_aim("city_title@auto.png"))
        self.pic_exist(d, "city_title@auto.png")
        self.pic_exist(d, "city_hotcity@auto.png")
        self.pic_exist(d, "city_hotcitylist@auto.png")
        self.pic_exist(d, "city_A_list@auto.png")
        self.adb.get_screenshot(self.pic_save)
        #对比乡镇列表页面
        d.uiautomator(text=u'乡镇').click()
        self.pic_exist(d, "town_title@auto.png")
        self.pic_exist(d, "town_pro@auto.png")
        self.pic_exist(d, "town_list@auto.png")
        self.adb.get_screenshot(self.pic_save)
        #对比海外列表页面
        d.uiautomator(text=u'海外').click()
        self.pic_exist(d, "oversea_poi@auto.png")
        self.pic_exist(d, "oversea_Am@auto.png")
        self.pic_exist(d, "oversea_Am_list@auto.png")
        self.pic_exist(d, "oversea_Can@auto.png")
        self.adb.get_screenshot(self.pic_save)
        self.adb.press_back()
        try:
            d.uiautomator(text=u'取消').click()
        except:
            pass
        # 对比首页大类
        d.wait(self.pic_aim("quanzhi@auto.png"))
        self.pic_exist(d, "quanzhi@auto.png")
        self.pic_exist(d, "jianzhi@auto.png")
        self.pic_exist(d, "zufang@auto.png")
        self.pic_exist(d, "ershoufang@auto.png")
        self.pic_exist(d, "ershouwupin@auto.png")
        self.pic_exist(d, "ershouche@auto.png")
        self.pic_exist(d, "chongwu@auto.png")
        self.pic_exist(d, "jiazheng@auto.png")
        self.pic_exist(d, "bendifuwu@auto.png")
        self.pic_exist(d, "gengduo@auto.png")
        #对比到家服务
        self.pic_exist(d, "daojia_title@auto.png")
        self.pic_exist(d, "daojia_baojie@auto.png")
        self.pic_exist(d, "daojia_baomu@auto.png")
        self.pic_exist(d, "daojia_yuesao@auto.png")
        self.adb.get_screenshot(self.pic_save)
        d.swipe(1208, 1356, 317, 1356) #到家服务右滑
        self.pic_exist(d, "daojia_huoyun@auto.png")
        self.pic_exist(d, "daojia_yuersao@auto.png")
        d.swipe(651, 493, 651, 2066) #首页下滑
        time.sleep(2)
        self.adb.get_screenshot(self.pic_save)

        #兼职页面对比
        d.uiautomator(text=u'兼职').click()
        d.wait(self.pic_aim("jianzhi_fabujianli@auto.png"))
        self.pic_exist(d, "jianzhi_fabujianli@auto.png")
        self.pic_exist(d, "jianzhi_searchmoren@auto.png")
        self.pic_exist(d, "jianzhi_zuixin@auto.png")
        self.pic_exist(d, "jianzhi_fujingangwei@auto.png")
        self.pic_exist(d, "jianzhi_kaopugangwei@auto.png")
        self.pic_exist(d, "jianzhi_zhoumojianzhi@auto.png")
        self.pic_exist(d, "jianzhi_xianshangrenwu@auto.png")
        self.pic_exist(d, "jianzhi_remenjianzhi@auto.png")
        self.pic_exist(d, "jianzhi_chakanquanbu@auto.png")
        self.pic_exist(d, "jianzhi_dingyuezhiwei@auto.png")
        self.pic_exist(d, "jianzhi_denglutixing@auto.png")
        self.adb.get_screenshot(self.pic_save)
        self.adb.press_back()

        #发现页面对比
        # d.uiautomator(text=u'发现').click()
        # self.pic_exist(d, "faxian_dingyue@auto.png")
        # self.pic_exist(d, "faxian_zuji@auto.png")
        # self.adb.get_screenshot(self.pic_save)

        #发布页面对比
        d.uiautomator(text=u'发布').click()
        self.pic_exist(d, "fabu_fabu@auto.png")
        self.pic_exist(d, "fabu_fangchan@auto.png")
        self.pic_exist(d, "fabu_fabuzhiwei@auto.png")
        self.pic_exist(d, "fabu_ershouwupin@auto.png")
        self.pic_exist(d, "fabu_car@auto.png")
        self.pic_exist(d, "fabu_bendifuwu@auto.png")
        self.pic_exist(d, "fabu_qiuzu@auto.png")
        # self.pic_exist(d, "fabu_jiaoyupeixun@auto.png")   #8.9.0版本去掉
        # self.pic_exist(d, "fabu_chongwu@auto.png")   #8.9.0版本去掉
        # self.pic_exist(d, "fabu_shangwufuwu@auto.png")  #8.9.0版本去掉
        self.pic_exist(d, "fabu_carserve@auto.png")
        self.pic_exist(d, "fabu_jiazhengfuwu@auto.png")
        self.pic_exist(d, "fabu_zhuangxiujiancai@auto.png")
        self.pic_exist(d, "fabu_piaowu@auto.png")
        self.pic_exist(d, "fabu_pinche@auto.png")
        self.pic_exist(d, "fabu_xunren@auto.png")
        self.adb.get_screenshot(self.pic_save)

        #对比消息页面
        d.uiautomator(text=u'消息').click()
        d.wait(self.pic_aim("xiaoxi_jingxuan@auto.png"))
        self.pic_exist(d, "xiaoxi_jingxuan@auto.png")
        self.pic_exist(d, "xiaoxi_hudong@auto.png")
        self.pic_exist(d, "xiaoxi_tuijian@auto.png")
        self.pic_exist(d, "xiaoxi_dingyue@auto.png")
        self.pic_exist(d, "xiaoxi_tixing@auto.png")
        self.adb.get_screenshot(self.pic_save)

        # 对比个人中心页面
        d.uiautomator(text=u'个人中心').click()
        d.wait(self.pic_aim("UCenter_dengluicon@auto.png"))
        self.pic_exist(d, "UCenter_dengluicon@auto.png")
        self.pic_exist(d, "UCenter_xunzhang@auto.png")
        self.pic_exist(d, "UCenter_jinbi@auto.png")
        self.pic_exist(d, "UCenter_shenqikuang@auto.png")
        self.pic_exist(d, "UCenter_qianbao@auto.png")
        #self.pic_exist(d, "UCenter_renwu@auto.png")
        self.pic_exist(d, "UCenter_fabu@auto.png")
        self.pic_exist(d, "UCenter_shoucang@auto.png")
        self.pic_exist(d, "UCenter_lishi@auto.png")
        self.pic_exist(d, "UCenter_dingyue@auto.png")
        self.pic_exist(d, "UCenter_title@auto.png")
        self.pic_exist(d, "UCenter_qiuzhi@auto.png")
        self.pic_exist(d, "UCenter_ershou@auto.png")
        self.pic_exist(d, "UCenter_zufang@auto.png")
        self.pic_exist(d, "UCenter_pingjia@auto.png")
        self.pic_exist(d, "UCenter_daikuan@auto.png")
        self.pic_exist(d, "UCenter_licai@auto.png")
        self.pic_exist(d, "UCenter_renzheng@auto.png")
        self.adb.get_screenshot(self.pic_save)
    # d.click_image(self.pic_aim("fabu_xunren@auto.png"))
    #     self.adb.press_back()
        rp.close()

if __name__ == '__main__':
    default_test = UICompaare()
    default_test.PicCom()
