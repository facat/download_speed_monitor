
import logging
logging.basicConfig(level=logging.INFO,filename='/home/cubie/log/vps.log',
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt='%m-%d %H:%M',)
#import unit_test
# from orm import model
from task.vps import VPSSpeedTest
from orm.crud import addVPSResult
import datetime
if __name__=='__main__':
    taskList=[{'url':'http://hnd-jp-ping.vultr.com/vultr.com.100MB.bin','name':'(Asia) Tokyo, Japan'},
    {'url':'http://fra-de-ping.vultr.com/vultr.com.100MB.bin','name':'(EU) Frankfurt, DE'},
    {'url':'http://ams-nl-ping.vultr.com/vultr.com.100MB.bin','name':'(EU) Amsterdam, NL'},
    {'url':'http://lon-gb-ping.vultr.com/vultr.com.100MB.bin','name':'(EU) London, UK'},
    {'url':'http://par-fr-ping.vultr.com/vultr.com.100MB.bin','name':'(EU) Paris, France'},
    {'url':'http://syd-au-ping.vultr.com/vultr.com.100MB.bin','name':'(AU) Sydney, Australia'},
    {'url':'http://wa-us-ping.vultr.com/vultr.com.100MB.bin','name':'Seattle, Washington'},
    {'url':'http://sjo-ca-us-ping.vultr.com/vultr.com.100MB.bin','name':'Silicon Valley, California'},
    {'url':'http://lax-ca-us-ping.vultr.com/vultr.com.100MB.bin','name':'Los Angeles, California'},
    {'url':'http://il-us-ping.vultr.com/vultr.com.100MB.bin','name':'Chicago, Illinois'},
    {'url':'http://nj-us-ping.vultr.com/vultr.com.100MB.bin','name':'New York / New Jersey'},
    {'url':'http://tx-us-ping.vultr.com/vultr.com.100MB.bin','name':'Dallas, Texas'},
    {'url':'http://ga-us-ping.vultr.com/vultr.com.100MB.bin','name':'Atlanta, Georgia'},
    {'url':'http://fl-us-ping.vultr.com/vultr.com.100MB.bin','name':'Miami, Florida'}, 
    ]
    vpsTest=VPSSpeedTest()
    for t in taskList:
        vpsTest.add(t['name'],t['url'])
    vpsTest.start()
    now=datetime.datetime.now()
    for r in vpsTest.result():
        addVPSResult(r['name'],r['url'],r['speed'],now)
    print('Finished.')