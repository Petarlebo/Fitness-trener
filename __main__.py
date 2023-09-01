from model import *
from model.relacije import *
from model.cache import region, api

korisnik = Korisnik(ime="Pero", prezime="Lebo", email="email@email.com", lozinka="123456")
session.add(korisnik)
session.commit()

korisnik2 = Korisnik(ime="Marko", prezime="Markic", email="email@email.com", lozinka="123456")
session.add(korisnik2)
session.commit()

ID = 1
KEY = f'korisnik_{ID}'
k = region.get(KEY)
print(k)
if k is api.NO_VALUE:
    k = session.query(Korisnik).filter(Korisnik.id==ID).one()
    region.set(KEY, k)
print(k.ime + " " + k.prezime)

ID2 = 2
KEY = f'korisnik_{ID2}'
k = region.get(KEY)
print(k)
if k is api.NO_VALUE:
    k = session.query(Korisnik).filter(Korisnik.id==ID2).one()
    region.set(KEY, k)
print(k.ime + " " + k.prezime)