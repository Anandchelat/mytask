
# 3. Write a function in Python that will take a list of numbers n and a number m as inputs and return the largest m numbers in the list n. Don't use the sort method.

# n list
n = []

num = int(input("Enter number of elements in list n: "))

for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    n.append(ele)


# m list
m = []

num = int(input("Enter number of elements in list m: "))

for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    m.append(ele)


print(n)
print(m)

def large(m):
    max = m[0]
    for x in m:
        if x > max:
            max = x
    return max

print("largest element in m is:", large(m))