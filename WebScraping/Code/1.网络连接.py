from urllib.request import urlopen

if __name__ == '__main__':
    html = urlopen("https://cn.bing.com/")
    print(html.read())
