from sqlalchemy import create_engine,Table,Column,MetaData,Integer,String,ForeignKey,Date,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, backref, relationship
import os

if os.path.exists("basa.db"):
    os.remove("basa.db")

engine = create_engine('sqlite:///basa.db', encoding='utf-8')
Session = sessionmaker()
Base = declarative_base(bind=engine)

class User(Base):
     __tablename__ = "Users"
     Login = Column(String, nullable = False,primary_key = True)
     Password = Column(String, nullable = False)
     Mail = Column(String, nullable = False)
     FirstName = Column(String, nullable = False)
     SecondName = Column(String, nullable = False)
     def __init__(self, Login, Password, Mail, FirstName, SecondName):
          self.Login = Login
          self.Password = Password
          self.Mail = Mail
          self.FirstName = FirstName
          self.SecondName = SecondName

     def __repr__(self):
          return self.Login + " " + self.Password + " " + self.Mail + " " +self.FirstName

class Admins(Base):
     __tablename__ = "Admins"
     Login = Column(String, nullable = False,primary_key = True)
     Password = Column(String, nullable = False)
     Mail = Column(String, nullable = False)
     FirstName = Column(String, nullable = False)
     SecondName = Column(String, nullable = False)

     def __init__(self, Login, Password, Mail, FirstName, SecondName):
          self.Login = Login
          self.Password = Password
          self.Mail = Mail
          self.FirstName = FirstName
          self.SecondName = SecondName

     def __repr__(self):
          return self.Login + " " + self.Password + " " + self.Mail + " " +self.FirstName + " " + self.SecondName


class Tovar(Base):
    __tablename__ = 'tovar'
    id_Tovar = Column(Integer, primary_key=True, nullable = False)
    name_Tovar = Column(String, unique=True, nullable=False)
    price_Tovar = Column(Integer, nullable = False)

    def __init__(self, id_Tovar, name_Tovar, price_Tovar):
         self.id_Tovar = id_Tovar
         self.name_Tovar = name_Tovar
         self.price_Tovar = price_Tovar

    def __repr__(self):
         return self.id_Tovar + " " + self.name_Tovar + " " + self.price_Tovar
