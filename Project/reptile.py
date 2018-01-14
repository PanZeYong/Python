#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 这是一个爬取网页 API 数据的例子

import requests
import random
import time
import urllib
import json
import http.cookiejar
import os
import re
import io

try:
    # Python 3
    from urllib.parse import urlparse, parse_qs
except ImportError:
    # Python 2
    from urlparse import urlparse, parse_qs

LOGIN_URL = 'https://ucenter.17zuoye.com/j_spring_security_check'
BASE_URL = "https://www.17zuoye.com/"
Error = 'Error'

proxy = { 'http://111.231.192.61:8080' }



timeout = random.choice(range(80, 180))
cookie_filename = 'cookie.txt'

headers = { 
     'Connection': 'keep-alive',
     'Content-Type': 'application/x-www-form-urlencoded',
     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
     'Origin': 'https://www.17zuoye.com'
}

class Task:
    def __init__(self):
        # self.proxy_support = urllib.request.ProxyHandler({ 'proxy': proxy})
        self.cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
        self.handler = urllib.request.HTTPCookieProcessor(self.cookie)
        self.opener = urllib.request.build_opener(self.handler)
        
    def login(self):
        params = {
            'j_username': '18933357778',
            'j_password': 'test123',
            '_spring_security_remember_me': 'on',
            '_a_loginForm': "登录"
        }
        # user_agent ＝ r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

        postdata = urllib.parse.urlencode(params).encode()

        # headers = {
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        #     'Accept-Encoding': 'gzip, deflate, br',
        #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        #     'Connection': 'keep-alive',
        #     'Content-Type': 'application/x-www-form-urlencoded',
        #     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36'
        # }
        request = urllib.request.Request(LOGIN_URL, postdata, headers)

        try:
            response = self.opener.open(request)
            if (response.status == 200):
                url = response.url
                o = urlparse(url)
                key = parse_qs(o.query)['key'][0];
                params = { 'j_key': key, 'j_userType': 'TEACHER' }
                postdata = urllib.parse.urlencode(params).encode()
                request = urllib.request.Request(LOGIN_URL, postdata, headers)

                try:
                    response = self.opener.open(request)
                    if (response.status == 200):
                        return True
                    else:
                        return False
                except urllib.error.URLError as e:
                    print(e.code, ':', e.reason)
            else:
                return False
        except urllib.error.URLError as e:
            print(e.code, ':', e.reason)

    def convert_to_json(self, response):
        return json.loads(response.read().decode('utf-8'))

    # 获取每个年级对应的语文版本（包括上下册）
    def get_grade_book(self, level, term):
        params = { 'level': level, 'term': term, 'subject': 'CHINESE' }
        headers = { 
            'Connection': 'keep-alive', 
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0' 
        }
        queryParams = urllib.parse.urlencode(params)
        request = urllib.request.Request(BASE_URL + 'teacher/new/homework/sortbook.api?' + queryParams, None, headers)

        try:
            response = self.opener.open(request);
            if response.status == 200:
                data = self.convert_to_json(response)
                if data['success']:
                    return data['rows']
                else :
                    return False        
            else:  
                print('Version ' + data)
                return False             
        except urllib.error.URLError as e:
            print(e.code, ':', e.reason)

    # 通知服务器选哪一本书
    def change_book(self, book_id):
        params = { 'clazzs': '36788084_10440790,36775687_10440792,36788085_10440791', 'bookId': book_id, 'subject': 'CHINESE'}
        postdata = urllib.parse.urlencode(params).encode()
        request = urllib.request.Request(BASE_URL + 'teacher/new/homework/changebook.api', postdata, headers, timeout)

        try:
            response = self.opener.open(request);
            if response.status == 200:
                data = self.convert_to_json(response)
                if data['success']:
                    return True
                else:
                    return False
            else:
                print('Book: ' + data)
                return False
        except urllib.error.URLError as e:
            print(e.code, ":", e.reason)
    
    # 获取每本书的目录
    def get_book_dir(self):
        params = { 'clazzs': '36788084_10440790,36775687_10440792,36788085_10440791', 'isTermEnd': 'false', 'subject': 'CHINESE' }
        queryParams = urllib.parse.urlencode(params)
        request = urllib.request.Request(BASE_URL + 'teacher/new/homework/clazz/book.api?' + queryParams, None, headers)

        try:
            response = self.opener.open(request);
            if response.status == 200:
                data = self.convert_to_json(response)
                if data['success']:
                    return data['clazzBook']
                else:
                    print('Dir: ' + data)
                    return False
        except urllib.error.URLError as e:
            print(e.code, ":", e.reason)

    # 获取每本书每单元每小节所包含的部分（基础知识、阅读、课文读背、配套试卷）
    def get_list(self, book_id, unit_id, sections):
        params = { 'bookId': book_id, 'unitId': unit_id, 'sections': sections, 'subject': 'CHINESE' }
        queryParams = urllib.parse.urlencode(params)
        request = urllib.request.Request(BASE_URL + 'teacher/new/homework/objective/list.api?' + queryParams, None, headers)

        try:
            response = self.opener.open(request);
            if response.status == 200:
                data = self.convert_to_json(response)
                if data['success']:
                    objectiveList = data['objectiveList']
                    for objective in objectiveList:
                        if not (objective['objectiveName'] == '阅读'):
                            continue
                        else:
                            return objective
                    return False
                else:
                    print('Read: ' + data)
                    return False
        except urllib.error.URLError as e:
            print(e.code, ":", e.reason)

    # 获取每小节所包含阅读相关题目 id
    def get_content_id(self, book_id, unit_id, sections, types, subject, objective_config_id):
        params = { 'bookId': book_id, 'unitId': unit_id, 'sections': sections, 'type': types, 'subject': subject, 'objectiveConfigId': objective_config_id }
        queryParams = urllib.parse.urlencode(params)
        request = urllib.request.Request(BASE_URL + 'teacher/new/homework/objective/content.api?' + queryParams, None, headers)

        try:
            response = self.opener.open(request);
            if response.status:
                data = self.convert_to_json(response)
                if data['success']:
                    return data['content']
                else:
                    print('Id: ' + data)
                    return False
        except urllib.error.URLError as e:
            print(e.code, ":", e.reason)

    # 通过 id 获取每道题目
    def get_questions_by_ids(self, data):
        params = { 'data': data }
        postdata = urllib.parse.urlencode(params).encode()
        request = urllib.request.Request(BASE_URL + 'exam/flash/load/question/byids.vpage', postdata, headers)

        try:
            response = self.opener.open(request);
            if response.status == 200:
                data = self.convert_to_json(response)
                return data['result']
            else:
                print('Question: ' + data)
                return False
        except urllib.error.URLError as e:
            print(e.code, ":", e.reason)

    def get_grade(self, level, term):
        if (level == 3 and term == 1):
            return '三年级上'
        elif (level == 3 and term == 2):
            return '三年级下'
        elif (level == 4 and term == 1):
            return '四年级上'
        elif (level == 4 and term == 2):
            return '四年级下'
        elif (level == 5 and term == 1):
            return '五年级上'
        elif (level == 5 and term == 2):
            return '五年级下'
        elif (level == 6 and term == 1):
            return '六年级上'
        elif (level == 6 and term == 2):
            return '六年下'
        else:
            pass

    def mkdir(self, path):
        path = path.strip()

        isExists = os.path.exists(path)

        if not isExists:
            os.makedirs(path)
            return True
        else:
            return False
            
if __name__ == '__main__':
    task = Task()
    if (task.login()):
        print("Login Success")
        # task.get_grade_book(3, 1)
        # task.change_book('BK_10100000016697')
        # task.get_book_dir()
        # task.get_list('BK_10100000016697', 'BKC_10100000723387', 'BKC_10100074686586')
        # task.get_content_id('BK_10100000016697', 'BKC_10100000723387', 'BKC_10100074686586', 'CHINESE_READING', 'CHINESE', 'OCN_01577005274')
        # task.get_questions_by_ids(json.dumps({ "ids": ["Q_10101080881506-1"]}))

        # 3 ~ 6 年级对应上下册
        grades = [ [3, 1], [3, 2], [4, 1], [4, 2], [5, 1], [5, 2], [6, 1], [6, 2] ]
        path = '../一起作业语文阅读数据/'
        sectionCount = 0;
        

        for row in grades:
            rows = task.get_grade_book(row[0], row[1])
            name = task.get_grade(row[0], row[1])
            path += name + '/'
            # print('Grade: ' + path)
            # totalCount = 0

            if rows:
                for teaching_material in rows:
                    path += teaching_material['name'] + '/'
                    # print('Book: ' + path)

                    dir = task.change_book(teaching_material['id'])
                    if dir:
                        # print('更换教材成功')
                        book = task.get_book_dir()
                        book_id = book['bookId']

                        if book:
                            # print('成功获取每本书目录')                            
                            unit_list = book['unitList']
                            # bookCount = 0

                            for unit in unit_list:
                                path += unit['cname'] + '/'
                                unit_id = unit['unitId']
                                sections = unit['sections']
                                # unitCount = 0
                                
                                # print('Unit: ' + path)

                                for section in sections:
                                    path += section['cname'] + '/'
                                    section_id= section['sectionId']
                                    read = task.get_list(book_id, unit_id, section_id)
                                    # print('Section: ' + path)
                                    if read:
                                        # print("获取成功")                                        
                                        typeList = read['typeList']
                                        for types in typeList:
                                            objective_config_id = types['objectiveConfigId']
                                            read_type = types['type']
                                            contents = task.get_content_id(book_id, unit_id, section_id, read_type, 'CHINESE', objective_config_id)
                                            
                                            if contents:
                                                # print('成功获取内容 id')
                                                for content in contents:
                                                    questions = content['questions']
                                                    
                                                    if task.mkdir(path):
                                                        for question in questions:
                                                        # ids.append(question['id'])
                                                            params = { 
                                                                'ids': [
                                                                    question['id']
                                                                ] 
                                                            }                                                    
                                                            result = task.get_questions_by_ids(json.dumps(params))
                                                            
                                                            with open(path + question['id'] + '.json', 'w+', encoding='utf-8') as f:
                                                                json.dump(result, f, ensure_ascii=False)
                                                                sectionCount = sectionCount + 1
                                                                print(path + question['id'] + '.json' + '-' + str(sectionCount))
                                                    else:
                                                        pass
                                                    # with open(path + 'question.json', 'w') as f:
                                                    #     json.dump(result, f) 
                                                    # print(result)
                                            else:
                                                print('失败获取内容 id: ')
                                    else:
                                        print("获取失败")
                                    time.sleep(10)
                                    # unitCount += sectionCount
                                    path = path[0:(len(path) - len(section['cname']) - 1)]

                                path = path[0 : (len(path) - len(unit['cname']) - 1)]
                                # bookCount += unitCount
                        else:
                            print('失败获取每本书目录')
                        
                    else:
                        print('更换教材失败')
                    # print("\n")
                    path = path[0 : (len(path) - len(teaching_material['name']) - 1)]
                    # totalCount += bookCount
                    time.sleep(20)                                        
            else:
                print("Network Error")

            path = path[0 : (len(path) - len(name) - 1)]
            print('Again: ' + path)
            print(sectionCount)
            
    else:
        print("Login Fail")