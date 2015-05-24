__author__ = 'dmy'

import requests,time
import logging
class wget:
    def __init__(self):
        self.config = {
            'block': 4096,
        }
        self.total = 0
        self.size = 0
        self.averageSpeed=0#KB/s
    def download(self, url,lastingTime=20, headers = {}):
        self.finished=False
        block = self.config['block']
        size = self.size
        total = self.total
        if total > 0:
            logging.info("[+] Size: %dKB" % (total / 1024))
        else:
            logging.info("[+] Size: None")
        start_t = time.time()
        try:
            r = requests.get(url, stream = True, verify = False, headers = headers,timeout=lastingTime)
            for chunk in r.iter_content(chunk_size = block):
                if chunk:
                    if (time.time()-start_t)>lastingTime:
                        break
                    size += len(chunk)
                    logging.info('Now: %d, Total: %s\n' % (size, total))
            self.finished=True
            spend = time.time() - start_t
            speed = (size - self.size) / 1024 / spend
            logging.info('\nDownload Finished!\nTotal Time: %ss, Average Download Speed: %sk/s\n' % (spend, speed))
            self.averageSpeed=speed
        except Exception as e:
            logging.critical(str(e))
            logging.info("\nDownload pause.\n")
