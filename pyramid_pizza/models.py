from sqlalchemy import Column, Index,Integer,Text, create_engine, ForeignKey, DateTime, Integer, Unicode, UnicodeText
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension
from pyramid_sqlalchemy import BaseObject
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from sqlalchemy.orm import backref, relationship

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

def sacrud_settings(config):
    config.include('pyramid_sacrud', route_prefix='admin')
    config.registry.settings['pyramid_sacrud.models'] = (
        ('zakaz', [Order, Tovar]),
        ('group', [User])
    )


def database_settings(config):
    from sqlalchemy import create_engine
    config.registry.settings['sqlalchemy.url'] = db_url =\
        "sqlite:///base.db"
    engine = create_engine(db_url)
    Base.metadata.bind = engine
    Base.metadata.create_all()


if __name__ == '__main__':
    from pyramid.session import SignedCookieSessionFactory
    my_session_factory = SignedCookieSessionFactory('123')
    config = Configurator(session_factory=my_session_factory)
    config.include(database_settings)
    config.include(sacrud_settings)
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
