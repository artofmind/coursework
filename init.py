from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from .models import User, Tovar, Order, Session, Base, engine
import transaction

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    Session.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    
    return config.make_wsgi_app()
