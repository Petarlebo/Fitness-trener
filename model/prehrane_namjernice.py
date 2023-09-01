from . import Base
from sqlalchemy import*



class Prehrana_Namjernica(Base):
    __tablename__="prehrane_namjernice"
    id = Column(Integer,primary_key=True)
    prehrana_id = Column(Integer,ForeignKey("prehrane.id"))
    namjernica_id = Column(Integer,ForeignKey("namjernice.id"))
    
  
    

