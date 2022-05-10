from lxml.html import fromstring
from requests_html import HTMLSession
import datetime
import requests
import json
import os

# Tiến trình 3
def crawl_page(link,author,view,comment):
    # Chạy requests_html với HTMLSession 
    # Vì khi chạy dòng dưới đây nó sẽ ghi lỗi RequestException vì thế dùng try/except để xử lý ngoại lệ
    try:
        session = HTMLSession()
        response = session.get(link)
        
    except requests.exceptions.RequestException as e:
        print(e)
    # Dưới đây cũng thế
    try:
        title_xpath = "".join(response.html.xpath("%s" %(data['title_xpath'])))     # Xử lý chuỗi với join
        body_xpath = "\n".join(response.html.xpath("%s" %(data['content_xpath'])))
        time_xpath = "".join(response.html.xpath("%s" %(data['time_xpath'])))
        img_xpath = ",".join(response.html.xpath("%s" %(data['image_xpath'])))
        # Tạo 1 dict sau đó thêm vào hàm hàm json_page
        json_page.append({"title": title_xpath, \
                            "content": body_xpath,\
                            "author": author,\
                            "time": time_xpath,\
                            "comment_count": comment,\
                            "List url image of post": img_xpath,\
                            "View Of Post": view
                    })

        #print(json_page)
        # Tạo thư mục mới
        os.makedirs("C:/Users/huyp0/Desktop/webtretho.vn/dt", mode=0o777, exist_ok=True)
    
        # Lưu file tại đây.
        with open("C:/Users/huyp0/Desktop/webtretho.vn/dt/datatest1.json", "w", encoding="utf-8") as news_file:
            json.dump(json_page, news_file, indent=4,ensure_ascii=False)
    except:
        pass
    

    
    
# Tiến trình 2
def get_links(url, num):
    for i in range(1,num+1):
        link = url.format(i) # tạo link theo trang
        # Khởi tạo requests
        try:
            session = HTMLSession()
            response = session.get(link)
            
        except requests.exceptions.RequestException as e:
            print(e)

        link_xpath =  response.html.xpath("%s" %(data["links_xpath"]))
        link_xpath = sorted(set(link_xpath), key=link_xpath.index)
        aut = response.html.find("%s" %(data["author_css"]))
        viw = response.html.xpath("%s" %(data["view_xpath"]))
        cmt = response.html.xpath("%s" %(data["cmt_xpath"]))

        #print(len(viw),len(cmt),len(aut))
        for i in range(len(link_xpath)):
            # lệnh lấy url
            clnk = data["link_domain"]+link_xpath[i]
            # Tổng các phần tử tương đương nhau vì thế sẽ dùng nhờ len của hàm link_xpath để mà dùng
            author = aut[i].text # có thể dùng .text hoặc join vì ở đây nên dùng .text là ổn nhất
            view = viw[i-1].text
            comment = cmt[i-1].text
            #print(view + comment)
            crawl_page(clnk,author,view,comment)

# Tiến trình 1
if __name__=="__main__":
    json_page = []  # Tạo list rỗng
    with open("C:/Users/huyp0/Desktop/webtretho.vn/config.json", "r") as fi: # Đọc config.json
        data = json.load(fi)
        get_links(data["cate_link"], data["num"])


     