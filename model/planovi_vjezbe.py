from . import Base
from sqlalchemy import*


class Plan_Vjezba(Base):
    __tablename__="planovi_vjezbe"
    id = Column(Integer,primary_key=True)
    plan_id = Column(Integer,ForeignKey("planovi.id"))
    vjezba_id = Column(Integer,ForeignKey("vjezbe.id"))
    
  
    
