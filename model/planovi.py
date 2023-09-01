from . import Base
from sqlalchemy import *


class Plan(Base):
    __tablename__="planovi"
    id = Column(Integer,primary_key=True)
    Naziv_vjezbe = Column(String(20))
    Opis = Column(Text)
    Tip_plana = Column(String(30))
    korisnik_id = Column(Integer, ForeignKey("korisnici.id"))
  
    
