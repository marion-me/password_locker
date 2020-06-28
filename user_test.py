class User:
        """
        Class to generates new instances of users.
        """
        
        user_list = [] #Empty user list
        def save_user(self):
          """
          save user method saves user objects into user_list
          """
          User.user_list.append(self)
        

        def __init__(self,user_name,account,password):
    
          # docstring removed for simplicity
      
           self.user_name = user_name
           self.account = account
           self.password = password