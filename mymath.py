# make a list of integer values from 1 to 100.
# create a function to return max value from the list
# create a function that return min value from the list
# create a function that return averaga value from the list.

# create unit test cases to test all the above functions.
# [ dont use python built in min function, write your own
# python script to test the list]


def max_num(a):
    myMax = a[0]
    for num in a:
        if myMax < num:
            myMax = num
    return myMax


def min_num(a):
    myMin = a[0]
    for num in a:
        if myMin > num:
            myMin = num
    return myMin


def avg_num(a):
    for num in a:
        average =  sum(a)/len(a)
    return average


