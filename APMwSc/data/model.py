import os
from flask.ext.migrate import Migrate, MigrateCommand
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager

import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

#Conexion con la base de datos
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'apl.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
	'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

#Descripcion de la Base de Datos

#Declaracion del modelo Departamento
class clsDpt(db.Model):
     __tablename__ = 'dpt'
     iddpt = db.Column(db.Integer, primary_key=True)
     namedpt = db.Column(db.String(50), unique=True)
     user_dpt = db.relationship('clsUser',backref='dpt',lazy = 'dynamic')

     def __init__(self, iddpt, namedpt):
     	self.iddpt = iddpt
     	self.namedpt = namedpt

     def __repr__(self):
        return '<Dpt %r>' % self.namedpt

#Declaracion del modelo Role
class clsRole(db.Model):
   __tablename__ = 'roles'
   idrole = db.Column(db.Integer, primary_key=True)
   namerole = db.Column(db.String(50), unique=True)
   user_role = db.relationship('clsUser',backref='role',lazy = 'dynamic')
   
   def __init__(self, idrole, namerole):
   		self.idrole = idrole
   		self.namerole = namerole
   
   def __repr__(self):
      return '<Role %r>' % self.namerole

#Declaracion del modelo Usuario
class clsUser(db.Model): 
    __tablename__ = 'user'
    fullname = db.Column(db.String(50))
    username = db.Column(db.String(16), primary_key = True, index = True)
    password = db.Column(db.String(16))
    email = db.Column(db.String(30), unique = True )
    id_dpt = db.Column(db.Integer, db.ForeignKey('dpt.iddpt'))
    id_role = db.Column(db.Integer, db.ForeignKey('roles.idrole'))

    def __init__(self, fullname, username, password, email, iddpt, idrole):
    	self.fullname = fullname
    	self.username = username
    	self.password = password
    	self.email = email
    	self.iddpt = iddpt
    	self.idrole = idrole
   
    def __repr__(self):
    	return '<User %r>' % self.username

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	db.drop_all() #Borramos la base de datos
	db.create_all() #Creamos la base de datos