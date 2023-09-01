from . import Base
from sqlalchemy import*


class Trening(Base):
    __tablename__="treninzi"
    id = Column(Integer,primary_key=True)
    Naziv_treninga = Column(String(20))
    Opis_treninga = Column(Text)
    plan_id = Column(Integer,ForeignKey("planovi.id"))
    

    
