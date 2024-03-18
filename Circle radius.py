# Shehraan Hafiz
# July 4, 2023
# Mr. Manyanga
# This Program will find the radius of Pi

#VARIABLES USED: Use meaningful variable name
#Programs must be USER-Friendly - Program should NEVER crash

#INPUT - asking the user for the value of the correct radius
while True:
    pi = 3.142
    unit = input("Choose your desired units to find the radius of a circle: ")
    radius = input("Enter the radius of a circle in your desired units: ")
    while radius.isalpha()==True or float(radius)<0:
        print("Error, you entered a character which is incompatible with this program. Please try again.")
        radius = input("Enter the radius of a circle in your desired units: ")
    
    #PROCESS - Calculating the area and perimeter of the circle using the radius
    radius = float(radius)
    area = str(round(pi*radius**2))
    perimeter = str(round(2*pi*radius))

    #OUTPUT - Printing the calculated area and perimeter
    print("The area of the circle is: "+area+unit)
    print("The perimeter of the circle is: "+perimeter+unit)
    redo = input("Would you like to check the perimeter and area of another circle (y/n)?")
    if redo!="y" and redo!= "n":
        print("Please only enter either 'y' or 'n'")
        redo = input("Would you like to check the perimeter and area of another circle (y/n)?")
    elif redo=="n":
        break


