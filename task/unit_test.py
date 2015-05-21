__author__ = 'dmy'

from task.vps import VPSSpeedTest
import logging

vpsTest=VPSSpeedTest()
vpsTest.add('(Asia) Tokyo, Japan','http://hnd-jp-ping.vultr.com/vultr.com.100MB.bin')
vpsTest.add('(AU) Sydney, Australia','http://syd-au-ping.vultr.com/vultr.com.100MB.bin')
vpsTest.add('(EU) Frankfurt, DE','http://fra-de-ping.vultr.com/vultr.com.100MB.bin')
vpsTest.start()

for u in vpsTest.result():
    logging.info("%s %f"%(u['url'],u['speed']))