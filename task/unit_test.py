__author__ = 'dmy'
import logging
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt='%m-%d %H:%M',)
from task.vps import VPSSpeedTest
from orm import crud
import datetime

# from task.vps import vpsTest

# for u in vpsTest.result():
#     logging.info("%s %f"%(u['url'],u['speed']))

now=datetime.datetime.now()
for c in crud.getLatestResultHoursAgo('http://hnd-jp-ping.vultr.com/vultr.com.100MB.bin',6):
	pass
	# logging.info('latest 6 hours ago %s %d'%(u['url'],c['speed']))

for c in crud.getVPSUrlList():
	logging.info(c)


logging.info('task unit test passed.')