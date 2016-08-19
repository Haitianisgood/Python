#! /usr/bin/env python
#coding=utf-8
#author lishijie
#编辑控制流
import datetime
import re
import time
import string
import random

from module import *


class UserManagementC:

    def __init__(self):
        self.__PASS = 'Pass'
        self.__FAIL = 'Fail'
        self.__ERROR = 'Error'
        self.browser = None
        self.util_act = UtilAction()
        self.replace_dict = {}
        self.replace_dict['organ_name'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name1'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name2'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name3'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name4'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name5'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name6'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name7'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name8'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name9'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name10'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name11'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name12'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name13'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name14'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name15'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_name16'] = 'auto-' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['organ_description'] = self.util_act.generate_random_string_simp(100)
        self.replace_dict['organ_description2'] = self.util_act.generate_random_string_simp(100)
        self.replace_dict['user_name'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name1'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name2'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name3'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name4'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name5'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name6'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name7'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name8'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name9'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name10'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name11'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name12'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name13'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name14'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name15'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_name16'] = 'auto_' + ''.join([(string.ascii_letters+string.digits+'_')[x]
                                                            for x in random.sample(range(0, 63), 13)])
        self.replace_dict['user_nickname'] = self.util_act.generate_random_string_simp(20)
        self.replace_dict['user_nickname2'] = self.util_act.generate_random_string_simp(20)
        self.replace_dict['user_password'] = (string.ascii_letters[random.randint(0, 51)] +
                                              ''.join([(string.ascii_letters+string.digits+'*_#@%$&=+')[x]
                                                       for x in random.sample(range(0, 71), 19)]))
        self.replace_dict['user_email'] = ''.join([(string.ascii_letters+string.digits+'._')[x]
                                                   for x in random.sample(range(0, 64), 20)]) + '@mail.com'
        self.replace_dict['user_email2'] = ''.join([(string.ascii_letters+string.digits+'._')[x]
                                                   for x in random.sample(range(0, 64), 20)]) + '@mail.com'
        self.replace_dict['user_cellphone'] = ''.join([string.digits[random.randint(0, 9)] for x in range(0, 11)])
        self.replace_dict['user_cellphone2'] = ''.join([string.digits[random.randint(0, 9)] for x in range(0, 11)])
        self.replace_dict['group_name'] = 'auto_' + self.util_act.generate_random_string_simp(15)
        self.replace_dict['group_description'] = self.util_act.generate_random_string_simp(100)
        self.replace_dict['group_description2'] = self.util_act.generate_random_string_simp(100)
        # self.replace_dict['organ_name'] = self.util_act.generate_random_string(20)
        # self.replace_dict['organ_description'] = self.util_act.generate_random_string(200)
        # self.replace_dict['user_name'] = self.util_act.generate_random_string(20)
        # self.replace_dict['user_nickname'] = self.util_act.generate_random_string(20)
        # self.replace_dict['user_email'] = ''.join([(string.ascii_letters+string.digits+'._')[x]
        #                                            for x in random.sample(range(0, 64), 20)]) + '@mail.com'
        # self.replace_dict['user_cellphone'] = ''.join([string.digits[random.randint(0, 9)] for x in range(0, 11)])
        # self.replace_dict['group_name'] = self.util_act.generate_random_string(20)
        # self.replace_dict['group_description'] = self.util_act.generate_random_string(200)
        self.log = logC(u'用户管理' + datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        self.log.log('organize name: ' + self.replace_dict['organ_name'])
        self.log.log('organize description: ' + self.replace_dict['organ_description'])

    # 资源管理-流程
    def do_product_buy(self, actives, compInfo):
        """调用解析模块和动作处理模块，返回执行结果。

        Args:
            actives : 测试用例动作的源数据
            compInfo: 测试用例使用数据的源数据

        Returns:
            result  : 测试用例执行结果，为自定义字符串结果
        """
        compDict = self.replace_pattern(Util.readComp(compInfo))
        result = self.util_act.utilActive(self.browser, actives, compDict, self.log)
        return result

    # 测试案例
    def testCase(self):
        """读取本次测试所有数据并返回汇总的结果。

        Returns:
            result_dict: 测试总的结果，生成报告用
        """
        try:
            # testExlUrl = 'bdoc2/userManagementMg/userManagement.xlsx'
            testExlUrl = 'bdoc2/userManagementMg/userManagement_1.xlsx'
            # dataExlUrl = 'data'
            dataExlUrl = 'ie'
            #读取测试案例内容
            # tables = Util.loadExcel(testExlUrl, dataExlUrl, 2, 458, 1, 5)
            tables = Util.loadExcel(testExlUrl, dataExlUrl, 2, 231, 1, 5)
        except Exception, e:
            print('Load excel error!\n' + str(e))
            raise e
        result_dict = {}
        if len(tables) > 0:
            result_dict = self.handle_steps(tables)
        return result_dict

    def handle_steps(self, table):
        """处理所有测试步骤和数据并返回所有测试结果。

        Args:
            table      : 测试步骤和数据的源数据

        Returns:
            result_dict: 所有测试用例执行后的结果汇总，生成报告用
        """
        test_id = ''
        test_description = ''
        test_steps = ''
        test_data = ''
        result_dict = {}
        test_browser = ''
        for i in range(0, len(table)):
            if i == (len(table) - 1) or table[i + 1][0]:
                result = self.__FAIL
                if not test_id:
                    test_id = table[i][0]
                    test_description = table[i][1]
                    test_browser = table[i][2]
                    test_steps = table[i][3].split(' ')[1]
                    if table[i][4]:
                        test_data = table[i][4] + ';'
                else:
                    test_steps += '/' + table[i][3].split(' ')[1]
                    if table[i][4]:
                        test_data += table[i][4] + ';'
                self.browser = WebControlC.openHtml(test_browser)
                imgName = test_id + '.png'
                # print imgName.decode('utf-8').encode('gbk')
                self.log.log('-------------------------------------------------' +
                             test_id + ' ' + test_description +
                             '-------------------------------------------------')
                try:
                    result = self.do_product_buy(test_steps, test_data)
                except Exception, e:
                    print(str(e))
                    self.log.log(str(e), 'error')
                finally:
                    self.log.log(result)
                    try:
                        #浏览器是否存在
                        len(self.browser.window_handles)
                        if result == self.__FAIL:
                            Util.catchImage(self.browser, 'img/' + imgName.decode('utf8').encode('gbk'))
                    except Exception, e:
                        self.log.log('No browser to take a screen shot!', 'error')
                        # print('No browser to take a screen shot!')
                        print(str(e))
                        return result_dict
                    result_dict.update(ReportData.createReportData(test_id, test_description, result,
                                                                   '../../img/' + imgName))
                    time.sleep(5)
                    #关闭页面
                    WebControlC.closeHtml(self.browser)
                    if result == "Pass":
                        print(test_id.decode('utf-8').encode('gbk') + ' Passed!')
                    else:
                        print(test_id.decode('utf-8').encode('gbk') + ' Failed!')
            elif table[i][0]:
                test_id = table[i][0]
                test_description = table[i][1]
                test_browser = table[i][2]
                test_steps = table[i][3].split(' ')[1]
                if table[i][4]:
                    test_data = table[i][4] + ';'
            else:
                test_steps += '/' + table[i][3].split(' ')[1]
                if table[i][4]:
                    test_data += table[i][4] + ';'
        return result_dict

    # 对测试数据的随机值部分做替换
    def replace_pattern(self, original_dict):
        """对测试过程中需要的一些随机值做替换，替换的规则为——
        预定义'abc' = datetime.datetime.now().strftime('%Y%m%d%H%M%S'), 之后将测试数据中对应的'${abc}'替换为'abc'的值。
        对于不需要替换的值则解析后更新到字典并返回。

        Args:
            original_dict: 需要处理的原始测试数据

        Returns:
            real_dict    : 解析并替换后的字典型测试数据
        """
        real_dict = {}
        pattern = re.compile(r'\$\{.*?\}')
        for each_key in original_dict:
            rep_list = pattern.findall(original_dict[each_key])
            if len(rep_list) > 0:
                tmp_str = original_dict[each_key]
                real_str = ''
                i = 0
                times = len(rep_list)
                while i < times:
                    if i == times - 1:
                        real_str += (tmp_str.split(rep_list[i])[0] +
                                     self.replace_dict[rep_list[i].split('{')[1].split('}')[0]] +
                                     tmp_str.split(rep_list[i])[1])
                    else:
                        real_str += (tmp_str.split(rep_list[i])[0] +
                                     self.replace_dict[rep_list[i].split('{')[1].split('}')[0]])
                        tmp_str = tmp_str.split(rep_list[i])[1]
                    i += 1
                real_dict[each_key] = real_str
            else:
                real_dict[each_key] = original_dict[each_key]
        return real_dict
