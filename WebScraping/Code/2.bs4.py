"""
[1]解析器。
    html.parser解析器
    lxml解析器
    html5lib解析器
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# 在这里，我们使用html.parser解析器解析了这个html页面
bs = BeautifulSoup(html.read(), "html.parser")
# 我们在这里输出这个页面的第一个h1标签
print(bs.h1)

# 输出
# <h1>An Interesting Title</h1>
