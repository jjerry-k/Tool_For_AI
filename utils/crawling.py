import os
import argparse
from icrawler.builtin import GoogleImageCrawler

def main(args):
    google_crawler = GoogleImageCrawler(storage={'root_dir': os.path.join(args.root, args.keyword)})
    google_crawler.crawl(keyword=args.keyword, max_num=50)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=str)
    parser.add_argument("--keyword", type=str)

    args = parser.parse_args()

    main(args)