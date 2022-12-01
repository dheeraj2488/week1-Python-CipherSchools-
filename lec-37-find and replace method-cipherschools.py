string =" her name is dheeraj and is good footballer"
print(string.replace("is","was",1)) #1 means i want to chnge only one is in the string first is 

#find method
print(string.find("is",9))

is_pos1=string.find("is")
is_pos2=string.find("is",is_pos1+1)
print(is_pos2)