__author__ = 'dmy'

from speedtest.wget import wget
from orm import crud

class VPSSpeedTest():
    def __init__(self):
        self._url=None
        pass
    def _generateUrls(self):
        return crud.getVPSUrlList()
    def start(self):
        urls=self._generateUrls()
        self._url=urls
        for u in self._url:
            w=wget()
            w.download(u['url'])
            u['speed']=w.averageSpeed
    def result(self):
        return self._url
