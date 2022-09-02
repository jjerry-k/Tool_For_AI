import os
from icrawler.builtin import GoogleImageCrawler

def crawling(user: str, root: str, keyword: str, insert_data: function):
    class_path = os.path.join(root, user, keyword)
    os.makedirs(class_path, exist_ok=True)
    google_crawler = GoogleImageCrawler(storage={'root_dir':class_path})
    
    google_crawler.crawl(keyword=keyword, max_num=10)
    
    data = {
        "username": user,
        "keyword": keyword,
        "classname": keyword,
        "data": os.listdir(class_path)
    }
    insert_data(data)