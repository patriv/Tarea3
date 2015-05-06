'''
Created on 30/4/2015

@author: Patricia Valencia
         Sahid Reyes
'''
import os
import sys
sys.path.append('../../data')
from model import *

class user(object):

    def searchUser(self,username):
        auser = clsUser.query.filter_by(username=username)
        return auser

    def insertUser(self, fullname, username, password, email, iddpt, idrole):
        auser = clsUser.query.filter_by(username=username).all()
        if auser == []:
            new_user = clsUser(fullname = fullname, username = username, password = password, email =email, iddpt = iddpt, idrole = idrole)
            if (new_user.username == '' or new_user.fullname == '' or new_user.password == '' or new_user.email == '' or new_user.iddpt == None or new_user.idrole == None):
                return False
            else:
                
                db.session.add(new_user)
                db.session.commit()
                return True
        else:
            return False

    

    
    def deleteUser(self,username):
        auser = searchUser(username)
        if auser is None:
            return False
        else:
            db.session.delete(auser)
            return True