# -*- coding: utf-8 -*- 
from pyramid.config import Configurator
from pizza.resources import get_root
from pyramid.session import SignedCookieSessionFactory
from sqlalchemy import inspect
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, Deny
from pyramid.security import Authenticated
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

from models import *

class MyFactory(object):
    def __init__(self, request):
        self.__acl__ = [(Allow, Authenticated, "add")]

my_session_factory = SignedCookieSessionFactory('pizza')

def main(global_config, **settings):
    Base.metadata.create_all()

    settings = dict(settings)
    settings.setdefault('jinja2.i18n.domain', 'pizza')

    config = Configurator(root_factory=MyFactory, settings=settings, session_factory=my_session_factory)
    config.include('pyramid_jinja2')

    config.add_static_view('static', 'static')
    config.add_route("index" , '/')
    config.add_route("vacations" , "/vacations")
    config.add_route("pizza", "/pizza")
    config.add_route("snacks", "/snacks")
    config.add_route("drinks", "/drinks")
    config.add_route("delivery", "/delivery")
    config.add_route("photo", "/photo")
    config.add_route("actions", "/actions")
    config.add_route("contacts" , "/contacts")
    config.add_route("goodReg", "/goodReg")
    config.add_route("register", "/register")
    config.add_route("logIn", '/logIn')
    config.add_route("admin", "/admin")



    authn_policy = AuthTktAuthenticationPolicy('secret', hashalg='1')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    #админ
    sessio = Session(bind = engine)
    new_admin = Admins(Login = 'admin',
    					Password = '123',
    					Mail = 'admin@mail.ru',
    					FirstName = 'Admin',
    					SecondName = 'Admin')
    sessio.add(new_admin)
    sessio.commit()

    config.scan()
    return config.make_wsgi_app()
