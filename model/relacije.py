from sqlalchemy.orm import relationship

from .korisnici import Korisnik
from .djelovi_treninga import Dio_treninga
from .namjernice import Namjernica
from .napredci import Napredak
from .planovi_vjezbe import Plan_Vjezba
from .planovi import Plan
from .prehrane_namjernice import Prehrana_Namjernica
from .prehrane import Prehrana
from .treninzi import Trening
from .vjezbe import Vjezba
from . import Base
from . import engine

Korisnik.planovi = relationship("Plan", back_populates="korisnik")
Korisnik.napredak = relationship("Napredak", back_populates="korisnik")
Dio_treninga.trening = relationship("Trening", back_populates="djelovi_treninga")
Napredak.korisnik = relationship("Korisnik", back_populates="napredak")
Namjernica.prehrana_namjernica = relationship("Prehrana_Namjernica", back_populates="namjernica")
Plan_Vjezba.plan = relationship("Plan", back_populates="plan_vjezba")
Plan_Vjezba.vjezba = relationship("Vjezba", back_populates="plan_vjezba")
Plan.korisnik = relationship("Korisnik", back_populates="planovi")
Plan.treninzi = relationship("Trening", back_populates="plan")
Plan.prehrane = relationship("Prehrana", back_populates="plan")
Plan.plan_vjezba = relationship("Plan_Vjezba", back_populates="plan")
Prehrana_Namjernica.prehrana = relationship("Prehrana", back_populates="prehrana_namjernica")
Prehrana_Namjernica.namjernica = relationship("Namjernica", back_populates="prehrana_namjernica")
Prehrana.plan = relationship("Plan", back_populates="prehrane")
Prehrana.prehrana_namjernica = relationship("Prehrana_Namjernica", back_populates="prehrana")
Trening.plan = relationship("Plan", back_populates="treninzi")
Trening.djelovi_treninga = relationship("Dio_treninga", back_populates="trening")
Vjezba.plan_vjezba = relationship("Plan_Vjezba", back_populates="vjezba")


Base.metadata.bind = engine
Base.metadata.create_all(engine)


