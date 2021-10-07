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

class PruebaRemota3():
    print('Test 3')

class PruebaLocal():
    print('Test Local 1')

class PruebaLocal2():
    print('Test Local 2')

class PruebaLocal3():
    print('hola')
