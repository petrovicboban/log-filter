import sys 
sys.path.append('.')

import log_filter
from unittest import mock, TestCase
from io import StringIO
import pytest

contents = '''
157.55.39.181 - - [02/Jun/2015:17:08:16 -0700] "GET /images/antiwarphotos.htm HTTP/1.1" 200 1930 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" "redlug.com"
31.184.238.128 - - [02/Jun/2015:17:09:03 -0700] "GET /logs/access.log HTTP/1.1" 200 4778 "http://www.theknot.com/wedding/zantac-and-no" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36" "redlug.com"

151.80.31.151 - - [02/Jun/2015:17:10:38 -0700] "GET /Scandals.htm HTTP/1.1" 200 12812 "-" "Mozilla/5.0 (compatible; AhrefsBot/5.0; +http://ahrefs.com/robot/)" "redlug.com"
31.184.238.128 - - [02/Jun/2015:17:09:03 -0700] "GET /logs/access.log HTTP/1.1" 200 4778 "http://www.theknot.com/wedding/zantac-and-no" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36" "redlug.com"
'''


def test_ip_validation():
    assert log_filter.validate('1.1.1.1') == True 
    assert log_filter.validate('1.1.1.698') == False
    assert log_filter.validate('1.1.1.1/24') == True 
    assert log_filter.validate('1.1.1.1/56') == False


class TestFilter(TestCase):

    @mock.patch("sys.stdin", StringIO(contents))
    def test_filtering_1(self):
        lines = []
        for line in log_filter.filter('157.55.39.181'):
            lines.append(line)
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0], '157.55.39.181 - - [02/Jun/2015:17:08:16 -0700] "GET /images/antiwarphotos.htm HTTP/1.1" 200 1930 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" "redlug.com"\n')

    @mock.patch("sys.stdin", StringIO(contents))
    def test_filtering_2(self):
        lines = []
        for line in log_filter.filter('31.184.238.128'):
            lines.append(line)
        self.assertEqual(len(lines), 2)

    @mock.patch("sys.stdin", StringIO(contents))
    def test_filtering_3(self):
        lines = []
        for line in log_filter.filter('31.184.238.121'):
            lines.append(line)
        self.assertEqual(len(lines), 0)

    @mock.patch("sys.stdin", StringIO(contents))
    def test_filtering_4(self):
        lines = []
        with pytest.raises(SystemExit):
            for line in log_filter.filter('31.184.238.1219'):
                lines.append(line)

    @mock.patch("sys.stdin", StringIO(contents))
    def test_filtering_5(self):
        lines = []
        for line in log_filter.filter('0.0.0.0/0'):
            lines.append(line)
        self.assertEqual(len(lines), 4)

