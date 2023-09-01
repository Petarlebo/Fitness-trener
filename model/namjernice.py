from . import Base
from sqlalchemy import*



class Namjernica(Base):
    __tablename__="namjernice"
    id = Column(Integer,primary_key=True)
    Naziv = Column(String(20))
    Kalorije = Column(Integer)
    Ugljikohidrati = Column(String(20))
    Proteini = Column(String(50))
    Masti = Column(String(50))
    
