#-*- coding: utf-8 -*-
import urllib
'''
1. 传入网址，网址的类型一定是字符串
2. 传入本地的网页保存路径+文件名
3. 一个函数的调用，可以定义函数的任意行为，但是必须保证传入有三个参数
  （1）到目前为止传递的数据库数量
  （2）每个数据块的大小，单位为byte，字节
  （3）远程文件的大小（有时候放回-1）
'''
def callback(a,b,c):
    '''
    @a
    @b
    @c
    '''
    down_progress = 1000*a*b/c
    if down_progress > 100:
        down_progress = 100

    print '%.2f%%'%down_progress



url = "https://www.taobao.com/"
url2 = "http://www.python.org"
save_path = '/home/zc/Python/test-tmp/iplaypython'
urllib.urlretrieve(url,save_path,callback)
# html = urllib.urlopen(url).read()
# print html
# print html.getcode()
# print html.geturl()
# print html.info()

