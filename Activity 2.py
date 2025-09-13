import math
x1 = float(input("We will use the Euclidean formula to see the distance between two points.\n " 
"Input the coordinates for the 1st point on the x axis:"))
y1 = float(input("Input the coordinates of the y axis of the 1st point:"))
x2 = float(input("Input the coordinates of the 2nd point on the x axis:"))
y2 = float(input("Input the coordinates of the 2nd point on the y axis:"))

d = math.sqrt(pow(x2-x1,2)+ (pow(y2-y1,2)))

round_d = round(d,2)
print ("The distance is", round_d)