from orm import conn
from orm import model
import datetime
import logging
from sqlalchemy.orm import sessionmaker,scoped_session
Session=scoped_session(sessionmaker(bind=conn.engine))

def _getLatest(url):#获得最近的记录
    id=_getVPSIDFromUrl(url)    
    query=Session.query(model.VPSSpeed).filter(model.VPSSpeed.vpsID==int(id)).order_by(model.VPSSpeed.monitorTime.desc()).first()
    return query

def _getVPSIDFromUrl(url):
    query=Session.query(model.VPSList.id).filter(model.VPSList.url==url).scalar()
    return query

def _getVPSNameFromUrl(url):
    query=Session.query(model.VPSList.name).filter(model.VPSList.url==url).scalar()
    return query

def changeNameByUrl(url,name):
    query=Session.query(model.VPSList).filter(model.VPSList.url==url).one()
    query.name=name
    Session.commit()

def getLatestResultHoursAgo(url,hours):#获得最近更新时间之前n个小时的记录
    latest=_getLatest(url)
    if not latest:
        return None
    latestTime=latest.monitorTime
    fromTime=latestTime-datetime.timedelta(hours=hours)
    toTime=latestTime
    # logging.info('totime %s'%(str(toTime)))
    return getVPSResultFromTo(url,fromTime,toTime)


def getVPSUrlList():
    query=Session.query(model.VPSList.url,model.VPSList.name)
    return [{'url':x[0],'name':x[1]} for x in query]

def addVPSResult(url,speed,monitorTime):
    id=_getVPSIDFromUrl(url)
    entry=model.VPSSpeed(vpsID=id,speed=speed,monitorTime=monitorTime)
    Session.add(entry)
    Session.commit()

def getVPSResultFromTo(url,fromTime,toTime,desc=True):
    id=_getVPSIDFromUrl(url)  
    if desc:
        query=Session.query(model.VPSSpeed).filter(model.VPSSpeed.vpsID==id).filter( (model.VPSSpeed.monitorTime>=fromTime) & (model.VPSSpeed.monitorTime<=toTime)).order_by(model.VPSSpeed.monitorTime.desc())
    else:
        query=Session.query(model.VPSSpeed).filter(model.VPSSpeed.vpsID==id).filter((model.VPSSpeed.monitorTime>=fromTime) & (model.VPSSpeed.monitorTime<=toTime)).order_by(model.VPSSpeed.monitorTime.asc())
    ret=[]
    name=_getVPSNameFromUrl(url)
    for q in query:
        ret.append({'url':url,'name':name,'speed':q.speed,'monitorTime':q.monitorTime})
    return ret
def removeSession():
    Session.remove()