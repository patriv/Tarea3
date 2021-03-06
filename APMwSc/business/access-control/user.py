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
const_min_long = 1

class user(object):
    
    def searchUser(self,username):
        if (type(username) != str):
            return []
        else:
            long_username = len(username)
            if (long_username >const_maxUser or long_username < const_min_long):
                return []
            else:
                auser = clsUser.query.filter_by(username=username).all()
                return auser


    def insertUser(self, fullname, username, password, email, iddpt, idrole):
        if (type(fullname) != str or type(username) != str or type(password) != str or type(email) != str or\
             type(iddpt) != int or type(idrole) != int):
            return False
        else:
            auser = clsUser.query.filter_by(username=username).all()
            if auser == []:
                new_user = clsUser(fullname = fullname, username = username, password = password, email =email, iddpt = iddpt, idrole = idrole)
                longUser = len(new_user.username)
                longFullname = len(new_user.fullname)
                longPassword = len(new_user.password)
                longEmail = len(new_user.email)
                if  (longUser >const_maxUser or longFullname > const_maxFullname or longPassword > const_maxPassword \
                     or longEmail>const_maxEmail or longEmail<const_min_long or longPassword<const_min_long or longUser<const_min_long\
                     or longFullname< const_min_long):
                    return False
                else:
                    dpt1 = clsDpt.query.filter_by(iddpt = iddpt).all()
                    role1 = clsRole.query.filter_by(idrole = idrole).all()
                    if (dpt1 == [] or role1 == []):
                        return False
                    else:
                        db.session.add(new_user)
                        db.session.commit()
                        return True
            else:
                return False
        
    def updateUser(self, new_fullname, username, new_password, new_email, new_iddpt, new_idrole):       
        if type(username) != str:
            return False
        else:
            auser = clsUser.query.filter_by(username=username).all()
            if auser == []:
                return False
            else:
                auser = clsUser.query.filter_by(username=username).first()
                if ((type(new_fullname) != str or type(new_password) != str or type(new_email) != str\
                     or type(new_iddpt) != int or type(new_idrole) != int)):
                    return False
                else:
                    longFullname = len(new_fullname)
                    longPassword = len(new_password)
                    longEmail = len(new_email)
                    if (longFullname>const_maxFullname or longPassword>const_maxPassword or longEmail>const_maxEmail\
                      or longFullname<const_min_long or longPassword<const_min_long or longEmail<const_min_long):
                        return False
                    else:
                        dpt1 = clsDpt.query.filter_by(iddpt = new_iddpt).all()
                        role1 = clsRole.query.filter_by(idrole = new_idrole).all()
                        if (dpt1 == [] or role1 == []):
                            return False
                        else:
                            auser.fullname = new_fullname
                            auser.password = new_password
                            auser.email = new_email
                            auser.iddpt = new_iddpt
                            auser.idrole= new_idrole
                            db.session.commit()
                            return True
                        
    def deleteUser(self,username):
        if type(username) != str:
            return False
        else:
            long_username = len(username)
            if long_username > const_maxUser or long_username < const_min_long:
                return False
            else:
                auser = clsUser.query.filter_by(username=username).all()
                if auser == []:
                    return False
                else:
                    for i in auser:    
                        db.session.delete(i)
                    db.session.commit()
                    return True