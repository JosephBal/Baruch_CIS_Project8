# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 16:33:41 2023

@author: Admin
"""

#### function definitions ####

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num

#### main program #####
num = 65875
while not is_prime(num):
    num += 1

print(num)



    


# your ultimate objective is to print the first prime number that is larger than your 5 digit 
# unique number.
    

