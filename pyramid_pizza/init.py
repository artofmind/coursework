from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from .models import User, Tovar, Order, Session, Base, engine
import transaction

def database_settings(config):
    from sqlalchemy import create_engine
    config.registry.settings['sqlalchemy.url'] = db_url = "sqlite:///example.db"
    engine = create_engine(db_url)
    Base.metadata.bind = engine
    Base.metadata.create_all()
    
def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    Session.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    
    return config.make_wsgi_app()

if __name__ == '__main__':
    config = Configurator()
    config.include(database_settings)
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
