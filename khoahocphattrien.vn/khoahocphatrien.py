from lxml.html import fromstring
import requests
import json
import os


class NewsCrawler:
    def __init__(self, categories, _directory, _links_css, _url,_title_css, _body_css, _time_css, _author_css, _number_of_page):
        self.title_css = _title_css
        self.body_css = _body_css
        self.time_css = _time_css
        self.author_css = _author_css
        self.number_of_page = _number_of_page
        self.directory = _directory
        self.categories = categories
        self.links_css = _links_css
        self.url = _url

    def crawl_page(self, link, f):
        req = requests.get(link)
        tree = fromstring(req.text)
        try:
            title = tree.cssselect(self.title_css)[0].text_content()
            # xem kỹ vị trí thẻ ở content, nó có đến 2 div con
            body = [p.text_content() for p in tree.cssselect(self.body_css)]
            time = tree.cssselect(self.time_css)[0].text_content()
            author = tree.cssselect(self.author_css)[0].text_content()


            #os.makedirs(self.directory + f, mode=0o777, exist_ok=True)
        
            with open(self.directory + f + ".txt", "a", encoding="utf-8") as my_file:
                my_file.write("\t\t" + title + "\n\n")
                my_file.write("\t\t\t\t\t\t" + time + "\n\n\n")
                my_file.write("\t" + "".join(body) + "\n")
                my_file.write("\t\t\t\t\t\t" + author + "\n\n\n\n")
                my_file.write("\n\n\n\n+++++++++++++++++++++++\n+++++++++++++++\n++++++++++++++\n")
        except:
            pass



    def get_links(self, u, file):
        for x in range(1,(self.number_of_page + 1)): 
            links = u.format(x)
            req = requests.get(links)
            tree = fromstring(req.text)
            link_css = tree.cssselect(self.links_css)
            link_css = sorted(set(link_css), key=link_css.index)
            for lik in link_css:
                # lệnh lấy url
                if 'href' in lik.attrib:
                    out = self.url + lik.attrib['href']
                    self.crawl_page(out,file)
            
                
            


    def _run_crawler(self):
        """Sau khi hoàn thiện xong hết tất cả các hàm
         rồi thì hãy gọi tất cả các hàm ở đây rồi chạy."""
        for category in self.categories:
            ct = category[35:-13].replace("/","_")
            print(ct)
            self.get_links(category, ct)
        

if __name__ == '__main__':
    file = "F:/@Study/@Social Learning/New folder/@WORDTRAINING/bt/BT END/"
    for each_file in os.listdir(file):
        if ".json" in each_file:
            #print(file + each_file)
            with open(file + each_file, "r", encoding="utf-8") as json_file:
                data = json.loads(json_file.read())
                my_crawler = NewsCrawler(categories=data.get("categories"),
                                        _directory=data.get("directory"),
                                        _links_css=data.get("css_links"),
                                        _url=data.get("url"),
                                        _title_css=data.get("css_title"),
                                        _body_css=data.get("css_body"),
                                        _time_css=data.get("css_time"),
                                        _author_css=data.get("css_author"),
                                        _number_of_page=data.get("number_of_page")
                                        )
                my_crawler._run_crawler()
        
    
    print('COMPLETE')
