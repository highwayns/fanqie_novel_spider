import requests
from lxml import etree
import ast

def spider(url, charmap_dic):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "priority": "u=0, i",
        "referer": "https://shimo.im/",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    et = etree.HTML(response.text)
    p_elements = et.xpath('//div[@class="muye-reader-content noselect"]//p')
    article = "\n".join([p.text for p in p_elements if p.text])
    right_article = ""
    with open(charmap_dic, "r", encoding="utf-8") as f:
        content = f.read().strip()
        dic = ast.literal_eval(content)  # 解析为字典
    for letter in article:
        if str(ord(letter))+".jpg" in dic.keys():
            right_article += dic[str(ord(letter))+".jpg"].strip()
        else:
            right_article += letter
    return right_article


if __name__ == '__main__':
    _url = "https://fanqienovel.com/reader/7076047336530510370"
    _charmap_dic = "./output/charmap_dic.txt"
    print(spider(_url, _charmap_dic))



