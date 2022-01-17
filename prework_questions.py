# Question 1

# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.


def hello_name(user_name):
    """prints hello_NAME"""
    print(f'hello_{user_name.upper()}')

hello_name('john')


# Quetion 2

# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for num in range(101):
        """prints all odd numbers between 1 and 100"""
        if num % 2 == 1:
            print(num)

first_odds()


# Question 3

# Please write a Python function, max_num_in_list to return the max number of a given list. 

nums = [12, 56, 154, 80, 12, 9, 100]

def max_num_in_list(a_list):
    """returns maximum number in a list of numbers"""
    max_num = max(a_list)
    return max_num


print(max_num_in_list(nums))


# Question 4

#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
#The return should be boolean Type (true/false).

def is_leap_year(a_year):
        """returns whether any year is a leap year"""
        if (a_year % 400 == 0) or (a_year % 4 == 0 and a_year % 100 != 0):
            return  True
        else:
            return False

print(is_leap_year(2400 ))


# Question 5

# Write a function to check to see if all numbers in list are consecutive numbers. 
#  For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.

num_list = [1,2,3,4,5]

def is_consecutive(a_list):
        """checks whether all numbers in a list are consecutive"""
        new_list = list(range(min(a_list), max(a_list) + 1))  # create new consecutive list and compare it to the original one
        if a_list == new_list:  
            return True
        else:
            return False

print(is_consecutive(num_list))





