import time
#import time module 

my_time=int(input("Enter the time in seconds: "))
#take the input from the user in seconds and convert it to integer
for x in range(my_time,0,-1) :
 seconds=x%60
 #calculate the seconds
 minutes=int(x/60)%60
 #calculate the minutes
 hours=int(x/3600)
 #calculate the hours
 print(f"{hours:02}:{minutes:02}:{seconds:02}")
 time.sleep(1)
 #time.sleep() function is used to delay the execution of the program for 1 second


print("Time's up!")
#finally when the countdown is over, print "Time's up!"