from . import Base
from sqlalchemy import*



class Vjezba(Base):
    __tablename__="vjezbe"
    id = Column(Integer,primary_key=True)
    Naziv_vjezbe = Column(String(20))
    Opis = Column(Text)
    Slika = Column(String(100), nullable = True)
    Video = Column(String(100), nullable = True)
  
    
