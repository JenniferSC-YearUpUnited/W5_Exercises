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

current_hr = time.strftime("%H:%M""%p") #display military hour minutes and pm or am
print(current_hr)

current_hr1 = int(time.strftime("%H")) #casting the display of time to a string as it is not letting me print without converting it first


if current_hr1 >= 5 and current_hr1 <= 9:
    print("Good morning!") # current hours being midnight 00 -9am then between 5 and 9am
elif current_hr1 >= 10 and current_hr1 <= 16:
   print("Good day!") # current hour being 10am through 4pm(1600)
elif current_hr1 >= 17 and current_hr1 <= 22:
  print("Good evening!")  #current hours being 5pm(1700 )through midnight (0000) then current hours being 5pm( 1700)through 11pm (2200)
elif current_hr1 >= 23 and current_hr1 <= 4:
    print("What are you doing up so late??") # updating/ adding for current hours being 11pm(2300) thorugh 4am


  

# try it again tonight to see if it prints the right message for evening and late night
# not giving me the right output for the greeting based on time
# need to change the comparison operators
# run code again tonight






     
    
