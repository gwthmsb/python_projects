"""
To find html tags

"""

import re, collections

reg = "(?<=<)\s*[a-zA-Z]+"

ordered_dict = collections.OrderedDict()

def find_tag(line):
    for match in re.finditer(reg, line):
        tag = match.group()
        ordered_dict[tag] = tag


def test_find_tag():
    find_tag("<div> <p>")
    find_tag("<p> <html>")
    print(ordered_dict.keys())
