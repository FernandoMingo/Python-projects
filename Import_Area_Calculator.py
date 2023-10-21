import Area_Calculator
print("Lets calculate the area of a polygon!")
polygon_type = input("Enter the number of sides: ")
base = input("Enter the width of the base: ")
polygon_type = float(polygon_type)
base = float(base)
if polygon_type < 3 :
    print("That's not a polygon, try again")
    quit()
Area_Calculator.calcarea(polygon_type, base)

