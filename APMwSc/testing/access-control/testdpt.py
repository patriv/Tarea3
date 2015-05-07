'''
Created on 30/4/2015

@author: Patricia Valencia
         Sahid Reyes
'''
import sys
sys.path.append('../../data')
sys.path.append('../../business/access-control')
import unittest

from dpt import *

class ClsDptTester(unittest.TestCase):
    
    #CASOS DE PRUEBA FUNCION INSERTDPT

    def test1Dptinsert(self):
        dpt1 = dpt()
        self.assertTrue(dpt1.insertDpt(iddpt = '1',namedpt = 'computacion'))
        print (clsDpt.query.all())
        