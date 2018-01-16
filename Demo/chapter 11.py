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

import reprlib
import pprint
import textwrap
import locale
import time, os.path
import struct

from string import Template

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
    with open('myfile.zip', 'rb') as f:
        data = f.read()
    
    start = 0
    for i in range(3):
        start += 14
        fields = struct.unpack('<IIHH', data[start:start+16])
        crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

        start += 16
        filename = data[start:start+filenamesize]
        start += filenamesize
        extra = data[start:start+extra_size]
        print(filename, hex(crc32), comp_size, uncomp_size)

        start += extra_size + comp_size