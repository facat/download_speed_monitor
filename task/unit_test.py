__author__ = 'dmy'
import logging
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt='%m-%d %H:%M',)
from task.vps import VPSSpeedTest
from orm import crud
import datetime

vpsTest=VPSSpeedTest()
# vpsTest.add('(Asia) Tokyo, Japan','http://hnd-jp-ping.vultr.com/vultr.com.100MB.bin')
# vpsTest.add('(AU) Sydney, Australia','http://syd-au-ping.vultr.com/vultr.com.100MB.bin')
vpsTest.add('(EU) Frankfurt, DE','http://fra-de-ping.vultr.com/vultr.com.100MB.bin')
vpsTest.start()

for u in vpsTest.result():
    logging.info("%s %f"%(u['url'],u['speed']))

now=datetime.datetime.now()
for u in vpsTest.result():
	crud.addVPSResult(u['name'],u['url'],u['speed'],now)
for u in vpsTest.result():
	result=crud.getVPSResultFromTo(u['url'],now-datetime.timedelta(seconds=1),now+datetime.timedelta(seconds=1))
	assert abs(result[0]['monitorTime']-now).seconds==0
	crud.getLatest(u['url']).monitorTime==now
	for c in crud.getLatestResultHoursAgo(u['url'],6):
		logging.info('latest 6 hours ago %s %d'%(u['url'],c['speed']))

for c in crud.getVPSUrlList():
	logging.info(c)


logging.info('task unit test passed.')