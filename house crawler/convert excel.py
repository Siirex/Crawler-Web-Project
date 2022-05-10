import os
import requests
from lxml.html import fromstring
import pandas as pd


def Cotchinh():
    link2 = "https://alonhadat.com.vn/chinh-chu-ban-nha-so-59-ngo-193-phu-dien-60m2-nha-3-tang-gia-5-5-ty-9460243.html"
    req = requests.get(link2)
    tree = fromstring(req.text)
    ttprice = "".join(tree.xpath("//span[@class='price']//span[1]//text()"))
    ttsquare = "".join(tree.xpath("//span[@class='square']//span[1]//text()"))
    ttaddress = "".join(tree.xpath("//div[@class='address']//span[1]//text()"))
    ttb = ",".join(tree.xpath("//tr//td[1]//text()")) + "," + ",".join(tree.xpath("//tr//td[3]//text()"))
    cot1 = "Title" + "," + "Time" + "," + ttprice + "," + ttsquare + "," + ttaddress + "," + ttb
    cot1 = cot1.replace(":", "")
    return cot1


columns = Cotchinh().split(",")
df = pd.read_csv('D:/[NORII]/TADDEZ/XX___House/dataset/data-house-5.txt', encoding="utf-8", on_bad_lines='skip')
df.columns = columns
print(df.head(5))
df.to_excel("D:/[NORII]/TADDEZ/XX___House/dataset/data-5.xlsx", index=False)
