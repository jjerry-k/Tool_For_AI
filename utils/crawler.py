import os
import argparse
from icrawler.builtin import GoogleImageCrawler

def crawling(root, keyword):
    os.makedirs(os.path.join(root, keyword), exist_ok=True)
    google_crawler = GoogleImageCrawler(storage={'root_dir': os.path.join(root, keyword)})
    google_crawler.crawl(keyword=keyword, max_num=10)

def crawling_test(user, root, keyword, insert_data):
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