from . import Base
from sqlalchemy import*
from sqlalchemy.orm import relationship


class Dio_treninga(Base):
    __tablename__="djelovi_treninga"
    id = Column(Integer,primary_key=True)
    Naziv_djela_treninga = Column(String(20))
    trening_id = Column(Integer,ForeignKey("treninzi.id"))
    
  
    
