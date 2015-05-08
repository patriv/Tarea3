'''
Created on 30/4/2015

@author: Patricia Valencia
         Sahid Reyes
'''
import sys
sys.path.append('../../data')
sys.path.append('../../business/access-control')
import unittest

from user import *

class ClsUserTester(unittest.TestCase):
    
    #CASOS DE PRUEBA FUNCION INSERTUSER

    #caso frontera
    def test1UserInsertTrue(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sah', username = 'ehfah',password = 'al', email = '@ls', iddpt = 1, idrole = 1))
    
    #caso frontera
    def test2UserInsertFalse(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sah', username = 'ehfah',password = 'al', email = '@ls', iddpt = 1, idrole = 1))
     
    #caso frontera externa
    def test3UserInsertNoUser(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sah', username = '',password = 'al', email = '@?lds', iddpt = 1, idrole = 1))
     
    #caso frontera interna 
    def test4UserInsert1char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid', username = 'a',password = '12234', email = 'xxx@gmail.com', iddpt = 800, idrole = 45))
         
    #caso frontera Externa 
    def test5UserInsert17char(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sahid', username = 'jksjdfdj vkjdfuhf',password = '12234', email = 'xxx@gmail.com', iddpt = 800, idrole = 45))
     
    #caso frontera Externa 
    def test6_0UserInsert16char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid', username = 'jksjdfdjvkjdfuhf',password = '12234', email = 'yzyyxxx@gmail.com', iddpt = 800, idrole = 45))
     
    #caso frontera Externa 
    def test6_1UserInsert15char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid', username = 'wjfr9olpsmfkreo',password = '12234', email = 'xfeexx@fgmail.com', iddpt = 800, idrole = 45)) 
         
    #caso frontera
    def test6_2UserInsert8char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid', username = 'wiekfprm',password = '12234', email = 'yffe@ldv.gmail.com', iddpt = 800, idrole = 45))
         
    #caso frontera Externa 
    def test6UserInserFullnamet51char(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sahid Patricia Reyes Valencia kjhdj kjhvjfdbhjdcmkd', username = 'jksjdfdj vkjdfuhf',password = '12234', email = 'xxx@gmail.com', iddpt = 800, idrole = 45))
     
    #caso frontera
    def test7UserInserFullnamet50char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid Patricia Reyes Valencia kjhdj kjhvjfdbhjdcmk', username = 'jksjdfdj__',password = '12234', email = 'xx__x@gmail.com', iddpt = 800, idrole = 45))   
     
    #caso frontera Interna 
    def test8UserInserFullnamet49char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid Patricia Reyes Valencia jhdj kjhvjfdbhjdcmkd', username = 'jpvkjdfuhf',password = '12234', email = 'xyyy@gmail.com', iddpt = 800, idrole = 45))
     
    #caso frontera Externa 
    def test9UserInserFullnamet25char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'Patricia Reyes Valencia25', username = 'patkjdfuhf',password = '12234', email = 'patx@gmail.com', iddpt = 800, idrole = 45))
     
    #caso frontera Externa 
    def test9_0UserInserNoFullname(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = '', username = 'patkjdfuhf',password = '12234', email = 'patx@gmail.com', iddpt = 800, idrole = 45))
     
       #caso frontera Externa 
    def test9_1UserInserFullnamet1char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'P', username = 'patkfhf_1',password = '12234', email = 'paddtx@gmail.com', iddpt = 800, idrole = 45))
     
    #caso frontera Externa
    def test_10UserInsertEmail31char(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sahid Patricia', username = 'tdd ',password = '12d234', email = '10-10603-10-10916ing@ldc.usb.ve', iddpt = 800, idrole = 45))
 
    #caso frontera Externa
    def test_11UserInsertNoEmail(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sahid Patricia', username = 'tdd ',password = '12d234', email = '', iddpt = 800, idrole = 45))
      
    #caso frontera Interna
    def test_12UserInsertEmail1char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid Patricia', username = 'tdd_1 ',password = '12d234', email = '@', iddpt = 800, idrole = 45))
      
     #caso frontera Interna
    def test_13UserInsertEmail30char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid Patricia', username = 'tdd_2',password = '12d234', email = '1234567890patricia_v@gmail.com', iddpt = 800, idrole = 45))
      
     #caso frontera Interna
    def test_14UserInsertEmail29char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid Patricia', username = 'tdd_3',password = '12d234', email = '1234567890patriciav@gmail.com', iddpt = 800, idrole = 45))
     
    #caso frontera externa
    def test_15UserInsertPassword17(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'pat', username = 'ehfah_1',password = '123456789qwertyui', email = '2@ls', iddpt = 1, idrole = 1))
     
    #caso frontera externa
    def test_16UserInsertNoPassword(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sah', username = 'ehfah_2',password = '', email = '3@ls', iddpt = 1, idrole = 1))
     
    #caso frontera interna
    def test_17UserInsertPassword15(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sah', username = 'ehf_1',password = 'eifko09olpedft5', email = 'po@rls', iddpt = 1, idrole = 1))
     
    #caso frontera interna
    def test_18UserInsertPassword1(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sr', username = 'er3r_1',password = '1', email = 'desm@ld.s', iddpt = 1, idrole = 1))
     
    #caso frontera
    def test_19UserInsertPasword16(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sah', username = 'frkfe_1',password = 'qiejdp0t4jmds21l', email = 'fefef_t@l.ss', iddpt = 1, idrole = 1))
     
    #caso frontera
    def test_20UserInsertPassword8(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sah', username = 'lowdn',password = 'kdiopw34', email = 'efmefm@l.c', iddpt = 1, idrole = 1))
     
    #Caso Malicia5
    def test_21UserInsertiddptChar(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sahid', username = 'a',password = '12234', email = 'xxx@gmail.com', iddpt = 'a', idrole = 'b'))
                
    #caso malicia
    def test_22UserInsertNochar(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = '', username = '',password = '', email = '', iddpt = None, idrole = None))
     
    #caso malicia   
    def test_22_1UserInsertNoParam(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = None, username = None,password = None, email = None, iddpt = None, idrole = None))
# 
    ##################################################################################
     
    #CASOS DE PRUEBA SEARCHUSER
     
    #Caso Frontera
    def test_23searchUserTrue(self):
        user1 = user()
        self.assertNotEqual([],user1.searchUser(username = 'ehfah'))
         
    #Caso Frontera 
    def test_24searchUser1Char(self):
        user1 = user()
        self.assertNotEqual([],user1.searchUser(username = 'a'))
     
    #Caso Frontera
    def test_25searchUser16Char(self):
        user1 = user()
        self.assertNotEqual([],user1.searchUser(username = 'jksjdfdjvkjdfuhf'))
     
    #Caso Frontera externa
    def test_26SearchUserNotChar(self): 
        user1 = user()
        self.assertEqual([],user1.searchUser(username = ''))
     
    #Caso Frontera externa
    def test_27searchUser17Char(self):
       user1 = user()
       self.assertEqual([],user1.searchUser(username = 'jksjdfdj vkjdfuhf'))
        
    #Caso Esquina
    def test_28searchUserNotInsert(self):
        user1 = user()
        self.assertEqual([],user1.searchUser(username = 'PatriciaValencia'))
         
    #Caso INtermedio
    def test_29searchUser8Char(self):
        user1 = user()
        self.assertNotEqual([],user1.searchUser(username = 'wiekfprm'))
     
     
    ###############################################################################################    
 
    #CASOS DE PRUEBA FUNCION DELETEUSER
     
    #Caso Frontera
    def test_30UserDeleteTrue(self):
        user1 = user()
        self.assertTrue(user1.deleteUser(username = 'wiekfprm'))
     
    #caso Frontera     
    def test_31UserDeleteFalse(self):
        user1 = user()
        self.assertFalse(user1.deleteUser(username = 'wiekfprm'))
     
    #caso malicia    
    def test_32UserDeleteNoUser(self):
        user1 = user()
        self.assertFalse(user1.deleteUser(username = ''))
     
    #caso frontera Interna 
    def test_33UserDelete1char(self):
        user1 = user()
        self.assertTrue(user1.deleteUser(username = 'a'))
     
    #caso frontera     
    def test_34UserDelete16char(self):
        user1 = user()
        self.assertTrue(user1.deleteUser(username = 'jksjdfdjvkjdfuhf'))
             
    #Caso frontera Externa        
    def test_35UserDelete17char(self):
        user1 = user()
        self.assertFalse(user1.deleteUser(username = 'jksjdfdj vkjdfuhf'))
             
    #caso frontera Interna 
    def test_36UserDelete15char(self):
        user1 = user()
        self.assertTrue(user1.deleteUser(username = 'wjfr9olpsmfkreo')) 
     
        