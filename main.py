
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
    {'url':'http://speedtest.newark.linode.com/100MB-newark.bin','name':'Linode US East'}, 
    {'url':'http://speedtest.atlanta.linode.com/100MB-atlanta.bin','name':'Linode US South'}, 
    {'url':'http://speedtest.dallas.linode.com/100MB-dallas.bin','name':'Linode US Central'}, 
    {'url':'http://speedtest.fremont.linode.com/100MB-fremont.bin','name':'Linode US West'}, 
    {'url':'http://speedtest.london.linode.com/100MB-london.bin','name':'Linode London'}, 
    {'url':'http://speedtest.singapore.linode.com/100MB-singapore.bin','name':'Linode Singapore'}, 
    {'url':'http://speedtest.tokyo.linode.com/100MB-tokyo.bin','name':'Linode Tokyo'}, 
    {'url':'http://ipv4.speedtest-nyc1.digitalocean.com/10mb.test','name':'NYC1'}, 
    {'url':'http://ipv4.speedtest-nyc2.digitalocean.com/10mb.test','name':'NYC2'}, 
    {'url':'http://ipv4.speedtest-nyc3.digitalocean.com/10mb.test','name':'NYC3'}, 
    {'url':'http://ipv4.speedtest-ams1.digitalocean.com/10mb.test','name':'AMS1'}, 
    {'url':'http://ipv4.speedtest-ams2.digitalocean.com/10mb.test','name':'AMS2'},
    {'url':'http://ipv4.speedtest-ams3.digitalocean.com/10mb.test','name':'AMS3'},
    {'url':'http://speedtest-sfo1.digitalocean.com/10mb.test','name':'SFO1'},
    {'url':'http://speedtest-sgp1.digitalocean.com/10mb.test','name':'SGP1'},
    {'url':'http://speedtest-lon1.digitalocean.com/10mb.test','name':'LON1'},
    {'url':'http://speedtest-fra1.digitalocean.com/10mb.test','name':'FRA1'},
    ]
    now=datetime.datetime.now()
    vpsTest=VPSSpeedTest()
    for t in taskList:
        vpsTest.add(t['name'],t['url'])
    vpsTest.start()
    for r in vpsTest.result():
        addVPSResult(r['name'],r['url'],r['speed'],now)
    logging.info('Finished.')