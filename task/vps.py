__author__ = 'dmy'

from speedtest.wget import wget

class VPSSpeedTest():
    def __init__(self):
        self._url=[]
        pass
    def add(self,name,url):
        self._url.append({'url':url,'name':name})
    def start(self):
        for u in self._url:
            w=wget()
            w.download(u['url'])
            u['speed']=w.averageSpeed
    def result(self):
        return self._url
