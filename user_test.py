import unittest #importing the unittest module
import pyperclip
from user import User #import the class from user file.

#firstclass
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


#second class 
from user import Credentials

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        
        self.user_credential = Credentials("sharonnevanessa", "sharonnekay23@gmail.com", "shazzykay01" )

    def tearDown(self):
            
        Credentials.user_credentials = []

    def test_init(self):
        self.assertEqual(self.user_credential.account_name, "sharonnevanessa")
        self.assertEqual(self.user_credential.email, "sharonnekay23@gmail.com")
        self.assertEqual(self.user_credential.password, "shazzykay01")
    
    def test_save_credentials(self):
        self.user_credential.save_credentials()
        self.assertEqual(len(Credentials.user_credentials), 1)

    def test_save_multiple_credentials(self):
        self.user_credential.save_credentials()
        test_Credentials = Credentials("account_name", "email", "password")
        test_Credentials.save_credentials()

        self.assertEqual(len(Credentials.user_credentials), 2)
    
    def test_delete_credentials(self):
        self.user_credential.save_credentials()
        test_Credentials = Credentials("account_name", "email", "password")
        test_Credentials.save_credentials()

        self.assertEqual(len(Credentials.user_credentials), 1)

    def test_display_credentials(self):
        self.assertEqual(Credentials.display_credentials(),Credentials.user_credentials)

    def test_find_account(self):
        self.user_credential.save_credentials()

        test_Credentials = Credentials("sharonnevanessa", "sharonnekay23@gmail.com", "shazzykay01" )
        test_Credentials.save_credentials()

        found_account = Credentials.find_by_account_name("sharonnevanessa")

        self.assertEqual(found_account.email,test_Credentials.email)

    def test_copy_account(self):
        '''
        Test to confirm that we are copying a credential from the accounts found
        '''
        self.user_credential.save_credentials()
        Credentials.copy_credential("shazzykay01")
    
        self.assertEqual(self.user_credential.password,pyperclip.paste())
    
if __name__ == '__main__':
    unittest.main()
    