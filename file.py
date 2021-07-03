
# 5. Write a function that will take a file name fname and a string s as input. It will return whether s occurs inside the file. It's possible that the file is extremely large so it cannot be read into memory in one shot.

f = open("fname.txt", "a")
f.write("hai i am Anand ")
f.close()


f = open("fname.txt", "r")
print(f.read())