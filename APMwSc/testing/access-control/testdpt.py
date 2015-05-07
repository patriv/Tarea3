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

    def test9DptInsertNamedptChar50(self):
        dpt1 = dpt()
        self.assertTrue(dpt1.insertDpt(iddpt = 301,namedpt = 'Departamento de Informacion y Tecnologia Computaci'))
  
    #Caso Frontera interna
    def test_10DptInsertNamedptChar49(self):
        dpt1 = dpt()
        self.assertTrue(dpt1.insertDpt(iddpt = 302,namedpt = 'Departamento de Informacion y Tecnologia Computac'))

    #Caso Malicia
    def test_11DptInsertNegative(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.insertDpt(iddpt = -566,namedpt = 'mecanica'))
   
    #Caso esquina
    
    def test_12DptInsertminchar(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.insertDpt(iddpt = 1,namedpt = 'x'))
     
    #caso malicia   
    def test_13DptInsertNoparam(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.insertDpt(iddpt = '' ,namedpt = ''))
    
    #caso esquina
    def test_14DptInsertmax(self):
        dpt1 = dpt()
        self.assertTrue(dpt1.insertDpt(iddpt = (2**31) ,namedpt = 'Departamento de Informacion & Tecnologia Computaci'))
    
    #caso malicia   
    def test_15DptInsertNoparamId(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.insertDpt(iddpt = None ,namedpt = ''))
    
    #caso malicia   
    def test_16DptInsertNoparam(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.insertDpt(iddpt = None ,namedpt = 30))
              
###########################################################################

    #CASOS DE PRUEBA FUNCION SEARCHDPT
        
    #Caso Frontera
    def test_17searchDpt(self):
        dpt1 = dpt()
        self.assertNotEqual([],dpt1.searchDpt(iddpt = 301))

    #Caso Frontera
    def test_18seacrhDptiddpt1(self):
        dpt1 = dpt()
        self.assertNotEqual([],dpt1.searchDpt(iddpt = 1))
        
    #Caso Frontera
    def test_19searchDptiddptbig(self):
        dpt1 = dpt()
        self.assertNotEqual([],dpt1.searchDpt(iddpt = (2**31)-1))     
    
    #Caso Malicia
    def test_20seacrhDptiddptNoInt(self):
        dpt1 = dpt()
        self.assertEqual([],dpt1.searchDpt(iddpt = ''))
    
    #Caso Malicia
    def test_21seacrhDptiddptNoParam(self):
        dpt1 = dpt()
        self.assertEqual([],dpt1.searchDpt(iddpt = None))        
    
    #Caso Malicia
    def test_22seacrhDptiddpt0(self):
        dpt1 = dpt()
        self.assertEqual([],dpt1.searchDpt(iddpt = 0))

    #Caso Malicia
    def test_23seacrhDptiddptnegative(self):
        dpt1 = dpt()
        self.assertEqual([],dpt1.searchDpt(iddpt = -8))       

#####################################################################
        
            #CASOS DE PRUEBA FUNCION DELETEDPT
    #Caso Frontera
    def test_24deleteDptTrue(self):
        dpt1 = dpt()
        self.assertTrue(dpt1.deleteDpt(iddpt = 1))  
        
        #Caso Frontera
    def test_25deleteDptFalse(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.deleteDpt(iddpt = 1))  
        
    #Caso Frontera
    def test_26deleteDptiddptbig(self):
        dpt1 = dpt()
        self.assertTrue(dpt1.deleteDpt(iddpt = (2**31)-1))     
    
    #Caso Malicia
    def test_27deleteDptiddptNoInt(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.deleteDpt(iddpt = ''))
    
    #Caso Malicia
    def test_28deleteDptiddptNoParam(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.deleteDpt(iddpt = None))        
    
    #Caso Malicia
    def test_29deleteDptiddpt0(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.deleteDpt(iddpt = 0))

    #Caso Malicia
    def test_30deleteDptiddptnegative(self):
        dpt1 = dpt()
        self.assertFalse(dpt1.deleteDpt(iddpt = -8))   
    
         