import urllib2
from lxml import etree
import requests


def get_tree(url):
    # url = 'http://freedesignfile.com/category/free-vector/'
    request = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib2.urlopen(request)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    return tree

def get_xml(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    # xmlparser = etree.XMLParser()
    tree = etree.parse(response)
    return tree

xtree = get_tree('https://staterecords.org/sitemap1.xml')
urls = [el.text for el in xtree.xpath('//loc')]
print len(urls)
no_repeats = list(set(urls))
print len(no_repeats)
# with open('results.txt', 'a+') as output:
#     output.write('lorem ipsum')
print 'done'
print 'af'
with open('results.txt', 'a+') as output:
    for index, item in enumerate(no_repeats):
        print index,
        try:
            final_string = ''
            r = requests.get(item)
            final_string += item + '"'
            if r.is_redirect or len(r.history) > 0 or r.is_permanent_redirect:
                final_string += 'redirected ({})"'.format(r.url) + str(r.status_code)
            elif r.status_code != 200:
                if r.status_code == 404:
                    final_string += '404"' + str(r.status_code)
                else:
                    final_string += 'STATUS CODE"' + str(r.status_code)
            else:
                final_string += 'GOOD"' + str(r.status_code)
            output.write(final_string + '\n')
            print final_string
        except:
            print 'REQUEST ERROR'
            output.write(item + '"' + 'REQUEST ERROR')

    # print item
# for index, url in enumerate(urls):
#     print index
#     print url.text
    # print loc.text
# print 'hol'

