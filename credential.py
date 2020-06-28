class Credentials:
    """
    Class that generates new instances of user credentials.
    """
    credential_list = [] # Empty credential list
    def __init__(self,account,username,account_password):
        """
        method that defines user credentials and stored
        """
        self.account = account
        self.username = username
        self.account_password = account_password 
    def save_credential(self):
        """
        method to store a new credential to the credential_list.
        """
        Credentials.credential_list.append(self)

    def delete_credential(self):
        """
        delete_credential method deletes a saved credential form the credential_list
        """
        Credentials.credential_list.remove(self)     
    


    @classmethod
    def credential_exist(cls,account):
        """
        Method that checks if a credential exists from the credential list .
        Args:
            name: account to search if it exists
        Return :
            Boolean: True or false depending if the credential exists  
         """
        for credential in cls.credential_list:
            if credential.account == account:
                    return True
        return False            
    
    @classmethod
    def display_credential(cls):
        """
        method that return credential list
        """
        return cls.credential_list    

    @classmethod
    def search_credential(cls):
        """
        method that search credentiak list
        """
        return cls.credential_list    