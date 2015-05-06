'''
Created on 30/4/2015

@author: sahid
'''
import sys
sys.path.append('../../data')
sys.path.append('../../business/access-control')
import unittest

from user import *

class ClsUserTester(unittest.TestCase):
    
   #def testSearchUser(self):
    
    #caso frontera
    def test1UserInsertTrue(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sah', username = 'ssgfwguewhdioweflwefweflwhlwehflehfah',password = 'al', email = '@ls', iddpt = 1, idrole = 1))
    '''
    #caso frontera
    def test2UserInsertFalse(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sah', username = 'sgfwguewhdioweflwefweflwhlwehflehfah',password = 'al', email = '@ls', iddpt = 1, idrole = 1))
    
    #caso frontera externa
    def test3UserInsertNoUser(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = 'sah', username = '',password = 'al', email = '@?lds', iddpt = 1, idrole = 1))
    
    #caso frontera interna 
    def test4UserInsert1char(self):
        user1 = user()
        self.assertTrue(user1.insertUser(fullname = 'sahid', username = 'a',password = '12234', email = 'xxx@gmail.com', iddpt = 800, idrole = 45))
    
            
    #caso malicia
    def test99999UserNoParam(self):
        user1 = user()
        self.assertFalse(user1.insertUser(fullname = '', username = '',password = '', email = '', iddpt = None, idrole = None))
    
    '''