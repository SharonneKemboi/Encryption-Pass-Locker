import random  #to generate the pseudo-random variables, in this case the random passwords

class User:
    """
    Class that generates new instances of user
    """

    user_createaccount = [] # create a variable that will be used to store our created user objects .
    
    def _init_(self,first_name,last_name,email,password):
         '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New user first name.
            last_name : New user last name.
            email: New user email address.
            password : New user password 
        '''

         self.first_name = first_name
         self.last_name = last_name
         self.email = email
         self.password = password

    def save_account(self):
        User.user_createaccount.append(self) #Create a save_account method that is called on a user object and appends it .


    def generate_password(self):
        '''
        generate new password
        ''' 
        ## characters to generate password from
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

        ## length of password from the user
        length = int(input("Please Enter Preferred Password Length: "))

        ## shuffling the characters
        random.shuffle(characters)

        ## picking random characters from the list
        password = []
        for i in range(length):
            password.append(random.choice(characters))

        ## shuffling the resultant password
        random.shuffle(password)

        ## converting the list to string
	    ## printing the list
        print(password)

       




