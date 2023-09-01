from . import Base
from sqlalchemy import*



class Prehrana(Base):
    __tablename__="prehrane"
    id = Column(Integer,primary_key=True)
    Obrok = Column(String(15))
    Datum = Column(Date)
    Kolicina = Column(String(50))
    plan_id = Column(Integer,ForeignKey("planovi.id"))
    
    

