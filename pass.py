#Karen Chut Ling
#20DDT21F1009
nf = open ("password.txt","w")
nf.write ("abc123")
nf.write ("\n123")
nf.write ("\nsun")
nf.write ("\n0000")
nf.write ("\n1200")
nf.close()
         
                       
class PasswordManager :
     
     def __init__(self, old_password):
          self.old_password = old_password

     def get_password(self):
          get_new_password = self.old_password[-1]
          return get_new_password
     
     def set_password(self, attempted_password):
          print(f"Please Enter your new password :{attempted_password}")
          if attempted_password not in self.old_password:
               jwpn = input(f"Are you sure you want to add {attempted_password} to password.txt? (Yes, No) \n")
               if jwpn == 'Yes':
                    with open('password.txt', 'a') as newpass:
                         newpass.write('\n' + attempted_password)
                    print(f'Your new password will be added')
               elif jwpn == 'No':
                    print(f"{attempted_password} will not be added to the password list.")
               else:
                    print("Invalid input. Please choose either 'Yes' or 'No'.")

     def is_correct(self, attempted_password):
          if attempted_password == object1.get_password():
               print('It is your password.')
          else:
               self.set_password(attempted_password)

list_of_password = open("password.txt").read().splitlines()
print(list_of_password)

newpass = input("Please enter your password: ")

object1 = PasswordManager(list_of_password)
object1.is_correct(newpass)



          
     
