# -*- coding: utf-8 -*-
import re
# s='1 22 333 4444 55555 666666'
# print re.findall(r'\b\d{3}\b',s)
# print re.findall('\\b\d{3}\\b',s)

s1='/* part1 */* part2 */'
# print re.findall(r'/*.*/*/',s1)
# print re.findall(r'/*.*/',s1)
print re.findall(r'.*',s1)

s2='aox2a'
print re.findall(r'.*',s2)
s3 = "adfad asdfasdf asdfas asdfawef asd adsfas "
ro = re.compile('(\w+)\s+\w+')
print ro.findall(s3)

# print re.findall(r'\d','sien230xxiwox99')
# print re.findall('\d','sien230xxiwox99')
# print '\w'
# print '\n'
# print '\b'
# print '\d'
