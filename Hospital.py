import os
import pickle

class user:
  name = ""
  second_name = ""
  id = 0
  login = ""
  password = ""
  user_type = ""

class nurse(user):
  working_hours = 0
  user_type = "nurse"


class doctor(user):
 spec_level = ""
 whz = 0
 working_hours = 0
 user_type = "doctor"


class admin(user):
 user_type = "admin"
 def user_creator(_login, _password,_user_type, _name, _second_name):
   global user_count
   user_count +=1
   new_user = user
   new_user.id = user_count 
   new_user.login = _login 
   new_user.name = _name 
   new_user.password = _password 
   new_user.second_name = _second_name 
   new_user.user_type=_user_type 
   if _user_type == "Doctor":
     doc_spec = input("Please name the doctor's specialization")
   global active_users
   active_user = [_name, _second_name, _user_type]
   active_users.append(active_user)
   global users
   users[_login] = _password, _user_type, _name, _second_name
   print("Current user count:" + str(user_count) + "users")
   print("User added sucessfully!")
        
         
     
     
user_count = 0
users =  {}
active_users = []
admin.user_creator("Admin","123", "Admin","Cristian", "Demkowicz")
try:
 users = pickle.load(open("serialized_users.dat", "rb"))
except:
	print("No saved data found")
print(users)



print("Welcome to the hospital managament app!")


check = True

while check == True:
    _login=input("Login:")
    os.system("cls")
    _password=input("Password:")
    os.system("cls")
    try:
     if _login in users[_login] and _password in users[_login]:
        print("Login sucessfull")
        check = False
    except:
        os.system("cls")
        print("Please try again")
        
print("Hello:"+ _login+"!")
print(users[_login])
program_going = True
while program_going == True:

 print("What do you want to do:")
 print("[C]heck other session users?")
 print("[L]ook-up your timetable?")
 print("[Cr]eate new user?")
 print("[E]nd program?")

 action = input("[C] or [L] or [Cr] or [E]?")

 if action == "C":
    os.system("cls")
    print(active_users)
 elif action == "L":
    print("Not yet implemented")
    os.system("cls")
 elif action == "Cr":
     if "Admin" in users[_login]:
         input_login = input("Create new login: ")
         input_password = input("Create new password: ")
         input_name = input("Enter user's name: ")
         input_second_name = input("Enter user's second name: ")
         input_user_type = input("Chose the user account type: Doctor, Nurse, Admin: ")
         admin.user_creator(input_login,input_password,input_user_type,input_name,input_second_name)



    
 elif action == "E":
    serial_users = pickle.dump(users, open("serialized_users.dat", "wb"))
    program_going == False
    break

