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
minIddpt = 0
maxNameDpt = 50

class dpt(object):

    def insertDpt(self,iddpt,namedpt):
        adpt = clsDpt.query.filter_by(iddpt=iddpt).all()
        if (adpt == []):
            new_dpt = clsDpt(iddpt = iddpt, namedpt = namedpt)
            #Definimos la longitud de namedpt
            if  type(namedpt) != str:
                return False
            else:
                long_namedpt=len(new_dpt.namedpt)
                if (type(iddpt) == str or new_dpt.iddpt == None or new_dpt.iddpt <= minIddpt \
                        or new_dpt.namedpt == '' or long_namedpt > maxNameDpt):
                    return False
                else:
                    db.session.add(new_dpt)
                    db.session.commit()
                    return True
        else:
            return False
    
    def searchDpt(self,iddpt): 
        if (iddpt == '') or (iddpt == None) or iddpt <=0 or type(iddpt) != int:
            return []
        else:
            dpt1 = clsDpt.query.filter_by(iddpt=iddpt).all()
            return dpt1
    
    def deleteDpt(self,iddpt):
        if (iddpt == '') or (iddpt == None) or iddpt <=0 or type(iddpt) != int:
            return False
        else:
            adpt = clsDpt.query.filter_by(iddpt=iddpt).all()
            if adpt == []:
                return False
            else:
                for i in adpt:    
                    db.session.delete(i)
                db.session.commit()
                return True