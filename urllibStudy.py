import urllib.request
import urllib.error

# 使用 getcode() 函数获取网页状态码，返回 200 说明网页正常，返回 404 说明网页不存在:
myURL1 = urllib.request.urlopen("https://starsound.xyz")
print(myURL1.getcode())  # 200

try:
    myURL2 = urllib.request.urlopen("https://starsounding.xyz")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(404)  # 404

    # from urllib.request import urlopen

    # 使用 urlopen 打开一个 URL，然后使用 read() 函数获取网页的 HTML 实体代码
    # myURL = urlopen("https://starsound.xyz")

    # print(myURL.read())
    # read() 是读取整个网页内容，我们可以指定读取的长度：
    # print(myURL.read(300))

    # readline() - 读取文件的一行内容
    # print(myURL.readline())

    # readlines() - 读取文件的全部内容，它会把读取的内容赋值给一个列表变量
    # lines = myURL.readlines()
    # for line in lines:
    #     print(line)
