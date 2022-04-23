import unittest #importing the unittest module
from user import User #import the class from user file.


class TestUser(unittest.TestCase):
    '''
    TestUser is a subclass of the parent class.
    unittest.TestCase helps in creating tests cases
    '''

    def setUp(self):#Setup Method is for defining instructions that will be executed before each test method.
        self.new_account = User("Sharonne", "Vanessa", "sharonnekay23@gmail.com", "shazzykay")

    def tearDown(self):#This code is executed before each test case.
                       #and its work is to clean up after each test case has run.
        User.user_createaccount = []

    def test_init(self):
        self.assertEqual(self.new_account.first_name, "Sharonne")
        self.assertEqual(self.new_account.last_name, "Vanessa")
        self.assertEqual(self.new_account.email, "sharonnekay23@gmail.com")
        self.assertEqual(self.new_account.password, "shazzykay")

    def test_save_account(self):
        self.new_account.save_account()
        self.assertEqual(len(User.user_createaccount), 1)


    def test_log_in(self):
        self.new_account.save_account()
        log_in = User("Sharonne", "Vanessa", "sharonnekay23@gmail.com", "shazzykay")
        log_in.save_account()

        account_exists = User.account_exists("sharonnekay23@gmail.com", "shazzykay")
        self.assertTrue(account_exists)

    def test_generate_password(self):
        '''
        test to auto-generate password
        '''
        self.new_account.generate_password() #generating new password
        self.assertEqual(self.new_account.password,"password")


#second test
from user import Credentials

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        
        self.user_credential = Credentials("sharonnevanessa", "sharonnekay23@gmail.com", "shazzykay01" )

    def tearDown(self):
            
        Credentials.user_credentials = []
