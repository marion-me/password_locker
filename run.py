#!/usr/bin/env python3.6
from user import User
from credential import Credentials

def create_user(user_name,account,password):
    """
    Function that create a new user
    """
    new_user = User(user_name,account,password)
    return new_user

def save_user(user):
    """
    Function to save user
    """  
    user.save_user()

def generate_password():
    """
    Function that generates a password
    """
    generate_password = Credentials.generate_password()
    return generate_password


def create_credential(account,username,account_password):
    """
    Function that create a new credential
    """   
    new_credential = Credentials(account,username,account_password)
    return new_credential

def save_credential(credential):
    """
    Function that save credential
    """   
    credential.save_credential()

def del_credential(credential):
    """
    Function that delete credential 
    """    
    credential.delete_credential()

def display_credential():
    """
    Function that return all saved credential
    """
    return Credentials.display_credential() 

def search_credential():
    """
    Function that return all saved credential
    """
    return Credentials.search_credential() 



def main():
    print("Hello Welcome to password locker. Enter your name ?....")
      
    user_name = input()
    
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
                    
          print("use these short code: cc - create a new credential, dc - saving credential, sc - search credential, ex - log out") 

          short_code = input('Enter your choice: ').lower()

          if short_code == "cc":
              print("Create a new account:")
              print("="*10)

              print("username ...")
              user_name = input()

              print ("account ...")
              account = input()

              print ("Password ...")
              password = input()

              save_credential(create_credential(account, user_name, password))
              print('\n')
              print(f"New Credential {user_name} {account} {password} created")
              print('\n') 


          elif short_code == "dc":

                  if display_credential():
                        print ("Here  are the list of all your credential")
                        print('\n')

                        for credential in display_credential():
                            print(f"credential {user_name} {account}   ...{password} ")
                            print('\n') 
                  else:
                            print('\n')
                            print("you credential have not been saved yet") 
                            print('\n')  
          elif short_code == "sc":
                  if search_credential():
                         print("Here are the list of searching for credential")
                         print('\n')

                         for credential in search_credential():
                                 print(f"credential--- {account}") 
                                 print(f"credential--- {user_name}")
                                 print(f"credential--- {password}")
                                 print('\n')                 
      

          elif short_code == "ex":
                            
                  print("Bye .....")
                  break
          else:
                  print("i really didn't get that .Please use the short codes")

if __name__ == '__main__':
    main()