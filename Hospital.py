import os
import pickle

class user:
 
 def __init__(self, login, password, usertype, first, last):
     self.login = login
     self.password = password
     self.usertype = usertype
     self.first = name
     self.last = last

class nurse(user):
  working_hours = 0
  user_type = "nurse"


class doctor(user):
 spec = ""
 whz = 0
 working_days = 0
 user_type = "doctor"


class admin(user):
 user_type = "admin"

 def user_creator():

   global active_nurses
   global active_doctors
   global active_admins

   _login = input("Create new login: ")
   os.system("cls")
   _password = input("Create new password: ")
   os.system("cls")
   _name = input("Enter user's name: ")
   os.system("cls")
   _second_name = input("Enter user's second name: ")
   os.system("cls")
   _user_type = input("Chose the user account type: Doctor, Nurse, Admin: ")
   os.system("cls")
   
   if _user_type == "Doctor":
      new_doctor = _login
      new_doctor = doctor
      new_doctor.first = _name
      new_doctor.second = _second_name
      new_doctor.login = _login
      new_doctor.password = _password
      new_doctor.user_type = "Doctor"
      new_doctor.whz = input("Please enter WHZ of a doctor: ")
      new_doctor.spec = input("Please enter specialization of a doctor: ")
      new_doctor.working_days = 0
      active_doctors.append([new_doctor.first, new_doctor.second, new_doctor.spec])
      
   elif user_type == "Nurse":
      new_nurse = _login
      new_nurse = nurse
      new_nurse.login = _login
      new_nurse.password = _password
      new_nurse.user_type = "Doctor"
      new_nurse.working_days = 0
      active_doctors.append(new_doctor)
   
   global users
   users[_login] =_login, _password, _user_type, _name, _second_name
   print("Current user count:" + (str)(len(users)) + "users")
   print("User added sucessfully!")
        
os.system("mode con cols=180 lines=50")

active_nurses = []
active_doctors = []
active_admins= []     
user_count = 0
users = {}
active_users = []
monthly_timetable = {}
try:
 users = pickle.load(open("serialized_users.dat", "rb"))
except:
	print("No saved data found")
try:
 active_users = pickle.load(open("serialized_active_users.dat", "rb"))
except:
 print("No saved data found")


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
    print("Our doctors")
    print('\n'.join(map(str, active_doctors)))
    print(active_nurses)
    if "Admin" in users[_login]:
     print(active_admins)
 elif action == "L":
    
    os.system("cls")
 elif action == "Cr":
     if "Admin" in users[_login]:
         admin.user_creator()
         

    
 elif action == "E":
    serial_users = pickle.dump(users, open("serialized_users.dat", "wb"))
    serial_active_users = pickle.dump(users, open("serialized_active_users.dat", "wb"))
    program_going == False
    break

