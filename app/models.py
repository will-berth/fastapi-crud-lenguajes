from sqlalchemy import Column, Integer, String
from .Conexion import Base

class Lenguaje(Base):
    __tablename__ = 'lenguaje'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20))

class TestRemote():
    pass

class TestRemote2():
    pass

class TestLocal():
    pass

class TestLocal2():
    pass

class PruebaRemota():
    print('Test 1')

class PruebaRemota2():
    print('Test 2')
