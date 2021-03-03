'''
----------------------------------------------------------------------
Name:   problem2.py

Purpose:  This program calculates how many days it takes for Tony to drive over 100km as well as the average number of kilmoters he drove during each of those days

Author: Guo.T
 
Created:  03/03/2021
----------------------------------------------------------------------
'''
print("*****  Welcome to the DoorDash Distance Tracker *****")
print()

#initialize variables for the total number of days and the total distance
days = 0
distance = 0 

#while the total distance is not over 100, ask user for input and add it to the total distance while incrementing total days by 1
print("** Travel Log **")
while(distance <= 100):
  current_day = int(input("Enter the distance travelled for the day (in km): "))
  days += 1
  distance += current_day

#calculate the average km/day
average = round(distance/days)

#output results
print()
print("** Summary **")
print("It took", days, "days to surpass 100km driven.")
print("The average distance driven per day is", average, "km.")