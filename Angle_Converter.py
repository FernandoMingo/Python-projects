import math
print("Lets convert rad to deg. (note that pi is already included)")
a = input("Enter the numerator: ")
b = input("Enter the denominator: ")
a = int(a)
b = int(b)
ivangle = int(a / b)
convertang = ivangle*math.pi * 180 / math.pi
print("Your angle is:", convertang, "degrees")
