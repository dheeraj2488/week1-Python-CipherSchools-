# if we want to two or more input in one line  we use the split function
name, age = input("enter your name and age").split()
print(name)
print(age)

# if we dont want to use the space we can use , also by
name, age = input("enter your name and age").split(",")
print(name)
print(age)