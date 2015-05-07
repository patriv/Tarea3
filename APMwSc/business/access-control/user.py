'''
Created on 30/4/2015

@author: Patricia Valencia
         Sahid Reyes
'''
import os
import sys
sys.path.append('../../data')
from model import *

#Declaracion de constantes

const_maxUser = 16
const_maxFullname = 50
const_maxPassword = 16
const_maxEmail = 30
 
class user(object):

    def searchUser(self,username):
        long_username = len(username)
        if (username == '') or long_username > 16:
            return False
        else:
            auser = clsUser.query.filter_by(username=username).all()
            return auser

    def insertUser(self, fullname, username, password, email, iddpt, idrole):
        auser = clsUser.query.filter_by(username=username).all()
        if auser == []:
            new_user = clsUser(fullname = fullname, username = username, password = password, email =email, iddpt = iddpt, idrole = idrole)
            longUser = len(new_user.username)
            longFullname = len(new_user.fullname)
            longPassword = len(new_user.password)
            longEmail = len(new_user.email)
            if (new_user.username == '' or new_user.fullname == '' or new_user.password == '' or new_user.email == '' or new_user.iddpt == None \
                or new_user.idrole == None or longUser>const_maxUser or longFullname>const_maxFullname or longPassword>const_maxPassword or longEmail>const_maxEmail):
                return False
            else:
                
                db.session.add(new_user)
                db.session.commit()
                return True
        else:
            return False

      
    def deleteUser(self,username):
        auser = self.searchUser(username)
        if auser == []:
            return False
        else:
            db.session.delete(auser)
            db.session.commit()
            return True