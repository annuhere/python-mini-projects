#mini project: Countdown Timer(with 1-second gap)

#goal:
#print a countdown before something "exciting" happens (like "launching.." or "happy new year!").

#concepts used: for loops,range(),and the time module.
import time

count=int(input("Enter the counter number: "))
print(" COUNTDOWN START...")

for i in range(count,0,-1):
    print(i)
    time.sleep(1)
print("All Set To Go😊!")
