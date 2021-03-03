'''
----------------------------------------------------------------------
Name:   problem1.py

Purpose:  This program places players into seperate groups based on how many of six games they won or lost.

Author: Guo.T
 
Created:  03/03/2021
----------------------------------------------------------------------
'''
print("*****  Tournament Tracker *****")
print()

#ask for user input 6 times and count the number of W's 
win_count = 0
print("Enter the wins and losses for your team (W/L):")
for i in range(6):
  game = str(input())
  if game == "W":
    win_count +=1

#check conditions and output
if(win_count > 4):
  print("Your team is in Group 1")
elif(win_count > 2):
  print("Your team is in Group 2")
elif(win_count > 0):
  print("Your team is in Group 3")
else:
  print("Your team is eliminated from the tournament :c")