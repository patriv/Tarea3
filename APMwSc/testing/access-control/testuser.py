'''
Created on 05/05/2015

@author: Sahid Reyes
         Patricia Valencia
'''
import sys
sys.path.append('../../data')
sys.path.append('../../business/access-control')
import unittest

from user import *

class ClsUserInsertTester(unittest.TestCase):
       
     #caso frontera
     def test1UserInsertTrue(self):
         user1 = user()
         self.assertTrue(user1.insertUser(fullname = 'sah', username = 'ehfah',password = 'al', email = '@ls', iddpt = 1, idrole = 1))
     
     #caso frontera
     def test2UserInsertFalse(self):
         user1 = user()
         self.assertFalse(user1.insertUser(fullname = 'sah', username = 'ehfah',password = 'al', email = '@ls', iddpt = 1, idrole = 1))
     
     #caso frontera externa PREGUNTAR
     def test3UserInsertNoUser(self):
         user1 = user()
         self.assertFalse(user1.insertUser(fullname = 'sah', username = '',password = 'al', email = '@?lds', iddpt = 1, idrole = 1))
         
     #caso frontera Externa 
     def test6_0UserInsert16char(self):
       user1 = user()
       self.assertTrue(user1.insertUser(fullname = 'sahid', username = 'jksjdfdjvkjdfuhf',password = '12234', email = 'yzyyxxx@gmail.com', iddpt = 800, idrole = 45))
     
     #caso frontera interna 
     def test4UserInsert1char(self):
         user1 = user()
         self.assertTrue(user1.insertUser(fullname = 'sahid', username = 'a',password = '12234', email = 'xxx@gmail.com', iddpt = 800, idrole = 45))
    
     def test6_2UserInsert8char(self):
         user1 = user()
         self.assertTrue(user1.insertUser(fullname = 'sahid', username = 'wiekfprm',password = '12234', email = 'yffe@ldv.gmail.com', iddpt = 800, idrole = 45))
         
     #caso frontera Externa 
     def test5UserInsert17char(self):
         user1 = user()
         self.assertFalse(user1.insertUser(fullname = 'sahid', username = 'jksjdfdj vkjdfuhf',password = '12234', email = 'xxx@gmail.com', iddpt = 800, idrole = 45))
         
     #caso frontera Externa 
     def test6UserInserFullnamet51char(self):
         user1 = user()
         self.assertFalse(user1.insertUser(fullname = 'sahid Patricia Reyes Valencia kjhdj kjhvjfdbhjdcmkd', username = 'jksjdfdj vkjdfuhf',password = '12234', email = 'xxx@gmail.com', iddpt = 800, idrole = 45))
     
      #FALTA PROBAR CON CADA PARAMETRO SU LONGITUD.
      
     #Caso Malicia
     def test99998UserInsertiddptChar(self):
         user1 = user()
         self.assertFalse(user1.insertUser(fullname = 'sahid', username = 'a',password = '12234', email = 'xxx@gmail.com', iddpt = 'a', idrole = 'b'))
 
                
     #caso malicia
     def test99999UserNoParam(self):
         user1 = user()
         self.assertFalse(user1.insertUser(fullname = '', username = '',password = '', email = '', iddpt = None, idrole = None))
     
    
    
    ##################################################################################
    #Casos de Prueba funcion searchUser
   
     #Caso Frontera
     def test_333searchUserTrue(self):
         user1 = user()
         self.assertNotEqual([],user1.searchUser(username = 'ehfah'))
         
     #Caso Frontera 
     def test_334searchUser1Char(self):
         user1 = user()
         self.assertTrue(user1.searchUser(username = 'a'))
    
     #Caso Frontera
     def test_335searchUser16Char(self):
         user1 = user()
         self.assertNotEqual([],user1.searchUser(username = ' jksjdfdjvkjdfuhf'))

    #Caso Frontera externa
     def test_336SearchUserNotChar(self): 
         user1 = user()
         self.assertFalse(user1.searchUser(username = ''))

    #Caso Frontera externa
     def test_337searchUser17Char(self):
        user1 = user()
        self.assertFalse(user1.searchUser(username = 'jksjdfdj vkjdfuhf'))
        
    #Caso Esquina
     def test_336searchUserNotInsert(self):
         user1 = user()
         self.assertEqual([],user1.searchUser(username = 'PatriciaValencia'))
         
     #Caso INtermedio
     def test_337searchUser8Char(self):
         user1 = user()
         self.assertNotEqual([],user1.searchUser(username = 'wiekfprm'))

        
    ###################################################################

         
        
    