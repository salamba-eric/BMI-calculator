from tkinter import *
from pymongo import *
window_sign_in = Tk() 
client = MongoClient()

Data_Base = client.BMI
users_data = Data_Base.users_data

profile = {"user_name" : "Eric" , "gender" : "male" , "Body_mass_Idex" : 20}
user1 = users_data.insert_one(profile)






	# A sign in window #
# window_sign_in.title("Sign in")
# window_sign_in.geometry("350x350+570+100")
# window_sign_in.mainloop()