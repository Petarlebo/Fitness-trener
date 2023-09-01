from . import Base
from sqlalchemy import*


class Napredak(Base):
    __tablename__="napredci"
    id = Column(Integer,primary_key=True)
    Datum = Column(Date())
    Tezina = Column(Integer)
    Visina = Column(Integer)
    Broj_ponavljanja = Column(Integer)
    Tezina_podizanja = Column(Integer)
    korisnik_id = Column(Integer,ForeignKey("korisnici.id"))
  
    

