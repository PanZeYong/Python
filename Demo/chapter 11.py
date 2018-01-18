#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 11 标注库浏览 - Part II

# 1、输出格式:
# reprlib
# pprint：以可读的方式深入控制内置和用户自定义的对象的打印
# textwrap：格式化文本段落以适应设定的屏宽
# locale：按访问预定好的国家信息数据库
# 2、模板
# Template：字符串模板
# struct: 二进制数据记录布局
# 3、多线程：threading
# 4、日志：logging
# 5、弱引用：weakref
# 6、列表工具：array、collections、bisect（存储链表）

import reprlib
import pprint
import textwrap
import locale
import time, os.path
import struct
import threading, zipfile
import logging
import weakref, gc
import bisect
from string import Template
from array import array
from collections import deque
from heapq import heapify, heappop, heappush

if __name__ == '__main__':
    
    # reprlib
    print(reprlib.repr(set('supercalifragilisticexpialidocious')))
    
    # pprint
    t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
    pprint.pprint(t, width=30)

    # textwrap
    doc = """The wrap() method is just like fill() except that it returns 
    a list of strings instead of one big string with newlines to separate 
    the wrapped lines."""
    print(textwrap.fill(doc, width=40))

    # locale
    # print(locale.setlocale(locale.ja_JP, 'English_United States.1252'))
    conv = locale.localeconv();
    print(conv)
    print(locale.format("%d", 1234567.8, grouping=True))
    print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], 1234567.8), grouping=True))

    # Template
    t = Template('${village}folk send $$10 to $cause')
    print(t.substitute(village='Nottingham', cause='the ditch fund'))
    s = Template('Return the $item to $owner.')
    d = dict(item='unladen swallow')
    s.safe_substitute(d)

    photofiles = ['img_1074', 'img_1076.jpg', 'img_1077.jpg']

    class BatchRename(Template):
        delimiter = '%'
    
    fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
    img = BatchRename(fmt)
    date = time.strftime('%d%b%y')
    for i, filename in enumerate(photofiles):
        base, ext = os.path.splitext(filename)
        newname = img.substitute(d=date, n=i, f=ext)
        print('{0} --> {1}'.format(filename, newname))
    
    # struct
    with open('wrond.md.zip', 'rb') as f:
        data = f.read()
    
    start = 0
    # for i in range(3):                      # show the first 3 file headers
    #     start += 14
    #     fields = struct.unpack('<IIIHH', data[start:start+16])
    #     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    #     start += 16
    #     filename = data[start:start+filenamesize]
    #     start += filenamesize
    #     extra = data[start:start+extra_size]
    #     print(filename, hex(crc32), comp_size, uncomp_size)

    #     start += extra_size + comp_size     # skip to the next header

    # threading
    class AsyncZip(threading.Thread):
        def __init__(self, infile, outfile):
            threading.Thread.__init__(self)
            self.infile = infile
            self.outfile = outfile
        
        def run(self):
            f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
            f.write(self.infile)
            f.close()
            print('Finished background zip of:', self.infile)
    
    background = AsyncZip('new_reques.json.zip', 'wrond.md.zip')
    background.start()
    print('The main program continues to run in foreground')

    # loggin
    print(logging.debug('Debugging information'))
    logging.info('Informational message')
    print(logging.warning('Warning:config file %s not found', 'server.conf'))
    print(logging.error('Critical error -- shutting down'))

    # weakref
    # class A:
    #     def __init__(self, value):
    #         self.value = value
    #     def __repr__(self):
    #         return str(self.value)

    # a = A(10)                # create a reference
    # d = weakref.WeakKeyDictionary()
    # d['primary'] = a
    # print(d['primary']);

    # array：存储数据
    a = array('H', [4000, 10, 700, 22222])
    print(sum(a))
    print(a[1:3])

    # collections
    d = deque(["task1", "task2", "task3"])
    d.append("task4")
    print("Handling", d.popleft())
    
    # unsearched = deque([starting_node])
    # def breadth_first_search(unsearched):
    #     node = unsearched.popleft()
    #     for m in gen_moves(node):
    #         if is_goal(m):
    #             return m
    #         unsearched.append(m)
    # bisect
    scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
    bisect.insort(scores, (300, 'ruby'))
    print(scores)
    # heapq
    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    heapify(data)
    heappush(data, -5)
    print([heappop(data) for i in range(3)])
