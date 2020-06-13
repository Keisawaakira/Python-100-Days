"""
第一个Python程序 - hello, world!
向伟大的Dennis M. Ritchie先生致敬

Version: 0.1
Author: 骆昊
Date: 2018-02-26

请将该文件命名为hello.py

使用Windows的小伙伴可以在命令行提示下通过下面的命令运行该程序
python hello.py

对于使用Linux或macOS的小伙伴可以打开终端并键入下面的命令来运行程序
python3 hello.py
"""

print('hello, world!')
# print("你好,世界！")
# 解释框内的任何东西不会执行
print('你好', '世界')
# 字符串之间默认以空格连接
print('hello', 'world', sep=', ', end='!')
# 字符串之间以sep的值连接，以end中的值结尾
print('goodbye, world', end='!\n')
# end中默认存在换行符\n，如果自定义值的话没换行符则输出于同一行。
