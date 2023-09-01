from . import Base
from sqlalchemy import*


class Korisnik(Base):
    __tablename__="korisnici"
    id = Column(Integer,primary_key=True)
    ime = Column(String(25))
    prezime = Column(String(25))
    email = Column(String(100))
    lozinka = Column(String(30))

    



