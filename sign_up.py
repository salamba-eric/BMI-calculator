from tkinter import *
from pymongo import *

# from BMI_calculator import calculate_bmi


window_sign_in = Tk() 
client = MongoClient()
sex = StringVar()

Data_Base = client.BMI
users_data = Data_Base.users_data

		# Classes #


		# functions #
def data_sender():
	pass
def signing_in():

	user_name = user_entry.get()
	gender = str(sex.get())
	profile = { "Username" : user_name , "Gender" : gender , "BMI" : ""}

	users_data.insert_one(profile)

	data_sender()
	window_sign_in.destroy()


def finish():
	sign_in_button.place(x = 100, y = 165 , width = 100 , height = 25)

		# Widgets #
	# Labes #
label_1 = Label(window_sign_in, text = " Sign in ", font = ("Arial" , 17))
user_label = Label(window_sign_in, text = "Username :", font = ("Arial" , 15))
password_label = Label(window_sign_in, text = "Password  :" , font = ("Arial", 15))
	# Entrys #
user_entry = Entry(window_sign_in, bd = 3)
password_entry = Entry(window_sign_in, bd = 3)
	# Buttons #
sign_in_button = Button(window_sign_in, text = " Done ", command = signing_in )
	# Radiobutton #
male_button = Radiobutton(window_sign_in, text = "male", borderwidth = 0, variable = sex, value = "male", font = ("Arial" , 12), command = finish)
female_button = Radiobutton(window_sign_in, text = "female", borderwidth = 0, variable = sex, value = "female", font = ("Arial" , 12), command = finish)


		# Widget placement #
			# Labels #
label_1.place(x = 90 , y = 20)
user_label.place(x = 5 , y = 65)
password_label.place(x = 2, y = 90)
			# Entry #
user_entry.place(x = 115 , y = 70 , width = 175)
password_entry.place(x = 115, y = 95 , width = 175)
			#Radiobutton #
male_button.place(x = 65 , y = 130)
female_button.place(x = 175 , y = 130)


def test2():
	number = 2



	# A sign in window #
window_sign_in.title("Sign in")
window_sign_in.geometry("300x200+570+100")
window_sign_in.mainloop()