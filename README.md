# Baruch_CIS_Project8
This was my 9th project in my CIS 2300 "Programming and Computational Thinking" led by professor Sadat Chowdhury

# Project Description

For this project, I will define a function as follows:

```python
def is_prime(num):
    # modify function to return True only if num is a prime number
    # A prime number is any positive integer greater than 1 that is only divisible by two numbers: 
    # 1 and num.
    # By definition 2 is a prime number, and it is the ONLY even prime number. 
    
    # This is a dummy implementation -- for now, this function returns True.
    return True
```

This function can be designed in several ways. Here are two methods:

Method 1) We would like to determine if num is a prime number. If num == 2, then num is prime. Otherwise, if num is divisible by any number between 2 and (num-1) then, num must be prime. It is advisable to set up a loop that iterates from 2 to (num-1) inclusive to determine if any of those numbers evenly divides num. If any  of them divides num, num cannot possibly be prime, so the function should return False; otherwise, if none of them divides, the function should return True

Method 2) We would like to determine if num is a prime number. Let us count all numbers from 1 to num that evenly divides num. If that count is exactly 2, then num must be a prime number. It is recommended to set up a loop that iterates from 1 to num inclusive to determine how many of those numbers evenly divide num. If that count is 2, the function should return True; otherwise, it should return False.

Please use one of these approaches to define your is_prime() function. Here are the first few prime numbers below 100:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

To test if the function is working, the function should return True for the values above. 

Once the function properly working, design a program that prints out the first prime number that is larger than your unique 5-digit number.

The main program should be called is_prime(). Please do not use any built-in math functions to determine primes. 

The program should output a single numeric result.
