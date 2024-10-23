import math
length_of_room=int(input("what is the length of your room in feet? "))
width_of_room=int(input(" What is the width of your room in feet? "))

ttl_boxes=(length_of_room* width_of_room)/12 
extra=(ttl_boxes*.10) + ttl_boxes
print(" The total amount of boxes for tile you will need, including extra tile for mess-ups are", math.ceil(extra), "boxes")