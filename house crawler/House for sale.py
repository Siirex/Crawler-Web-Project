# import package
import os
import requests
from lxml.html import fromstring




# crawl data
# links https://batdongsan.com.vn/ban-nha-dat --> checked error
# https://alonhadat.com.vn/can-ban-nha.htm
link = "https://alonhadat.com.vn/can-ban-nha.htm"
link1 = "https://alonhadat.com.vn/can-ban-nha-ha-noi-t1.htm"
link2 = "https://alonhadat.com.vn/chinh-chu-ban-nha-so-59-ngo-193-phu-dien-60m2-nha-3-tang-gia-5-5-ty-9460243.html"
def crawl_page(link):
    req = requests.get(link)
    tree = fromstring(req.text)
    title = "\n".join(tree.xpath("//div[@class='title']//h1//text()"))
    time = "\n".join(tree.xpath("//div[@class='title']//span//text()"))
    price = "\n".join(tree.xpath("//span[@class='price']//span[2]//text()"))
    square = "\n".join(tree.xpath("//span[@class='square']//span[2]//text()"))
    address = "\n".join(tree.xpath("//div[@class='address']//span[2]//text()"))
    body = "|".join(tree.xpath("//tr//td[2]//text()")) + "|" + "|".join(tree.xpath("//tr//td[4]//text()"))
    cot2 = title + "|" + time + "|" + price + "|" + square + "|" + address + "|" + body
    cot2 = cot2.replace("Ngày đăng:", "")
    cot2 = cot2.replace(",",".")
    cot2 = cot2.replace("\n","")
    cot2 = cot2.replace("|",",")
    #print(cot2 + "\n")
    with open("D:/[NORII]/TADDEZ/XX___House/dataset/data-house-5.txt", "a", encoding="utf-8") as my_file:
        my_file.write(cot2 + "\n")
    



def Cotchinh():
    link2 = "https://alonhadat.com.vn/chinh-chu-ban-nha-so-59-ngo-193-phu-dien-60m2-nha-3-tang-gia-5-5-ty-9460243.html"
    req = requests.get(link2)
    tree = fromstring(req.text)
    ttprice = "\n".join(tree.xpath("//span[@class='price']//span[1]//text()"))
    ttsquare = "\n".join(tree.xpath("//span[@class='square']//span[1]//text()"))
    ttaddress = "\n".join(tree.xpath("//div[@class='address']//span[1]//text()"))
    ttb = ",".join(tree.xpath("//tr//td[1]//text()")) + "," + ",".join(tree.xpath("//tr//td[3]//text()"))
    cot1 = "Title" + "," + "Time" + "," + ttprice + "," + ttsquare + "," + ttaddress + "," + ttb
    cot1 = cot1.replace(" :", "")
    return cot1


def get_links(u,numb):
    for x in range(1,(numb + 1)): 
        links = (u.replace(".htm","/trang-{}.htm")).format(x)
        print(links)
        req = requests.get(links)
        tree = fromstring(req.text)
        xpath_links = tree.xpath("//div[@class='ct_title']//@href")
        xpath_links = sorted(set(xpath_links), key=xpath_links.index)  
        for elink in xpath_links:
            url_link = "https://alonhadat.com.vn" + elink
            crawl_page(url_link)
            #print(url_link)



#f = os.makedirs("D:/[NORII]/TADDEZ/XX___House/dataset", mode=0o777, exist_ok=True)
with open("D:/[NORII]/TADDEZ/XX___House/dataset/data-house-5.txt", "w", encoding="utf-8") as my_file:
    my_file.write(Cotchinh())
    my_file.write("\n")

get_links(link1,20)



