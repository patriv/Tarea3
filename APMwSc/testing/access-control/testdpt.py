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
    
    #Caso Frontera
    def test1DptInsert(self):
        dpt1 = dpt()
        self.assertTrue(dpt1.insertDpt(iddpt = 1,namedpt = 'computacion'))
        
    #Caso Frontera    
    def test2DptInsertFalse(self):
         dpt1 = dpt()
         self.assertFalse(dpt1.insertDpt(iddpt = 1,namedpt = 'computacion'))
         
    #Caso Frontera externa
    def test3DptInsertNotiddt(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.insertDpt(iddpt = None, namedpt = 'mecanica'))
               
    #Caso Frontera externa
    def test4DptInsertIddt0(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.insertDpt(iddpt = 0,namedpt = 'materiales'))
        
    #Caso Fronetra 
    def test5DptInsertIddt(self):
        dpt1 = dpt()
        self.assertTrue(dpt1.insertDpt(iddpt = (2**31)-1,namedpt = 'materiales'))
        
    #Caso Frontera
    def tesdt6DptInsertNamedpt1char(self):
        dpt1 = dpt()
        self.assertTrue(dpt1.insertDpt(iddpt = 587,namedpt = 'm'))
        
    #Caso Malicia
    def test7DptInsertNotNamedpt(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.insertDpt(iddpt = 587,namedpt = ''))
        
    #Caso Frontera Externa
    def test8DptInsertNamedptChar51(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.insertDpt(iddpt = 300,namedpt = 'Departamento de Informacion y Tecnologia Computacio'))
        
    #Caso Frontera interna
    def test9DptInsertNamedptChar49(self):
        dpt1 = dpt()
        self.assertTrue(dpt1.insertDpt(iddpt = 301,namedpt = 'Departamento de Informacion y Tecnologia Computac'))

    #Caso Malicia
    def test_60DptInsertNegative(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.insertDpt(iddpt = -566,namedpt = 'mecanica'))
   
    #Caso escquina    
######################################################################

        #CASOS DE PRUEBA FUNCION SEARCHDPT
    '''    
    #Caso Frontera
    def test_61searchDpt(self):
        dpt1 = dpt()
        self.assertTrue(dpt1.searchDtp(iddpt = 301))
        
    #Caso Frontera
    def test_62seacrhDptiddpt1(self):
        dpt1 = dpt()
        self.assertTrue(dpt1.searchDpt(iddpt = 1))
        
    '''    
   
        

    
        
        

        
        
        
    
         