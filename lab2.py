__author__ = 'Illya King'

#   Input List: fahrenheit
#   Output List: fahrenheit, celsius
#
#   Declare Integer fahrenheit
#   Declare Integer celsius
#
#   Display welcome message
#
#   Display "What is the Fahrenheit Temperature? "
#   Input fahrenheit
#   Set celsius = (fahrenheit - 32) * 0.5555555555555556
#   Display "In Celsius, the temperature is ", celsius, "degrees."

fahrenheit = 0
celsius = 0

print ("Convert Fahrenheit to Celsius")
print ("Enter the Fahrenheit Temperature")

fahrenheit = int(input("What is the Fahrenheit Temperature? "))
celsius = int((fahrenheit - 32) * 0.5555555555555556)
print ("In Celsius, the temperature is", celsius, "degrees.")

#   Input List: freight_length, freight_width, freight_height, freight_weight
#   Output List : freight_length, freight_width, freight_height, freight_weight, cubic_foot, pounds_per_cubic_foot = 0.0
#   Declare Real freight_length
#   Declare Real freight_width
#   Declare Real freight_height
#   Declare Real freight_weight
#
#   Display welcome message
#   Display "What is freight's length? "
#   Input freight_length
#   Display "What is the freight's width? "
#   Input freight_width
#   Display "What is the freight's height? "
#   Input freight_height
#   Display "What is the freight's weight? "
#
#   Set cubic_foot = (freight_length * freight_width * freight_height) / 1728
#   Set pounds_per_cubic_foot =  freight_weight / cubic_foot
#
#   Display "Your freight had a dimension of", freight_length, "x" , freight_weight, "x", freight_height
#   Display "Which means this freight is", "{:.2f}".format(cubic_foot), "Cubic Feet "
#   Display "The weight of the freight is", freight_weight, "lbs"
#   Display "Which means this freight is", "{:.2f}".format(pounds_per_cubic_foot), "pounds per cubic foot."

freight_length = 0.0
freight_width = 0.0
freight_height = 0.0
freight_weight = 0.0
cubic_foot = 0.0
pounds_per_cubic_foot = 0.0

print("Welcome to the Dimensions Calculator!")
print("Please inter in the dimensions of the freight.")
print("")
84\

freight_length = float(input("What is freight's length? "))
freight_width= float(input("What is the freight's width? "))
freight_height = float(input("What is the freight's height? "))
freight_weight = float(input("What is the freight's weight? "))

cubic_foot = (freight_length * freight_width * freight_height) / 1728
pounds_per_cubic_foot = freight_weight / cubic_foot

print("Your freight had a dimension of", freight_length, "x" , freight_weight, "x", freight_height)
print("Which means this freight is", "{:.2f}".format(cubic_foot), "Cubic Feet ")
print("The weight of the freight is", freight_weight, "lbs")
print("Which means this freight is", "{:.2f}".format(pounds_per_cubic_foot), "pounds per cubic foot.")
