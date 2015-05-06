'''
Created on 30/4/2015

@author: sahid
'''
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from model import *

class User(object):
    
    def __init__(self):
        return

    def insertUser(self,fullname, username, password, email, iddpt, idrole):
        new_user = clsUser(fullname = fullname, usernamer = username, email =email, iddpt = iddpt, idrole = idrole)
        db.session.add(new_user)
        db.commit()
        return True
    
    def searchUser(self,fullname):
        user = clsUser.query.filter_by(fullname=fullname)
        return user
    '''
    def modifyUser(self,fullname):
        user = searchUser(fullname):
            if user is None:
                return False
            else
                db.session.deleteUser(user)
                user.fullname = input("fullname: ")
                user.username = input("username: ")
                user.email = input("email: ")
                user.iddpt = input("dpt: ")
                user.idrole = input("idrole: ")
                insertUser()
                
        return True
    '''
    def deleteUser(self,fullname):
        user = searchUser(fullname)
        if user is None:
            return False
        else:
            db.session.deleteUser(user)
            return True