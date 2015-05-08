'''
Created on 07/05/2015

@author: Patricia Valencia
         Sahid Reyes
'''

import os
import sys
sys.path.append('../../data')
from model import *

#Declaracion de constantes
minIdrole = 0
maxNameRole = 50
roles = ['Product Owner', 'Scrum Master', 'Team member']

#Implementacion de la clase role
class role(object):
    
    #Metodo que inserta un role
    def insertRole(self,idrole,namerole):
        arole = clsRole.query.filter_by(idrole=idrole).all()
        if (arole == []):
            new_role = clsRole(idrole = idrole, namerole = namerole)
            #Definimos la longitud de 
            if  type(namerole) != str:
                return False
            else:
                long_namerole=len(new_role.namerole)
                if (type(idrole) == str or new_role.idrole == None or new_role.idrole <= minIdrole \
                        or new_role.namerole == '' or long_namerole > maxNameRole or new_role.namerole not in roles):
                    return False
                else:
                    db.session.add(new_role)
                    db.session.commit()
                    return True
        else:
            return False
    
    #Metodo que busca un role, dado su id    
    def searchRole(self,idrole): 
        if (idrole == '') or (idrole == None) or idrole <=0 or type(idrole) != int:
            return []
        else:
            role1 = clsRole.query.filter_by(idrole=idrole).all()
            return role1
        
    #Metodo que elimina un role, dado su id    
    def deleteRole(self,idrole):
        if (idrole == '') or (idrole == None) or idrole <=0 or type(idrole) != int:
            return False
        else:
            arole = clsRole.query.filter_by(idrole=idrole).all()
            if arole == []:
                return False
            else:
                for i in arole:    
                    db.session.delete(i)
                db.session.commit()
                return True