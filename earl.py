from collections import OrderedDict
from urlparse import urlparse, urlunparse, parse_qsl
from urllib import urlencode
from json import dumps

class OD(OrderedDict):
    def json(self):
        return dumps(self)

    def __repr__(self):
        return self.json()

class Url(object):
    def __init__(self, url):
        self.parse_url(url)

    def parse_url(self, url):
        self.original_url = url
        self.parse()

    def parse(self):
        self.parsed_url = urlparse(self.original_url)
        self.host = self.parsed_url.netloc
        self.query = OD(parse_qsl(self.parsed_url.query))

    def unparse(self):
        l = list(self.parsed_url)
        l[4] = urlencode(self.query)
        return urlunparse(l)

    def set(self, name, value):
        self.query[name] = value
        return self

    def __getattr__(self, item):
        if item in object.__dict__:
            object.__getattribute__(self, item)
        else:
            return self.parsed_url.__getattribute__(item)

    def __repr__(self):
        return self.unparse()
