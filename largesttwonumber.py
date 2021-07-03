
# 1. Write a function in python that will take a list of numbers n as input and return the largest element in the list. Don't use the sort method.
def large(list):
    lar = list[0]

    for x in list:
        if x > lar:
            lar = x

    return lar

list = []

num = int(input("Enter number of elements in list: "))

for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list.append(ele)

print("largest element is:", large(list))

