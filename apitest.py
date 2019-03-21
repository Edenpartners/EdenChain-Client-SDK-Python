import os
import uuid

import inspect

import unittest

from pathlib import Path
import os.path


from eden_client_api.api import EdenClientApi

import time

import requests
import json
import asyncio





class TestSDKApi(unittest.TestCase):

    """ Eden Client API Test Class """

### Setup
    def setUp(self):
        self.startTime = time.time()
        self.api =  EdenClientApi(EdenClientApi.EDEN_PROTOTYPE_NETWORK)
        self.token = self.api.authenticate_user(os.environ['AUTH_USER'], os.environ['AUTH_PASSWORD'])        

    def tearDown(self):
        t = time.time() - self.startTime
        print( "%s: %.3f" % (self.id(), t))

####   Sync API Test 
    def test_token_valid(self):
        """ User's token is valid or not check"""
        # Create test, delete it first.        
        self.assertEqual(self.api.is_token_valid(self.token),True)

    def test_get_balance(self):
        """ Get Current Balance """
        balance = self.api.get_user_balance(token=self.token)
        print("balance:"+str(balance))
        self.assertIsNotNone(balance)

    
    def test_get_user_info(self):
        """ Get Current user information """
        user_info = self.api.get_user_info(token=self.token)
        print("User information:"+str(user_info))
        self.assertIsNotNone(user_info)

    def test_get_user_transaction(self):
        """ Get user transaction """
        transaction = self.api.get_user_transaction(token=self.token,page=1,countperpage=10)
        print("User transaction:"+str(transaction))
        self.assertIsNotNone(transaction)

    def test_get_coin_server_address(self):
        """ Get Coin Server Address """
        address = self.api.get_coin_server_address(token=self.token)
        print("Coin Server Address:"+str(address))
        self.assertIsNotNone(address)

    def test_add_eth_addres(self):
        self.assertEqual(self.api.add_eth_address(self.token,'0x7ab5e1487bb8ff6353778edca5745c0421df9df825862fca01a36b582f3b8a88'),True)

    def test_del_eth_addres(self):
        self.assertEqual(self.api.del_eth_address(self.token,'0x7ab5e1487bb8ff6353778edca5745c0421df9df825862fca01a36b582f3b8a88'),True)


#### Async API test.
    def test_token_valid_async(self):
        loop = asyncio.get_event_loop()
        ret = loop.run_until_complete(self.api.is_token_valid_async(self.token))
        self.assertEqual(ret,True)


    def test_get_balance_async(self):
        """ Get Current Balance """
        loop = asyncio.get_event_loop()
        balance = loop.run_until_complete( self.api.get_balance_async(token=self.token))
        print("balance:"+str(balance))
        self.assertIsNotNone(balance)

    def test_get_user_info_async(self):
        """ Get User information """
        loop = asyncio.get_event_loop()
        user_info = loop.run_until_complete( self.api.get_user_info_async(token=self.token))
        print("User Information:"+str(user_info))
        self.assertIsNotNone(user_info)    

    def test_get_user_transaction_async(self):
        """ Get User Transaction """
        loop = asyncio.get_event_loop()
        transaction = loop.run_until_complete( self.api.get_user_transaction_async(self.token,1,10))
        print("User Transaction:"+str(transaction))
        self.assertIsNotNone(transaction) 

    def test_get_coin_server_address_async(self):
        """ Get Coin Server address """
        loop = asyncio.get_event_loop()
        address = loop.run_until_complete( self.api.get_coin_server_address_async(token=self.token))
        print("Coin Server Address:"+str(address))
        self.assertIsNotNone(address)
    
    def test_add_eth_addres_async(self):
        loop = asyncio.get_event_loop()
        ret = loop.run_until_complete(self.api.add_eth_address_async(self.token,'0x7ab5e1487bb8ff6353778edca5745c0421df9df825862fca01a36b582f3b8a88'))
        self.assertEqual(ret,True)

    def test_del_eth_addres_async(self):
        loop = asyncio.get_event_loop()
        ret = loop.run_until_complete(self.api.del_eth_address_async(self.token,'0x7ab5e1487bb8ff6353778edca5745c0421df9df825862fca01a36b582f3b8a88'))
        self.assertEqual(ret,True)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSDKApi)
    unittest.TextTestRunner(verbosity=0).run(suite)

