'''
Created on 30/4/2015

@author: sahid
'''

import unittest
from user import *

class ClsUserTester(unittest.TestCase):
    
    def testUserInsert(self):
        nombre_usuario = "Patricia"
        auser = user()
        self.assertTrue(auser.insertUser(nombre_usuario))        