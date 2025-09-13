import math

rad = float(input("Area of circle calculator. Please inuput the radius: "))
area =math.pi*(pow(rad,2))
twodecimalarea = round(area, 2)
print ("Your area is", twodecimalarea)  