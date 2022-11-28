# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def count_down(input_num):
    new_list = []
    for x in range(input_num, -1, -1):
        new_list.append(x)
    return new_list

result = count_down(10)
print(result)

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(a,b):
    print(a)
    return(b)

x = print_and_return(1,2)
print(x)
#x prints the value of b returned by the function

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(some_list):
    a = some_list[0]
    b = len(some_list)
    print(a,b)
    return a+b

example = first_plus_length([1,2,3,4,5])
print(example)

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(some_list):
    new_list = []
    if len(some_list) < 2:
        return False
    else:
        for i in range(len(some_list)):
            if some_list[i] > some_list[1]:
                new_list.append(some_list[i])
        print(len(new_list))
        return(new_list)

test_case1 = values_greater_than_second([5,2,3,2,1,4])
print(test_case1)

test_case2 = values_greater_than_second([3])
print(test_case2)


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size, value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list

test_1 = length_and_value(4,7)
print(test_1)

test_2 = length_and_value(6,2)
print(test_2)