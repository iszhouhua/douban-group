import datetime
import unittest

from crawler import crawl_list, crawl_detail


class TestCrawler(unittest.TestCase):
    def test_crawl_list(self):
        start_time = datetime.datetime.combine(datetime.date(2022, 7, 14), datetime.time.min)
        post_list = crawl_list("106955", start_time)
        for post in post_list:
            print(post)

    def test_crawl_detail(self):
        start_time = datetime.datetime.combine(datetime.date(2022, 7, 14), datetime.time.min)
        detail = crawl_detail("https://www.douban.com/group/topic/271153816/", start_time)
        print(detail)


if __name__ == '__main__':
    unittest.main()
