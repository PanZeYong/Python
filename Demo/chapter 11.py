#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 11 标注库浏览 - Part II

# 1、输出格式:
# reprlib
# pprint：以可读的方式深入控制内置和用户自定义的对象的打印
# textwrap：格式化文本段落以适应设定的屏宽
# locale：按访问预定好的国家信息数据库

import reprlib
import pprint
import textwrap
import locale

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