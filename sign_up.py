from tkinter import *
from pymongo import *
from tkinter.ttk import Combobox



window_sign_in = Tk() 
client = MongoClient()
sex = StringVar()

Data_Base = client.BMI
users_data = Data_Base.users_data

	# constants #
months = list(("01","02","03","04","05","06","07","08","09","10","11","12"))

days = list(())
day = 0
while day != 31:
	day += 1
	days.append(day)


		# functions #

def signing_in():

	user_name = user_entry.get()
	gender = str(sex.get())
	set_day = day_combobox.get()
	set_month = month_combobox.get()
	date = str(set_day + "/" + set_month)

	profile = { "Username" : user_name , "Date  " : date ,"Gender" : gender , "BMI" : ""}

	users_data.insert_one(profile)

	window_sign_in.destroy()


def finish():
	sign_in_button.place(x = 100, y = 165 , width = 100 , height = 25)

	set_day = day_combobox.get()
	set_month = month_combobox.get()
	date = str(set_day + "/" + set_month)

		# Widgets #
	# Labes #
label_1 = Label(window_sign_in, text = " Sign in ", font = ("Arial" , 17))
user_label = Label(window_sign_in, text = "Username :", font = ("Arial" , 15))
day_label = Label(window_sign_in, text = "Day  :" , font = ("Arial", 12))
month_label = Label(window_sign_in, text = "Month  :" , font = ("Arial", 12))
	# Entrys #
user_entry = Entry(window_sign_in, bd = 3)

	# Buttons #
sign_in_button = Button(window_sign_in, text = " Done ", command = signing_in )
	# Radiobutton #
male_button = Radiobutton(window_sign_in, text = "male", borderwidth = 0, variable = sex, value = "male", font = ("Arial" , 12), command = finish)
female_button = Radiobutton(window_sign_in, text = "female", borderwidth = 0, variable = sex, value = "female", font = ("Arial" , 12), command = finish)
	# Combobox #
day_combobox = Combobox(window_sign_in, values = days)
month_combobox = Combobox(window_sign_in, values = months)

		# Widget placement #
			# Labels #
label_1.place(x = 90 , y = 0)
user_label.place(x = 5 , y = 45)
day_label.place(x = 50, y = 90)
month_label.place(x = 150, y = 90)
			# Entry #
user_entry.place(x = 115 , y = 50 , width = 175)
			#Radiobutton #
male_button.place(x = 65 , y = 130)
female_button.place(x = 175 , y = 130)
			# Combobox #
day_combobox.place(x = 100, y = 90 , width = 45)
month_combobox.place(x = 200 , y = 90 , width = 45)


	# A sign in window #
window_sign_in.title("Sign in")
window_sign_in.geometry("300x200+570+100")
window_sign_in.mainloop()