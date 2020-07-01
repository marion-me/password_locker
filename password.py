import unittest #Importing the unittest module
import pyperclip
from user import User
from credential import Credentials

class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the contact class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("mia","Instagram","1234")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly.
        """
        self.assertEqual(self.new_user.user_name,"mia")
        self.assertEqual(self.new_user.account,"Instagram")
        self.assertEqual(self.new_user.password,"1234")

    def test_save_user(self):
        """
        test_save_user test case to test if the contact object is saved into the user list.
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

"""
======================================================================================================================
"""            
class TestCredential(unittest.TestCase):

    """
    Test class that defines test cases for the contact class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credentials("Instagram","maria_ mia","mase")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly.
        """
        self.assertEqual(self.new_credential.account,"Instagram")
        self.assertEqual(self.new_credential.username,"maria_ mia")
        self.assertEqual(self.new_credential.account_password,"mase")
    
    def test_save_credential(self):
        """
        test_save_credential test case to test if the crendential object is saved into the credential list.
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),1)
    def tearDown(self):
        """
        tearDown method that does clean up for each test when run.
        """
        Credentials.credential_list = []

    def test_save_multiple_credential(self):
        """
        test that can save multiple credential object to our credential_list.
        """
        self.new_credential.save_credential()
        test_credential = Credentials("account","username","account_password") 
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_credential(self):
        """
        test_delete that remove a credential from our credential_list.
        """
        self.new_credential.save_credential()
        test_credential = Credentials("account","username","account_password")
        test_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credential_list),1)  

    # def test_find_by_credential(self):
    #     """
    #     test to check if we can find a contact by username and display information.
    #     """
    #     self.new_credential.save_credential()
    #     test_credential = Credentials("account","username","account_password")
    #     test_credential.save_credential()

    #     find_credential = Credentials.find_by_credential("Twitter")

    #     self.assertEqual(find_credential.account,test_credential.account)         


   
    def test_credential_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the credential.
        """

        self.new_credential.save_credential()
        test_credential = Credentials("account","username","account_password")
        test_credential.save_credential()

        credential_exist = Credentials.credential_exist("account")

        self.assertTrue(credential_exist)

    def test_display_credential(self):
        """
        method that return a list of all credential and save
        """    

        self.assertEqual(Credentials.display_credential(),Credentials.credential_list)

    def test_search_credential(self):
        """
        method that search a list of all credential 
        """
        self.assertEqual(Credentials.search_credential(),Credentials.credential_list)    


    

if __name__ == '__main__':
    unittest.main()     
