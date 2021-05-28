from tkinter import *

window = Tk()

	# Calculating function #
def metric_calculator():
		# Clear what's on the space #
	BMI_display_entry.delete(0, 'end')
		#Getting the values #
	height = (int(height_str.get())/100)
	weight = int(weight_str.get())
		# Actual calculator #
	BMI = weight/(height*height)
		# What to display #
	BMI_display_entry.insert(END ,str(BMI))

		# Window widgets #
	# The labels #
label_1 = Label(window, text = "This will calculate your BMI", fg = "black", font = ("Arial" , 12))
label_2 = Label(window, text = "Input your weight and height below", fg = "black", font = ("Arial" , 12))
height_label = Label(window, text = "Enter your height (cm)", fg = "black", font = ("Arial" , 14))
weight_label = Label(window, text = "Enter your weight (kg)", fg = "black", font = ("Arial" , 14))
BMI_display_label = Label(window, text = "Your BMI is ", fg = "black", font = ("Arial", 14))
	#The entrys #
height_str = Entry(window, bg = "white", fg = "black", bd = 3)
weight_str = Entry(window, bg = "white", fg = "black", bd = 3)
BMI_display_entry = Entry(window, font = ("Arial", 12))
	#The buttons#
calculate_button = Button(window,text = "Calculate", bd = 1, font = ("Arial" , 12), command = metric_calculator)

	#Widget placements #
		# labels #
label_1.place(x = 75, y = 25)
label_2.place(x = 50, y = 50)
height_label.place(x = 10, y = 125)
weight_label.place(x = 10, y = 153)
BMI_display_label.place(x = 125, y = 420)
		# entrys #
height_str.place(x = 200, y = 130 ,width = 90 , height = 20)
weight_str.place(x = 200, y = 158 ,width = 90 , height = 20)
BMI_display_entry.place(x = 90, y = 445)
		# buttons #
calculate_button.place(x = 125, y = 200)

  
   #Generating the window #  
window.title("BMI Calculator")
window.geometry("350x500+550+100")
window.mainloop()
