import math
x2=int(input(" What is your x2 point value on a coord_plane? "))
x1=int(input(" What is your x1 point value on a coord_pane? "))
y2=int(input(" What is your y2 point value on a coord_plane? "))
y1=int(input(" What is your y1 point value on a coord_plane? "))

cal1=((x2-x1)**2) + ((y2-y1)**2)
cal2=math.sqrt(cal1)
print(" The distance between points", (x2,x1, "and points ", (y2,y1), "is: ", format(cal2, ".2f"))) 
                                       
#print(cal2)
#print(type(cal2))
#print(cal1)
#print(type(cal1))
       