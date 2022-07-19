import unittest

from parse import parse_list, parse_detail, extract_rent


class TestParse(unittest.TestCase):
    def test_parse_list(self):
        with open("./file/list.html", encoding='utf-8') as f:
            post_list = parse_list(f.read())
        for item in post_list:
            print(item)

    def test_parse_detail(self):
        with open("./file/detail.html", encoding='utf-8') as f:
            post = parse_detail(f.read())
            print(post)

    def test_extract_rent(self):
        text = '''前面两间大的，包括带阳台的都是1300，小的那间1200，看房联系我 13028872787（电话&Vx）'''
        rent = extract_rent(text)
        print(rent)


if __name__ == '__main__':
    unittest.main()
