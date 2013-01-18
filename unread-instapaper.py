# unread-instapaper.py v1.1
# View Unread Instapaper Articles in Alfred 2
# A Python Script by Kai Wells (2013)
# Probably not the most efficient way to do this, but it works!

# Based on the reddit workflow posted by Dan Palmer
# http://danpalmer.me/blog/articles/2013-01-12-reddit-workflow-for-alfred-20.html

from xml.etree import ElementTree as ET
import string
from subprocess import Popen, PIPE, STDOUT
import re

def build(USERNAME, PASSWORD):
    # GRAB DATA FROM INSTAPAPER
    raw = str(Popen('bash -i -c "curl -s --user ' + USERNAME + ':' + PASSWORD + ' https://www.instapaper.com/api/1/bookmarks/list"', shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT).communicate()).split('},{')
    # REGEX
    apos = re.compile(r"\\'")
    quot = re.compile(r"\\\"")
    t = re.compile(r"^\"title\":\"|\"$")
    multislash = re.compile(r"\\\\/")
    u = re.compile(r"^\"url\":\"|\"$")
    uidp = re.compile(r"bookmark_id|:|\"")
    d = re.compile(r"\"description\":\"|\"$")
    # BUILD OUTPUT
    xml = []
    # CHECK FOR NETWORK ERROR
    if raw != ["('', None)"]:
        # FIRST TWO ITEMS ARE DIAGNOSTIC
        del raw[0]
        del raw[0]
        for item in raw:
            temp = item.split(",")
            xml.append({
                'title': t.sub("", apos.sub("\'", quot.sub("\"", temp[3]))),
                'subtitle': d.sub("", apos.sub("\'", quot.sub("\"", quot.sub("\"", multislash.sub("/", temp[4]))))),
                'arg': u.sub("", multislash.sub("/", temp[2])),
                'uid': uidp.sub("", temp[1]),
                'icon': 'instapaper.png'
            })
    else:
        xml.append({
                'title': "No Items",
                'subtitle': "Possible Network Error",
                'arg': "http://instapaper.com/u",
                'uid': "123456"
            })
    # PLANT XML TREE
    xml_items = ET.Element('items')
    for item in xml:
        xml_item = ET.SubElement(xml_items, 'item')
        for key in item.keys():
            if key is 'uid' or key is 'arg':
                xml_item.set(key, item[key])
            else:
                child = ET.SubElement(xml_item, key)
                child.text = item[key]
    return ET.tostring(xml_items)