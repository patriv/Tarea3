'''
Created on 30/4/2015

@author: Patricia Valencia
         Sahid Reyes
'''
import os
import sys
sys.path.append('../../data')
from model import *

class dpt(object):

    def insertDpt(self,iddpt,namedpt):
        new_dpt = clsDpt(iddpt = iddpt, namedpt = namedpt)
        db.session.add(new_dpt)
        db.session.commit()
        return True
    
    def searchDtp(self,iddpt):
        user = clsUser.query.filter_by(iddpt=iddpt)
        return user
    
    def deleteDpt(self,iddpt):
        user = searchUser(iddpt)
        if user is None:
            return False
        else:
            db.session.deleteUser(dpt)
            return True