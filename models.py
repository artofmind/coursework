from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import zope.sqlalchemy import ZopeTransactionExtension

engine = create_engine('sqLite:///base.db')
Session = sessionmaker(bind=engine,
                       extension=ZopeTransactionExtension())
Base = declarative_base(bind=engine)

association_table = Table('association', Base.metadata,
 Column('id_Order', Integer, ForeignKey('Order.id_Order')),
 Column('id_Tovar', Integer, ForeignKey('Tovar.id_Tovar'))
 )
 
class User(Base):
       _tablename_ = 'user'
       id_User = Column(Integer, primary_key=True)
       name_User = Column(Unicode(255), nullable=False)
       lastName_User = Column(Unicode(255), nullable=False)
       email = Column(Unicode(255), unique=True, nullable=False)
       
def _repr_(self, name_User, lastName_User, email):
       self.name_User = name_User
       self.lastName_User = lastName_User
       self.email = email
            
class Tovar(Base):
       _tablename_ = 'tovar'
       id_Tovar = Column(Integer, primary_key=True)
       name_Tovar = Column(Unicode(255), unique=True, nullable=False)
       price_Tovar = Column(Integer)
       
def _repr_(self, name_Tovar, price_Tovar):
       self.name_Tovar = name_Tovar
       self.price_Tovar = price_Tovar
       
class Order(Base):
      _tablename_ = 'order')
      id_Order = Column(Integer, primary_key=True)
      Tovars = relationship("Tovar",
                            secondary=association_table)
      id_User = Column(Integer, ForeignKey('User.id_User'))
      price_Order = Column(Integer)
      sale = Column(Integer)
      
def _repr_(self, price_Order, sale):
      self.price_Order = price_Order
      self.sale = sale
