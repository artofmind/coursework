# -*- coding: utf-8 -*- 
from pyramid.view import view_config
from pyramid.response import Response
from models import *
import re
from datetime import *


from pyramid.security import (
remember,
forget,
)

from pyramid.httpexceptions import (
HTTPFound,
HTTPNotFound,
)


@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    return {'username': request.authenticated_userid}


@view_config(route_name='vacations', renderer='templates/vacations.jinja2')
def vacations(request):
    return {'username': request.authenticated_userid}


@view_config(route_name='contacts', renderer='templates/contacts.jinja2')
def contacts(request):
    return {'username': request.authenticated_userid}

@view_config(route_name='pizza', renderer='templates/pizza.jinja2')
def pizza(request):
    return {'username': request.authenticated_userid}


@view_config(route_name='snacks', renderer='templates/snacks.jinja2')
def snacks(request):
    return {'username': request.authenticated_userid}

@view_config(route_name='drinks', renderer='templates/drinks.jinja2')
def drinks(request):
    return {'username': request.authenticated_userid}


@view_config(route_name='delivery', renderer='templates/delivery.jinja2')
def delivery(request):
    return {'username': request.authenticated_userid}


@view_config(route_name='photo', renderer='templates/photo.jinja2')
def photo(request):
    return {'username': request.authenticated_userid}


@view_config(route_name='actions', renderer='templates/actions.jinja2')
def actions(request):
    return {'username': request.authenticated_userid}



@view_config(route_name='register', renderer='templates/register.jinja2')
def register(request):
	if request.method == 'POST':
		session = Session(bind=engine)
		errors = []
		if(len(request.params['name']) <=3):
			errors.append(u"Введите имя")
		if(len(request.params['login']) <6):
			errors.append(u"Введите логин")
		if(len(request.params['password']) <=5):
			errors.append(u"Введите пароль")
		if(len(request.params['passwordTwo']) <=5):
			errors.append(u"Введите подтверждение пароля")
		if(request.params['password']!= request.params['passwordTwo']):
			errors.append(u'Пароли не совпадают')
		if(session.query(User).filter_by(Login=request.params['login']).count() != 0):
			errors.append(u'Такой логин уже существует')
		if(len(errors) != 0):
			return { 'errors' : errors ,
					 'name' : request.params['name'],
					 'login' : request.params['login'],
					 'mail' : request.params['mail'],
					
		else:
			new_user = User(request.params['login'],
							request.params['password'],
							request.params['mail'],
							request.params['name'],
							
			session.add(new_user)
			session.commit()
			return HTTPFound(location = request.route_url('goodReg', goodReg='great', _query={'login' : request.params['login']}))
	else:
		return { 'username': request.authenticated_userid }

@view_config(route_name='logIn', renderer='templates/logIn.jinja2')
def logIn(request):
	if request.method == 'POST':
		user = Session(bind=engine).query(User).filter(User.Login == request.params['login']).first()
		if user != None and user.Password == request.params['password']:
			headers = remember(request, user.Login)			
			return HTTPFound(location = '/', headers = headers)
		else:
			return {'error': u"Введены неверные данные", 'username': request.authenticated_userid }
	else:
		return {'username' : request.authenticated_userid }


@view_config(route_name='goodReg', renderer='templates/goodReg.jinja2')
def goodReg(request):
    return {'username': request.authenticated_userid,
    		'login' : request.params['login'] }
