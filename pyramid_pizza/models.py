from sqlalchemy import Column, Index,Integer,Text, create_engine, ForeignKey, DateTime, Integer, Unicode, UnicodeText
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension
from pyramid_sqlalchemy import BaseObject

engine = create_engine('sqlite:///base.db')
Session = sessionmaker(bind=engine,extension=ZopeTransactionExtension()))
Base = declarative_base()

association_table = Table('association', Base.metadata,
 Column('id_Order', Integer, ForeignKey('Order.id_order')),
 Column('id_Tovar', Integer, ForeignKey('OTovar.id_Tovar')
)


class User(BaseObject):
    __tablename__ = 'user'
    id_User = Column(Integer, primary_key=True)
    name_User = Column(Unicode(255), nullable=False)
    lastname_User = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), unique=True, nullable=False)

class Tovar(BaseObject):
    __tablename__ = 'tovar'
    id_Tovar = Column(Integer, primary_key=True)
    name_Tovar = Column(Unicode(255), unique=True, nullable=False)
    price_Tovar = Column(Integer)

class Order(BaseObject):
    __tablename__ = 'order'
    id_Order = Column(Integer, primary_key=True)
    Tovars = relationship("Tovar",
                          secondary=association_table)
    id_User = Column(Unicode(255), ForeignKey('User.id_User'))
    price_Order = Column(Integer)
    sale = Column(Integer)
