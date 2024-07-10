from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
    # 得到BeautifulSoup对象
    bs = BeautifulSoup(html.read(), 'html.parser')


if __name__ == '__main__':
    main()
