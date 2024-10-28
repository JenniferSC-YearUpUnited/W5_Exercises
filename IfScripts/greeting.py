# define the known values
#current_hour = 4

# calculate the unknown and display result
# tried match/case but could not get any comparison operators to work
#if current_hour <=9:
    #print('Good morning!')
#elif current_hour <= 16:
#   print('Good day!')
#elif current_hour <= 10:
 # print('Good evening!')    
#elif current_hour >=22 and (current_hour <= 4):
 #   print(' What are you doing up so late???')
#else: 
 #   print('Invalid Military Hour Only- No Minutes!')    


## Need to work on last question 

import time

current_hr = time.strftime("%H:%M""%p")
print(current_hr)

current_hr1 = int(time.strftime("%H"))

morning_greeting = "Good morning!"
day_greeting = "Good day!"
evening_greeting = "Good evening!" 
latenight_greeting = "What are you doing up so late??"

if 5 >= current_hr1 <=9:
    print(morning_greeting)
elif current_hr1 <= 16:
   print(day_greeting)
elif current_hr1 <= 10:
  print(evening_greeting)    
elif 22 >= current_hr1 <= 4:
    print(latenight_greeting)
else:
   print("Get some rest!")    

#try it again tonight to see if it prints the right message for evening and late night






     
    
