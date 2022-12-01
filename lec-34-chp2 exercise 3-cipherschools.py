#we have to count character in the string 
name,char=input().split(",")
print(len(name))
print(f"the count of h is {name.lower().count(char.lower())}")