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
    def download(self, url,lastingTime=20,retry=3, headers = {}):
        self.finished=False
        block = self.config['block']
        size = self.size
        total = self.total
        if total > 0:
            logging.info("[+] Size: %dKB" % (total / 1024))
        else:
            logging.info("[+] Size: None")
        for _r in range(retry):
	        start_t = time.time()
	        try:
	            r = requests.get(url, stream = True, verify = False, headers = headers,timeout=lastingTime)
	            for chunk in r.iter_content(chunk_size = block):
	                if chunk:
	                    if (time.time()-start_t)>lastingTime:
	                        break
	                    size += len(chunk)
	                    logging.debug('Now: %d, Total: %s\n' % (size, total))
	            break
	        except Exception as e:
	            logging.critical(str(e))
	            logging.info("\nDownload pause.\n")
	        finally:
	            self.finished=True
	            spend = time.time() - start_t
	            speed = (size - self.size) / 1024 / spend
	            self.averageSpeed=speed
	            logging.info('\nDownload Finished!\nTotal Time: %ss, Average Download Speed: %sk/s\n' % (spend, speed))
        
