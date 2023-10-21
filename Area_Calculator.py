import math
print("Lets calculate the area of a polygon!")
polygon_type = input("Enter the number of sides: ")
base = input("Enter the width of the base: ")
polygon_type = float(polygon_type)
base = float(base)
if polygon_type < 3 :
    print("That's not a polygon, try again")
    quit()

def calcarea(polygon_type, base) :
    angle_ext = math.pi - (math.tau / (polygon_type * 2)- (math.pi / 2))
    angle_int = math.tau / (polygon_type * 2)
    angle_ext = math.sin(angle_ext)
    angle_int = math.sin(angle_int)
    height = (angle_ext * (base / 2)) / angle_int
    area = base * polygon_type * height / 2
    return(-area)

print(calcarea(polygon_type, base))
