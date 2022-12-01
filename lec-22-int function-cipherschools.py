# assume we are creating a function we have to take two numbers input from the user and we have to give print the sum of that two numbers
#as we know the input function take a string as a input as a default so for using as a integer we have to declare it by int function
firstno=input("enter any no:")
secondno=input("enter any no:")
add=firstno+secondno
print(add) #this will give the string as a output 

#after using the int function
firstno=int(input())
secondno=int(input())
add=firstno+secondno
print("the sum is: ",add)

# we can add int and float but not int and string
d=float(input())
e=int(input())
print(d+e) #gives float value