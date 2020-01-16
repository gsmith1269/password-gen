import random
import string
x = 0   #the variable "x" is a confermation variable to chech when a specific set of questions are done.
accountset = 1
program = str("active")
print(
'''
This program is to help you organize accounts and passwords (as well as generate passwords).
Program created by: Graeson Smith 
''')
while program == str("active"):
  while accountset == 1:
    menuselect = int(input('''
                  _______                           _____ 
    |\      /|   |          |\   |   |      |     _|_____|_
    | \    / |   |-------   | \  |   |      |     |       |
    |  \  /  |   |          |  \ |   |      |     |   L   |
    |   \/   |   |_______   |   \|   |______|     |_______|

    1) Start Program (available)
    2) See Saved Accounts (unavailable)      
    3) Edit Saved Accounts
    4) Exit (unavailable)
    5) Reset Saved Accounts (unavailable)
  
    Input: '''))
    if menuselect == int(1):
      account = input("What website/social media/program is this login for? ")
      if account == str("dev"):
        username = str("dev")
        password = str("dev")
        email = str("dev")
        x = int(input('''Input step:
                Username = 0
                Password = 1
                Email = 2
                Final = 3
                Input: '''))
      accountset = 0
    if menuselect == int(2):
      f= open("Password.txt", "r")
    #if menuselect == int(3):
    #if menuselect == int(4):
  while accountset == 0:
    #-----------USERNAME SET------------------------------------------------------#
    if x == 0:
      username = input(str("Hello. What would you like your username to be? "))
      confirm = input(str("Type your username again to confirm: "))
      if confirm == username:
        print("Username confirmed. Hello " + username)
        print(" ")
        x = 1
      else:
        print("Username not confirmed. Try again. ")
        print("")
        x = 0
    #-----------PASSWORD SET------------------------------------------------------#
    if x == 1:
      a = input("Would you like to have a randomly generated password? Y/N? ")
      if a == str("Y"):
        passlength = int(input("How long would you like your password to be? (Numbers only) "))
        def randomString(stringLength):
          letters = string.ascii_letters + string.digits
          return ''.join(random.choice(letters) for i in range(stringLength)) 
        print("Your password is: ")
        password = (randomString(passlength))
        print(password)
        passconfirm = input("Is this okay? Y/N? ")
        if passconfirm == ("Y"):
          x = 2
          print("Password set.")
        if passconfirm == ("N"):
          a = str("Y")
          password = str("")
          print("Proceed and try again.")
      if a == str("N"):
        password = input(str("Type in password "))
        x = 2
        print("Password set.")
    #-----------EMAIL INFO--------------------------------------------------------#
    if x == 2:
      emailcheck = input("Do you have an email you would like to tie to this account? Y/N? ")
      if emailcheck == str("Y"):
        email = input("What email would you like to tie to this account? ")
        x = 3
      if emailcheck == str("N"):
        emailcheck2 = input("No email, correct? Y/N? ")
        if emailcheck2 == str("Y"):
          email = str("None")
          x = 3
        if emailcheck2 == str("N"):
          print("Add email.")
          x = 2
    #-----------FINAL INFO PAGE---------------------------------------------------#
    if x == 3:
      print("1) ", username)
      print("2) ", password) 
      print("3) ", email) 
      FIConfirm = input("Are these correct? Y/N? ")
      if FIConfirm == str("Y"):
        f= open("Password.txt", "w+")
        f.write("Account: " + account + " Username: " + username + " Password: " + password + " Email: " + email)
        print("Everthing is correct. Here is your account information for your " + account + " account. Data stored" )
        f.close
        x = 4
        accountset = 1
      if FIConfirm == str("N"):
        resitem = int(input("Which is incorrect (use number value)? "))
        if resitem == 1:
          x = 0
        if resitem == 2:
          x = 1
        if resitem == 3:
          x = 2