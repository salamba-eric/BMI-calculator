import sign_up
import pymongo
from tkinter import *
from pymongo import *
from bson.objectid import ObjectId



window = Tk()
client = MongoClient()

Data_Base = client.BMI
users_data = Data_Base.users_data

#def calculate_bmi():
	# Calculating function #
def metric_calculator():
		# Clear what's on the space #
	BMI_display_entry.delete(0, 'end')
		#Getting the values #
	try:
		height = (int(height_str.get())/100)
		weight = int(weight_str.get())
		BMI = weight/(height*height)
	except ValueError:
		value_error()
		BMI = 0
	
		# What to display #
	if BMI != 0:
		BMI_listbox.delete(0, 'end')
		BMI_display_entry.insert(END ,str(BMI))
		Error_msg1.destroy()
		if BMI <16:
			comment = "You are Severely Underweight"
		elif BMI < 18:
			comment = "You are Underweight"
		elif BMI < 23:
			comment = "You are Healthy"
		elif BMI <29:
			comment = "You are Overweight"
		elif BMI <39:
			comment = "You are Obese"
		else:
			comment = "You are Extremely Obese"

	BMI_listbox.insert(1, "    " + str(BMI))
	BMI_listbox.insert(2 ,comment)


	current_doc = list(users_data.find({},sort = [( '_id', pymongo.DESCENDING )]).limit(1))
	excisting_in_doc = { "BMI" : ""}
	updated_doc = {"$ set" : {"BMI" : 10}}
	data = dict(current_doc[0])
	user_name = data["Username"]
	
	
	users_data.update_one({"Username": user_name },{"$set":{"BMI": BMI }})

					# Window widgets #
	# The labels #
label_1 = Label(window, text = "This will calculate your BMI", fg = "black", font = ("Arial" , 12))
label_2 = Label(window, text = "Input your weight and height below", fg = "black", font = ("Arial" , 12))
height_label = Label(window, text = "Enter your height (cm)", fg = "black", font = ("Arial" , 14))
weight_label = Label(window, text = "Enter your weight (kg)", fg = "black", font = ("Arial" , 14))
BMI_display_label = Label(window, text = "Your BMI is ", fg = "black", font = ("Arial", 14))
list_label = Label(window, text = "Your previous BMI's", font = ("Arial" , 12))
Error_msg1 = Label(window, text = "Input numerals as your height and weight", fg = "red", font = ("Arial", 12))
	#The entrys #
height_str = Entry(window, bg = "white", fg = "black", bd = 3)
weight_str = Entry(window, bg = "white", fg = "black", bd = 3)
BMI_display_entry = Entry(window, font = ("Arial", 12))
	#The buttons#
calculate_button = Button(window,text = "Calculate", bd = 1, font = ("Arial" , 12), command = metric_calculator)
	#The listbox #
BMI_listbox = Listbox(window,width = 30, height = 11, font = ("Raleway" ))

					#Widget placements #
		# labels #
label_1.place(x = 75, y = 25)
label_2.place(x = 50, y = 50)
height_label.place(x = 10, y = 85)
weight_label.place(x = 10, y = 113)
BMI_display_label.place(x = 125, y = 185)
list_label.place(x = 100, y = 265)
		# entrys #
height_str.place(x = 200, y = 90 ,width = 90 , height = 20)
weight_str.place(x = 200, y = 118 ,width = 90 , height = 20)
BMI_display_entry.place(x = 90, y = 210)

		# buttons #
calculate_button.place(x = 125, y = 150)
		# listbox #
BMI_listbox.place(x = 25, y = 285,width = 300, height = 120)

		# Error handling #
def value_error():
	Error_msg1.place(x = 33, y = 240)

  
   #Generating the window #  
window.title("BMI Calculator")
window.geometry("350x500+550+100")
window.mainloop()



