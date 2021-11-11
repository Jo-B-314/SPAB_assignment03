# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

repeat = 100000
win = 0
loose = 0

for i in range(repeat):
    car = random.randrange(0,2)
    pick = random.randrange(0,2)
    
    if (car == pick):
        win += 1
    else:
        loose += 1
            
print("Without change: ","Amount of wins" ,win,"Amoount of looses", loose,
      "Percentage of wins", (win/repeat))

repeat = 100000
win = 0
loose = 0

for i in range(repeat):
    car = random.randrange(0,2)
    pick = random.randrange(0,2)
    #print("Car Door", car)
    #print("Picked Door", pick)

    
    # goat_doors are the doors the moderator can pick from
    goat_doors = [0,1,2]
    goat_doors.remove(car)

    if pick in goat_doors:
        goat_doors.remove(pick)
    
    if(len(goat_doors) > 1):
        moderator = random.choice(goat_doors)
    else:
        moderator = goat_doors[0]
    
    #print("Moderator Door", moderator)    
    doors = [0,1,2]
    doors.remove(pick)
    doors.remove(moderator)
    pick = doors[0]
    #print("Picked Door", pick)
    
    if (car == pick):
        win += 1
    else:
        loose += 1
            
print("With change: ", "Amount of wins" ,win,"Amoount of looses", loose,
      "Percentage of wins", (win/repeat))
