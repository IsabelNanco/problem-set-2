"""
NTEC 361
Date: 04/23/2022
Isabel Nanco
Assignment Name: Problem Set No. 2
Description: Simple coding problems to reinforce topics covered in Modules 0, 1, 2 and 3
"""

""" IPO template
Input(s):   Weight
            Height 
            BMI
Process: 
            BMI = weight in Kilograms / height in meters squared = w/h2.
            Height = convert inches to meters 
            Weight = convert pounds to kilograms 
            kilograms 
            meters 

Output: 
        Taking the input from the user 
        Taking the weight in pounds and multiplying by .454 to get Kg.
        Taking the Height in inches and multiplyig 0.254 m^2 
        Taking the weight_in_kg / (height_in_meters * height_in_meters) to get BMI 
  
      
"""


def main():

    print("Body Mass Index")


# Ask user for input weight in pounds.
weight_in_pounds = float(input("Enter your weight in pounds : "))


# Ask user for input height in inches.
height_in_inches = float(input("Enter your height in inches : "))


# First convert the weight in kg and height in meters for BMI.
# Then, weight_in_kg will be: weight_in_pounds * 0.454
weight_in_kg = weight_in_pounds * 0.454


# height_in_meters will be: (height_in_inches * 2.54)/100
height_in_meters = (height_in_inches * 2.54)/100


# last, BMI will be: weight_in_kg / (height_in_meters * height_in_meters).
BMI = weight_in_kg / (height_in_meters * height_in_meters)


# Printing the details.
print("Calculate Body Mass Index")

# Printing the height and weight and BMI.
print("Weight: \t", weight_in_pounds, "lbs. \t", weight_in_kg, " kg")
print("Height: \t", height_in_inches, "in. \t", height_in_meters, " m")
print("BMI: \t", BMI)

main()

"""
NTEC 361
Date: 04/23/2022
Isabel Nanco 
Assignment Name: Problem Set No. 2
Description: Simple coding problems to reinforce topics covered in Modules 0, 1, 2 and 3
"""

""" IPO template
Input(s):   
        Pay 
        hours
        Gross Pay 
        taxes 
        Net Pay 
Process: 
        Pay = hours * pay rate 
        hours = the hours worked 
        Gross pay = hours worked * hourly rate
        Net Pay = gross pay - taxes 
        Tax = the tax percentage * pay 
Output: Taking the input from the user 
        storing rate in rate variable 
        calculate pay by multiplying hours and rate 
        calculate tax 12.5% of pay 
        net pay is total pay - taxes 
 
"""


def main():
    print("Simple Pay Program")
    # taking input from the user
    hours = float(input("Enter the number  of hours worked: "))

    # storing rate in rate variable
    rate = 25
    # calculate pay by multiplying hours and rate
    pay = hours * rate
    # calculate tax 12.5% of pay
    tax = 0.125 * pay
    # net pay is total pay - taxes
    netPay = pay - tax

    # Print all
    print("Income")
    print("Hours: ", hours)
    print("Rate: 25.00")
    print("Pay: ", pay)
    print("Tax: ", tax)
    print("Net Pay: ", netPay)


main()

"""
NTEC 361
Date: 04/23/2022
Isabel Nanco
Assignment Name: Problem Set No. 2
Description: Simple coding problems to reinforce topics covered in Modules 0, 1, 2 and 3
"""

""" IPO template
Input(s): Starting location
          Ending location
          Distance between the two locations
          Travel duration (use 60 m/hr for your calculation)

Process: Ask the user for the initial_location.
         Ask then end_location
         The distance between the location 
         time = distance / speed.
Output: 
        duration = distance / 60

"""


def main():
    print("Travel Time")


# Ask the user for the initial_location.
initial_location = input("Enter the initial_location: ")

# Then we, ask for the end_location.
end_location = input("Enter the end_location: ")


# Finally, ask for the distance between the locations.
distance = int(input("Enter the distance between the locations: "))


# As we know: time = distance / speed.
# So, the duration will be: distance/60
duration = distance / 60

# Printing out the details.
print("Travel Time Details")

# Printing the initial_location, end_location, distance and the duration.
print("Start: \t\t", initial_location)
print("End: \t\t", end_location)
print("Distance: \t", distance)
print("Duration: \t", duration)

main()
