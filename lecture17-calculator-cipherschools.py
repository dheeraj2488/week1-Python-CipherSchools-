a= int(input("enter any number1"))
b= int(input("enter any number2"))
#by int we means the integer otherise it is a string
print("addition is", a+b)
print("subtraction is", a-b)
print("multiplicatiin is", a*b)
print("floating division is", a/b)
print("exponentiaion is", a**b)
print("integer division is", a//b)
print("modulus", a%b)
print(a**0.5) #for under rooot value
print(round(a**0.5,4))
#precedence rule
print((a+b)*b/a%b)
print((a+b)/b*a) #left to right, highest is for paranthases
print(a**b**a) #right to left