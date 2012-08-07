import urllib2
import re
import csv
import operator
import os

URL = 'http://www.google.com/ig/calculator?hl=en&q=1'


def convert(curr_from, curr_to):
    try:
        data=urllib2.urlopen( URL + curr_from + '%3D%3F' + curr_to).read()
    except urllib2.URLError:
        return None

    result = re.search(".*rhs: \"(\d\.\d*)", data)
    if result:
        return result.group(1)

