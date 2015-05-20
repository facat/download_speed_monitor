from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, String,DateTime, Integer
from orm import conn

Base = declarative_base()

class VPSSpeed(Base):
    __tablename__ = 'vps_speed'
    id = Column(Integer, primary_key=True)
    url = Column(String(512))
    name = Column(String(512))
    monitorTime = Column(DateTime(True))
    speed=Column(Float())

Base.metadata.create_all(conn.engine) 