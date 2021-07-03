
# 2. Write a function in python that will take a list of numbers n as input and return the largest 2 elements in the list. Don't use the sort method

a = [1, 2, 3, 4, 5]
def large(a):
    max = a[0]
    for x in a:
        if x > max:
            max = x
    return max

print("largest element in m is:", large(a))


a.remove(large(a))
print("largest 2nd element in m is:", large(a))
