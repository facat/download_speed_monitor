from orm import conn
from orm import model

from sqlalchemy.orm import sessionmaker,scoped_session
Session=scoped_session(sessionmaker(bind=conn.engine))

def addVPSResult(name,url,speed,monitorTime):
    entry=model.VPSSpeed(name=name,url=url,speed=speed,monitorTime=monitorTime)
    Session.add(entry)
    Session.commit()

def getVPSResultFromTo(url,fromTime,toTime,desc=True):
    if desc:
        query=Session.query(model.VPSSpeed).filter( (model.VPSSpeed.monitorTime>=fromTime) & (model.VPSSpeed.monitorTime<=toTime)).order_by(model.VPSSpeed.monitorTime.desc())
    else:
        query=Session.query(model.VPSSpeed).filter((model.VPSSpeed.monitorTime>=fromTime) & (VPSSpeed.monitorTime<=toTime)).order_by(model.VPSSpeed.monitorTime.asc())
    ret=[]
    for q in query:
        ret.append({'url':q.url,'name':q.name,'speed':q.speed,'monitorTime':q.monitorTime})
    return ret