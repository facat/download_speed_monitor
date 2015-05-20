
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://dmy:abc123+_@localhost:3306/vps', echo=False,pool_recycle=3600)
    